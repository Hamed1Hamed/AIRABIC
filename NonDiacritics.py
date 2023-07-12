# -*- coding: utf-8 -*-
# pip install camel-tools
from camel_tools.utils.dediac import dediac_ar


def removeDiacritics(sentence):
    # Split the input into paragraphs
    paragraphs = sentence.split('\n')

    # Dediacritize each paragraph individually
    dediacritized_paragraphs = [dediac_ar(paragraph) for paragraph in paragraphs]

    # Join the dediacritized paragraphs back together
    dediacritized_sentence_str = '\n'.join(dediacritized_paragraphs)

    # Write to file
    with open("output.txt", "w", encoding='utf-8') as file:
        file.write(dediacritized_sentence_str)

    # print the number of characters in the output
    print(f"Number of characters in the output: {len(dediacritized_sentence_str)}")
