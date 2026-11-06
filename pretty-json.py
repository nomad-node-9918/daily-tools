#!/usr/bin/env python3
"""Pretty-print JSON from a file or stdin.

Usage:
    python pretty-json.py data.json
    cat data.json | python pretty-json.py
"""
import json
import sys


def main() -> None:
    if len(sys.argv) > 1:
        with open(sys.argv[1], encoding="utf-8") as f:
            data = json.load(f)
    else:
        data = json.load(sys.stdin)
    print(json.dumps(data, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
