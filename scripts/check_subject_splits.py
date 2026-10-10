#!/usr/bin/env python3
"""Check whether any subject appears in more than one data split.

Example:
  python check_subject_splits.py --csv splits.csv --subject-col subject_id --split-col split --site-col site
"""
import argparse
import pandas as pd


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--csv', required=True)
    p.add_argument('--subject-col', default='subject_id')
    p.add_argument('--split-col', default='split')
    p.add_argument('--site-col', default=None)
    args = p.parse_args()

    df = pd.read_csv(args.csv)
    for col in [args.subject_col, args.split_col]:
        if col not in df.columns:
            raise SystemExit(f"Missing required column: {col}")

    per_subject = df.groupby(args.subject_col)[args.split_col].nunique()
    leaked = per_subject[per_subject > 1]

    print(f"Rows: {len(df):,}")
    print(f"Unique subjects: {df[args.subject_col].nunique():,}")
    print("\nSplit counts by unique subject:")
    print(df.drop_duplicates(args.subject_col)[args.split_col].value_counts(dropna=False).to_string())

    if len(leaked):
        print(f"\nWARNING: {len(leaked)} subject(s) occur in more than one split.")
        bad_ids = leaked.index.astype(str).tolist()
        print("Example leaked IDs:", ', '.join(bad_ids[:20]))
    else:
        print("\nPASS: no subject appears in more than one split.")

    if args.site_col and args.site_col in df.columns:
        print("\nUnique-subject distribution by site and split:")
        tmp = df.drop_duplicates(args.subject_col)
        print(pd.crosstab(tmp[args.site_col], tmp[args.split_col]).to_string())


if __name__ == '__main__':
    main()
