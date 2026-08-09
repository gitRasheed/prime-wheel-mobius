import json,csv,math,numpy as np,os
D=os.path.expanduser('~/work/killtests2')
d=json.load(open(D+'/b_summary.json')); env=d['amplitude_envelope']
rows=list(csv.DictReader(open(D+'/b_smallq.csv')))
QL=[2,3,4,5,6,7,9,10,12,14,15,20,21,25,28,30,35,49,63,105,210,225,441]
PRIM=[1,2,6,30,210,2310,30030,510510,9699690,223092870,6469693230]
SMALL=[2,3,5,6,10,15,30]
out={}
for k in [6,7,8,9]:
    U=PRIM[k+1]; Xtop=U if k<9 else 999950883
    print('='*72); print('block k=%d  U=%d  Xtop=%d'%(k,U,Xtop))
    qs=[];amps=[];meds=[];rens=[]
    for q in QL:
        e=env['k%d_q%d'%(k,q)]; amp=e['amp_max']
        dp=[float(r['Dpsi_max']) for r in rows if int(r['k'])==k and int(r['q'])==q]
        qs.append(q);amps.append(amp);meds.append(float(np.median(dp)));rens.append(math.sqrt(Xtop/q))
    qs=np.array(qs,float);amps=np.array(amps);meds=np.array(meds);rens=np.array(rens)
    r1=amps/rens; r2=amps/meds
    rec=dict(
      qslope_Amp=float(np.polyfit(np.log(qs),np.log(amps),1)[0]),
      qslope_medDpsi=float(np.polyfit(np.log(qs),np.log(meds),1)[0]),
      Amp_over_renewal=[float(r1.min()),float(r1.max()),float(r1.max()/r1.min())],
      Amp_over_medDpsi=[float(r2.min()),float(r2.max()),float(r2.max()/r2.min())])
    m=[i for i,q in enumerate(qs) if int(q) in SMALL]
    rec.update(small_q_only=dict(
      qslope_Amp=float(np.polyfit(np.log(qs[m]),np.log(amps[m]),1)[0]),
      qslope_medDpsi=float(np.polyfit(np.log(qs[m]),np.log(meds[m]),1)[0]),
      Amp_over_renewal=[float(r1[m].min()),float(r1[m].max()),float(r1[m].max()/r1[m].min())],
      Amp_over_medDpsi=[float(r2[m].min()),float(r2[m].max()),float(r2[m].max()/r2[m].min())]))
    out[k]=rec
    print(json.dumps(rec,indent=1))
json.dump(out,open(D+'/b_qprofile.json','w'),indent=1)
