"""
Day 112 - RNA Transcription

Exercism - Easy

Given a DNA strand, return its RNA complement (per RNA transcription).
Both DNA and RNA strands are a sequence of nucleotides.

The four nucleotides found in DNA are adenine (A), cytosine (C), guanine (G) and thymine (T).
The four nucleotides found in RNA are adenine (A), cytosine (C), guanine (G) and uracil (U).

Given a DNA strand, its transcribed RNA strand is formed by replacing each nucleotide with its complement:
    G -> C
    C -> G
    T -> A
    A -> U


"""

#!/bin/python3
def to_rna(dna_strand):
    if not dna_strand:
        return ""
    complements = {'G': 'C', 'C' : 'G', 'T': 'A', 'A' : 'U'}
    return "".join([complements[dna] for dna in dna_strand])



if __name__ == "__main__":
    assert to_rna("") == "", "Invalid DNA input"
    assert to_rna("C") == "G", "Incorrect RNA Transcription output."
    assert to_rna("G") == "C", "Incorrect RNA Transcription output."
    assert to_rna("T") == "A", "Incorrect RNA Transcription output."
    assert to_rna("A") == "U", "Incorrect RNA Transcription output."
    assert to_rna("ACGTGGTCTTAA") == "UGCACCAGAAUU", "Incorrect RNA Transcription output."
