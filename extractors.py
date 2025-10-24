# -*- coding: utf-8 -*-
"""
Created on Fri Oct 24 21:17:15 2025

@author: USER
"""

def simple_triple_extraction(doc):
    triples = []
    for sent in doc.sents:
        root = sent.root
        subj = None
        obj = None
        for child in root.children:
            if child.dep_.startswith("nsubj"):
                subj = child.text
            if child.dep_.endswith("obj") or child.dep_.endswith("dobj"):
                obj = child.text
        if subj and obj:
            triples.append((subj, root.lemma_, obj))
    return triples
