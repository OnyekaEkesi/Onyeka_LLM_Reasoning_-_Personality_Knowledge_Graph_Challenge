# -*- coding: utf-8 -*-
"""
Created on Fri Oct 24 22:00:36 2025

@author: USER
"""

import random
def generate_person(name):
    # Generate simple biography-like sentences plus trait-ground-truth
    traits = {t: round(random.uniform(0,1), 2) for t in ["openness","conscientiousness","extraversion","agreeableness","neuroticism"]}
    sentences = [
        f"{name} is a careful and organised project manager who always meets deadlines.",
        f"{name} enjoys reading speculative fiction and loves solving puzzles.",
        f"{name} often speaks confidently in meetings and likes leading teams.",
        f"{name} volunteers on weekends and is considerate towards colleagues."
    ]
    doc = " ".join(random.sample(sentences, k=3))
    # Ground truth triples (simple)
    triples = [
        (name, "occupation", "project manager"),
        (name, "hobby", "reading"),
        (name, "behavior", "volunteers")
    ]
    return doc, triples, traits
