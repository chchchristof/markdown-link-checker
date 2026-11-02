#!/usr/bin/env python3
"""Check local Markdown links without installing dependencies."""
import argparse
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

LINK = re.compile(r'(?<!!)\[[^\]]*\]\(([^)]+)\)')


def check(root):
    issues = []
    for file in sorted(root.rglob('*.md')):
        if '.git' in file.parts:
            continue
        for number, line in enumerate(file.read_text(encoding='utf-8').splitlines(), 1):
            for match in LINK.finditer(line):
                target = match.group(1).strip().split(maxsplit=1)[0].strip('<>')
                url = urlsplit(target)
                if url.scheme or url.netloc or not url.path or url.path.startswith('/'):
                    continue
                if not (file.parent / unquote(url.path)).exists():
                    issues.append(f'{file}:{number}: missing {target}')
    return issues


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('directory', nargs='?', default='.', help='directory to scan')
    args = parser.parse_args()
    root = Path(args.directory)
    if not root.is_dir():
        parser.error(f'not a directory: {root}')
    issues = check(root)
    if issues:
        print('\n'.join(issues))
        return 1
    print('No broken local Markdown links found.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
