"""
Use the Brown corpus reader nltk.corpus.brown.words()
or the Web text corpus reader nltk.corpus.webtext.words()
 to access some sample text in two different genres.
"""
import nltk
from nltk.corpus import brown


cfd = nltk.ConditionalFreqDist(
    (genre,word)
    for genre in brown.categories()
    for word in brown.words(categories = genre)
    )
genres = ['news','religion','hobbies','science_fiction','romance','humor']
modals = ['can', 'could','may','might','must','will']
print cfd.tabulate(conditions = genres , samples = modals)
print nltk.corpus.brown.words(categories = genres[1])
