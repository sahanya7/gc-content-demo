# GC Content Demo

![tests](https://github.com/sahanya7/gc-content-demo/actions/workflows/tests.yml/badge.svg)

A tiny bioinformatics script that reads a FASTA file and reports each
sequence's length and GC content, used to demonstrate GitHub Actions.

Every push automatically runs the analysis and the tests on Python 3.10,
3.11 and 3.12. See `.github/workflows/tests.yml`.

## Run it yourself

```bash
pip install -r requirements.txt
python fasta_stats.py data/example.fasta
pytest -v
```

## Use this in your own project

Copy `.github/workflows/tests.yml` into the same folder in your repo,
and change the last two steps to run your own script and tests.
