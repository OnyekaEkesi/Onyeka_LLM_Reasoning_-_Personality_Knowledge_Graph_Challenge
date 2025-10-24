# -*- coding: utf-8 -*-
"""
Created on Fri Oct 24 21:59:15 2025

@author: USER
"""

import networkx as nx

def build_kg(triples, personality_dict=None):
    G = nx.DiGraph()
    for s,p,o in triples:
        G.add_node(s, type='entity')
        G.add_node(o, type='entity')
        G.add_edge(s, o, predicate=p)
    # personality_dict: {'Person Name': {'openness':0.7, ...}}
    if personality_dict:
        for person, traits in personality_dict.items():
            G.add_node(person, type='person')
            for trait, score in traits.items():
                trait_node = f"{person}::{trait}"
                G.add_node(trait_node, type='personality_trait', trait=trait, score=score)
                G.add_edge(person, trait_node, predicate='has_trait')
    return G