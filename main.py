"""Find leftover files of software that is no longer installed.

Usage: python3 main.py installed.csv leftovers.csv
installed.csv columns: software,version.
leftovers.csv columns: path,software (a scan of leftover files,
folders or registry entries, each attributed to a program name).
A leftover item belongs to an uninstalled program when its
software name is not in installed.csv. Items for software that
is still installed are skipped, not reported as leftovers.
Leftovers are grouped by program, most items first.
"""
import argparse, csv, sys

def find_leftovers(installed_rows, leftover_rows):
    installed = {row["software"].strip() for row in installed_rows}
    leftovers = {}
    skipped = 0
    for row in leftover_rows:
        software = row["software"].strip()
        if software in installed:
            skipped += 1
            continue
        leftovers.setdefault(software, []).append(row["path"].strip())
    ranked = sorted(leftovers.items(), key=lambda kv: (-len(kv[1]), kv[0]))
    return ranked, skipped

def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("installed")
    parser.add_argument("leftovers")
    args = parser.parse_args(argv)
    with open(args.installed, newline="", encoding="utf-8") as f:
        installed_rows = list(csv.DictReader(f))
    with open(args.leftovers, newline="", encoding="utf-8") as f:
        leftover_rows = list(csv.DictReader(f))
    ranked, skipped = find_leftovers(installed_rows, leftover_rows)
    for software, paths in ranked:
        print(f"{software}: {len(paths)} leftover item(s) - program not installed")
        for path in paths:
            print(f"  {path}")
    total = sum(len(paths) for _, paths in ranked)
    print(f"{total} leftover item(s) from {len(ranked)} uninstalled program(s); "
          f"{skipped} item(s) skipped (program still installed).")
    return 0

if __name__ == "__main__":
    sys.exit(main())
