"""strcount: count reads that carry a run of a short tandem repeat motif.

A deliberately small program, written to exercise STRhub Verified. It is not
an analysis tool.
"""
import argparse
import collections
import re


def reads(path):
    """Sequences of a FASTQ file: the second line of every four."""
    with open(path) as handle:
        for number, line in enumerate(handle):
            if number % 4 == 1:
                yield line.strip().upper()


def longest_run(sequence, motif):
    """The largest number of consecutive copies of `motif` in `sequence`."""
    best = 0
    for match in re.finditer(f"(?:{re.escape(motif)})+", sequence):
        best = max(best, len(match.group(0)) // len(motif))
    return best


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--fastq", required=True, help="reads, FASTQ, uncompressed")
    parser.add_argument("--motif", default="AATG", help="repeat unit (default AATG)")
    parser.add_argument("--min-copies", type=int, default=3, help="smallest run counted (default 3)")
    parser.add_argument("--out", required=True, help="table to write, tab-separated")
    args = parser.parse_args()

    counts = collections.Counter()
    total = 0
    for sequence in reads(args.fastq):
        total += 1
        copies = longest_run(sequence, args.motif.upper())
        if copies >= args.min_copies:
            counts[copies] += 1

    with open(args.out, "w") as table:
        table.write("motif\tcopies\treads\n")
        for copies in sorted(counts):
            table.write(f"{args.motif.upper()}\t{copies}\t{counts[copies]}\n")
    print(f"{total} reads read, {sum(counts.values())} with {args.min_copies} or more copies of {args.motif.upper()}")


if __name__ == "__main__":
    main()
