"""One-star review of an everyday essential.

Writes a single deadpan one-star review line to entry.txt inside the
output directory given by MAKEFUN_OUTPUT_DIR (defaults to /output).
The line is one sentence, no trailing newline, 160 characters or fewer.
"""

import os

# The review itself: sleep, the essential everyone relies on, reviewed
# the way a disappointed customer would review a faulty product.
ENTRY_LINE = (
    "Sleep takes eight hours every night and returns me to work just as "
    "tired, which is less like rest and more like a subscription "
    "I cannot cancel."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(ENTRY_LINE)


if __name__ == "__main__":
    main()
