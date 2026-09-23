#demo edit for class
"""Tiny FASTA toolkit used to demo GitHub Actions."""
import sys


def read_fasta(path):
    """Return a dict of {sequence_id: sequence} from a FASTA file."""
    sequences = {}
    current_id = None
    with open(path) as handle:
        for line in handle:
            line = line.strip()
            if not line:
                continue
            if line.startswith(">"):
                current_id = line[1:].split()[0]
                sequences[current_id] = ""
            elif current_id is not None:
                sequences[current_id] += line.upper()
    return sequences


def gc_content(sequence):
    """Percentage of G and C bases in a DNA sequence (0-100)."""
    if not sequence:
        return 0.0
    gc = sequence.upper().count("G") + sequence.upper().count("C")
    return round(100 * gc / len(sequence), 2)


def summarize(path):
    """Print length and GC% for every sequence in a FASTA file."""
    for seq_id, seq in read_fasta(path).items():
        print(f"{seq_id}\tlength={len(seq)}\tGC={gc_content(seq)}%")


if __name__ == "__main__":
    summarize(sys.argv[1] if len(sys.argv) > 1 else "data/example.fasta")
