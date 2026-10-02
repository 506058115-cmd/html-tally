# html-tally

Count common HTML start tags without printing page text, attribute names, or attribute values. Less common and custom element names are grouped as `other`, so the summary does not echo names from the input.

Requires Python 3.8+ and uses only the standard library. Input must be UTF-8 (an optional BOM is accepted) and is limited to 16 MiB.

~~~sh
python html_tally.py page.html
~~~

This is a lightweight inventory, not an HTML validator or accessibility checker. Python's built-in `HTMLParser` accepts malformed markup and does not verify that start and end tags match. See the [Python `html.parser` documentation](https://docs.python.org/3/library/html.parser.html).

## Linux x86_64 downloads

- [Single-file build](https://github.com/506058115-cmd/html-tally/releases/download/v1.0.0/html-tally-linux-x86_64-onefile.tar.gz)
- [Directory build](https://github.com/506058115-cmd/html-tally/releases/download/v1.0.0/html-tally-linux-x86_64-onedir.tar.gz)
- [v1.0.0 release](https://github.com/506058115-cmd/html-tally/releases/tag/v1.0.0)

Archives include build information and dependency licenses; the Release includes SHA-256 checksums. Built in WSL Ubuntu 24.04 (Python 3.12.3, PyInstaller 6.22.2) for GNU/Linux x86_64. Older Linux distributions may require a compatible glibc. The packaged executable has not been run for functional validation.

## License

MIT. See [LICENSE](LICENSE).
