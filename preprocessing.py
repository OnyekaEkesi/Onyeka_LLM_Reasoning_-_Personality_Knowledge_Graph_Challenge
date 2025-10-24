# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import spacy
nlp = spacy.load("en_core_web_sm")

def preprocess_text(text):
    doc = nlp(text)
    sentences = [sent.text.strip() for sent in doc.sents]
    return doc, sentences

def extract_entities(doc):
    ents = []
    for e in doc.ents:
        ents.append({"text": e.text, "label": e.label_, "start": e.start_char, "end": e.end_char})
    return ents
