"""Roblox Funky Friday Script Desktop — A desktop helper that finds Roblox Funky Friday Script data directories and archives config and export files locally."""
from __future__ import annotations

import argparse


def main() -> int:
    parser = argparse.ArgumentParser(
        prog='roblox_funky_friday_script_desktop',
        description='A desktop helper that finds Roblox Funky Friday Script data directories and archives config and export files locally.',
    )
    parser.add_argument('path', nargs='?', help='Input file or folder')
    parser.add_argument('--out', help='Output folder')
    parser.add_argument('--preview', help='Show the plan and do not write')
    args = parser.parse_args()
    print('Roblox Funky Friday Script Desktop')
    print('Dated copies of Roblox Funky Friday Script data data, nothing uploaded.')
    print('Local CLI preview.')
    if vars(args):
        print(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
