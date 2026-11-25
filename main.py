"""The Jealous Smoke Alarm — exactly one funny line.

The joke is a household appliance with a grudge: the smoke alarm
only screams when the cooking is actually going well, as if it were
jealous of the cook's confidence rather than warning about danger.
The personification is the whole punchline.

Prints the joke to stdout and writes the exact same line, with no
trailing newline, to /output/entry.txt. Standard library only, no
network access, no files read — the joke is a constant in this
file. The 200-character gate is checked on every run so an
over-long edit can never slip through silently. The alarm is not
broken, it is envious — and envy is funnier than a malfunction.
"""

import os
import sys

LINE = (
    "My smoke alarm only goes off when I am cooking something I am "
    "genuinely proud of, like it is jealous of my confidence."
)


def main() -> int:
    if not 1 <= len(LINE) <= 200:
        print(f"error: line is {len(LINE)} chars, must be 1-200",
              file=sys.stderr)
        return 1
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
