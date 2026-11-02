# Markdown Link Checker

A tiny, dependency-free tool to find missing local links in Markdown files.

## Usage

Requires Python 3. Run:

```sh
python3 check_links.py path/to/docs
```

Omit the path to scan the current directory. The tool prints missing targets and exits with status 1 when it finds any; otherwise it exits with status 0. Links to websites, absolute paths, and fragment-only links are skipped. URL-encoded filenames and relative links with anchors are supported.

This is a lightweight checker, not a full Markdown parser: it does not validate anchors, reference-style links, links inside HTML, or links with nested parentheses. It may report links in code examples.

## Contributing

Issues and pull requests are welcome. Please describe the problem, include an example, and run `python3 -m unittest` before submitting changes.
