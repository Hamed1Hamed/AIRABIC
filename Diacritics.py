# -*- coding: utf-8 -*-
# pip install camel-tools
from camel_tools.tagger.default import DefaultTagger
from camel_tools.disambig.bert import BERTUnfactoredDisambiguator

def addDiacritics(message):
    bertd = BERTUnfactoredDisambiguator.pretrained('msa')
    tagger = DefaultTagger(bertd, 'diac')

    diacritized_paragraphs = []
    paragraphs = message.split("\n")
    for paragraph in paragraphs:
        sentences = paragraph.split(". ")
        diacritized_sentences = []
        for sentence in sentences:
            words = sentence.split()
            diacritized_words = tagger.tag(words)
            diacritized_sentence = ' '.join(diacritized_words)
            diacritized_sentences.append(diacritized_sentence)
        diacritized_paragraph = '. '.join(diacritized_sentences)
        diacritized_paragraphs.append(diacritized_paragraph)

    diacritized_message = '\n'.join(diacritized_paragraphs)
    # open the output file in write mode and write the output to it
    with open('output.txt', 'w', encoding='utf-8') as f:
        f.write(diacritized_message)

    # print the number of characters in the output
    print(f"Number of characters in the output: {len(diacritized_message)}")
