"""agent1(b) secondary ensemble: dyadic-block correlation over the window
r < H at a fixed N (the a8 windows), complementing the pinned-sample ensemble."""
import numpy as np, csv, json, os, glob
D = os.path.expanduser('~/work/killtests2')
out = {}
for f in sorted(glob.glob(D + '/a8_window_*.csv')):
    rows = list(csv.DictReader(open(f)))
    B = np.array([[float(r['B%d' % j]) for j in range(16)] for r in rows])
    E = np.array([float(r['E']) for r in rows])
    keep = [j for j in range(16) if B[:, j].std() > 0]
    Bk = B[:, keep]
    C = np.corrcoef(Bk.T)
    off = ~np.eye(len(keep), dtype=bool)
    sab = np.abs(Bk).sum(axis=1)
    out[os.path.basename(f)] = dict(
        H=len(rows), n_blocks=len(keep),
        mean_offdiag_corr=float(C[off].mean()),
        pos_offdiag_frac=float(np.mean(C[off] > 0)),
        max_offdiag_corr=float(C[off].max()), min_offdiag_corr=float(C[off].min()),
        var_E_over_sum_var_Bj=float(E.var() / Bk.var(axis=0).sum()),
        mean_absE_over_sum_absBj=float(np.mean(np.abs(E) / sab)))
    print(os.path.basename(f), json.dumps(out[os.path.basename(f)], indent=1))
json.dump(out, open(D + '/a_window_dyadic_corr.json', 'w'), indent=1)
