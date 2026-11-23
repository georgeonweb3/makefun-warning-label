"""Warning Label for Humans: One Line, Big Laugh.

Writes one single-line safety warning label that should come printed on
every human being to /output/entry.txt. Deterministic, no network, no
randomness. The label is funny first and plausible second, in deadpan
printed-label wording, with the turn landing in the last few words.
"""

import os

ENTRY = (
    "WARNING: Do not ask this human to explain anything: they learned "
    "it five minutes ago and will present it as their own invention."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
