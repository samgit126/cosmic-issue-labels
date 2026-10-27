#!/usr/bin/env python3
"""Validate a COSMIC issue-labels CSV: schema, ranges, CFP arithmetic, and agreement when two raters are present.
Usage: python scripts/validate_labels.py data/examples.csv"""
import csv, sys
from collections import defaultdict
COLS = "issuekey,project,source_corpus,sizeable,reason,n_processes,entries,exits,reads,writes,cfp,rater,rater_confidence,adjudicated,notes".split(",")
path = sys.argv[1] if len(sys.argv) > 1 else "data/examples.csv"
rows = list(csv.DictReader(open(path, encoding="utf-8")))
errors = []
if rows and list(rows[0].keys()) != COLS: errors.append(f"columns differ from template: {list(rows[0].keys())}")
by_issue = defaultdict(dict)
for i, r in enumerate(rows, 2):
    try:
        e, x, rd, w, cfp, npr = (int(r[k]) for k in ("entries", "exits", "reads", "writes", "cfp", "n_processes"))
    except ValueError: errors.append(f"line {i}: non-integer count"); continue
    if r["sizeable"] not in ("yes", "no"): errors.append(f"line {i}: sizeable must be yes/no")
    if r["sizeable"] == "no" and r["reason"] not in ("non-functional", "insufficient-text"): errors.append(f"line {i}: reason required when not sizeable")
    if r["sizeable"] == "yes" and (npr < 1 or e < 1 or cfp < 2): errors.append(f"line {i}: sizeable issue needs >=1 process, >=1 Entry, >=2 CFP")
    if e + x + rd + w != cfp: errors.append(f"line {i}: cfp {cfp} != E+X+R+W {e+x+rd+w}")
    if r["rater_confidence"] not in ("1", "2", "3"): errors.append(f"line {i}: rater_confidence must be 1-3")
    by_issue[r["issuekey"]][r["rater"]] = (r["sizeable"], cfp)
pairs = [v for v in by_issue.values() if len(v) == 2]
if pairs:
    a, b = zip(*[tuple(v.values()) for v in pairs])
    agree_sz = sum(p[0] == q[0] for p, q in zip(a, b)) / len(pairs)
    mad = sum(abs(p[1] - q[1]) for p, q in zip(a, b) if p[0] == q[0] == "yes") / max(1, sum(p[0] == q[0] == "yes" for p, q in zip(a, b)))
    print(f"two-rater issues: {len(pairs)}  agreement on sizeable: {agree_sz:.2f}  mean |ΔCFP| on sizeable: {mad:.2f}")
print(f"{len(rows)} rows checked, {len(errors)} problems"); [print(" -", e) for e in errors]; sys.exit(1 if errors else 0)
