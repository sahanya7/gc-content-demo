from fasta_stats import gc_content, read_fasta


def test_gc_all_gc():
    assert gc_content("GGCC") == 100.0


def test_gc_half():
    assert gc_content("ATGC") == 50.0


def test_gc_none():
    assert gc_content("ATAT") == 0.0


def test_gc_lowercase():
    assert gc_content("atgc") == 50.0


def test_gc_empty():
    assert gc_content("") == 0.0


def test_read_fasta_ids_and_multiline():
    seqs = read_fasta("data/example.fasta")
    assert list(seqs) == ["seq1", "seq2", "seq3", "seq4"]
    assert seqs["seq4"] == "ATGCGCGCATAT"
