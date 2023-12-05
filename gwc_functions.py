import random
import numpy as np


def get_complement(sequence):
  new_sequence = ""
  complement = {"A": "T",
                "T": "A",
                "C": "G",
                "G": "C"}

  for base in sequence:
    # check if not valid
    new_sequence += complement[base]

  return(new_sequence)


def transcribe_sequence(sequence):
  pairs = {'A': 'U', 'T':'A', 'C':'G', 'G':'C'}
  transcribed_seq = ''

  if (sequence[0:3] == "ATG"):
    sequence = get_complement(sequence)

  for base in sequence:
    transcribed_seq += pairs[base]

  return transcribed_seq


def translate_sequence(sequence):

  # make sure multiple of 3
  assert len(sequence) % 3 == 0, 'sequence is incomplete and cannot be transcribed'

  AA_map = {'AUA':'I', 'AUC':'I', 'AUU':'I', 'AUG':'M',
            'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACU':'T',
            'AAC':'N', 'AAU':'N', 'AAA':'K', 'AAG':'K',
            'AGC':'S', 'AGU':'S', 'AGA':'R', 'AGG':'R',
            'CUA':'L', 'CUC':'L', 'CUG':'L', 'CUU':'L',
            'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCU':'P',
            'CAC':'H', 'CAU':'H', 'CAA':'Q', 'CAG':'Q',
            'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGU':'R',
            'GUA':'V', 'GUC':'V', 'GUG':'V', 'GUU':'V',
            'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCU':'A',
            'GAC':'D', 'GAU':'D', 'GAA':'E', 'GAG':'E',
            'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGU':'G',
            'UCA':'S', 'UCC':'S', 'UCG':'S', 'UCU':'S',
            'UUC':'F', 'UUU':'F', 'UUA':'L', 'UUG':'L',
            'UAC':'Y', 'UAU':'Y', 'UAA':'_', 'UAG':'_',
            'UGC':'C', 'UGU':'C', 'UGA':'_', 'UGG':'W'}

  protein = ""

  # check end range
  for i in range(0, len(sequence), 3):
    codon = sequence[i:i+3]
    # break if stop codon
    if AA_map[codon] == "_":
      protein += AA_map[codon]
      break
    protein += AA_map[codon]

  return(protein)