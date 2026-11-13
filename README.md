# strcount

Counts the reads of a FASTQ file that carry a run of a short tandem repeat
motif, by the number of consecutive copies.

This is a deliberately small program, written to exercise
[STRhub Verified](https://strhub.app/verified). It is not an analysis tool.

## Installation

```bash
pip install .
```

## Example

Reads `example/reads.fastq` (FASTQ, uncompressed) and writes `example/counts.tsv`,
a tab-separated table with one row per number of copies.

```bash
strcount --fastq example/reads.fastq --out example/counts.tsv
```

Expected output:

```
motif	copies	reads
AATG	3	2
AATG	5	2
AATG	6	4
AATG	7	2
AATG	9	6
AATG	11	1
AATG	12	1
```

## Options

| Option | Meaning |
|---|---|
| `--fastq` | reads, FASTQ, uncompressed |
| `--motif` | repeat unit (default `AATG`) |
| `--min-copies` | smallest run counted (default 3) |
| `--out` | table to write, tab-separated |

## License

MIT.
