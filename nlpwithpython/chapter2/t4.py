'''
    Read in the texts of the State of the Union addresses,
     using the state_union corpus reader.
     Count occurrences of men, women, and people in each document.
    What has happened to the usage of these words over time?
'''
from nltk.corpus import state_union

#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
