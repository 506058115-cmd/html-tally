#!/usr/bin/env python3
"""Count common HTML tags without printing text or attribute values."""

import argparse
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
import sys


# ponytail: cap parsing at 16 MiB; stream larger documents only if needed.
MAX_INPUT_BYTES = 16 * 1024 * 1024
COMMON_TAGS = frozenset(
    "a article audio body button div form h1 h2 h3 head header iframe img input "
    "label li link main meta nav ol option p script section select source span "
    "style svg table td textarea th title tr ul video".split()
)


class TagCounter(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.counts = Counter()

    def handle_starttag(self, tag, _attrs):
        self.counts[tag if tag in COMMON_TAGS else "other"] += 1


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Count common HTML tags without displaying text or attribute values."
    )
    parser.add_argument("file", type=Path, help="UTF-8 HTML file")
    args = parser.parse_args(argv)

    try:
        with args.file.expanduser().open("rb") as source:
            raw = source.read(MAX_INPUT_BYTES + 1)
        if len(raw) > MAX_INPUT_BYTES:
            raise ValueError("input exceeds the 16 MiB limit")
        html = raw.decode("utf-8-sig")
    except OSError as error:
        print(f"html-tally: cannot read input ({type(error).__name__})", file=sys.stderr)
        return 2
    except UnicodeError:
        print("html-tally: input is not valid UTF-8", file=sys.stderr)
        return 2
    except ValueError as error:
        print(f"html-tally: {error}", file=sys.stderr)
        return 2

    counter = TagCounter()
    counter.feed(html)
    counter.close()
    total = sum(counter.counts.values())
    print(f"start-tags={total}")
    if counter.counts:
        print(" ".join(
            f"{tag}={counter.counts[tag]}"
            for tag in sorted(counter.counts)
        ))
    else:
        print("(no start tags found)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
