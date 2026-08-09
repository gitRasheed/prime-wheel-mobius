#!/usr/bin/env bash
set -euo pipefail

if grep -RInE --include='*.lean' '\b(sorry|admit)\b' RHLean RHLean.lean; then
  echo 'Unfinished Lean proof found.' >&2
  exit 1
fi

if grep -RInE --include='*.lean' '^[[:space:]]*(axiom|constant)[[:space:]]' RHLean RHLean.lean; then
  echo 'New Lean axiom or opaque constant found.' >&2
  exit 1
fi

echo 'Lean source audit passed.'
