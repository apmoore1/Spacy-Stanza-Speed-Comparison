from typing import Iterable
import re

from nltk.corpus import webtext
from nltk.corpus import gutenberg
import stanza

def emma_book_paragraphs() -> Iterable[str]:
    emma = gutenberg.raw('austen-emma.txt')
    for match in re.finditer(r'(.*)\n\n', emma):
        yield match.group(0)

def wine_reviews() -> Iterable[str]:
    reviews = webtext.raw('wine.txt')
    for match in re.finditer(r'(.*)\n', reviews):
        if match.group(0).strip():
            yield match.group(0)

def batch_sort(data: Iterable[str]) -> Iterable[str]:
    data = sorted(data, key=lambda x: len(x), reverse=True)
    for value in data:
        yield value

def stanza_batch(data: Iterable[str], batch_size: int = 32) -> Iterable[str]:
    batch_str = ''
    current_batch_size = 0
    for sample in data:
        batch_str += f'{sample}'
        current_batch_size += 1
        if current_batch_size == batch_size:
            yield batch_str
            batch_str = ''
        else:
            batch_str += '\n\n'
    if batch_str:
        yield batch_str

from time import time
t = time()
nlp = stanza.Pipeline(lang='en', processors='tokenize,pos,ner,sentiment', tokenize_no_ssplit=True, tokenize_batch_size=32, ner_batch_size=200, 
                      sentiment_batch_size=200, use_gpu=False)
print(f'Loading time {time() - t}')
#t = time()
#for batch in stanza_batch(emma_book_paragraphs(), batch_size=200):
#    d = nlp(batch)
#print(f'Processing time {time() - t}')
t = time()
for batch in stanza_batch(batch_sort(wine_reviews()), batch_size=200):
    d = nlp(batch)
print(f'Processing time {time() - t}')
print('done')
