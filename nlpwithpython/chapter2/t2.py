"""Use the corpus module to explore austen-persuasion.txt. How many word tok
ens does this book have? How many word types?"""
from nltk.corpus import gutenberg
import nltk
gutenberg.fileids()
emma = nltk.Text(gutenberg.words('austen-persuasion.txt'))
print len(emma);
#emma.concordance("surprize")
