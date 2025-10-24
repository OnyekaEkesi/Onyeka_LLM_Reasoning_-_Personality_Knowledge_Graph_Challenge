# -*- coding: utf-8 -*-
"""
Created on Fri Oct 24 21:22:02 2025

@author: USER
"""

import openai
openai.api_key = "YOUR_API_KEY"

def call_llm(prompt, model="gpt-4o-mini", max_tokens=400):
    resp = openai.ChatCompletion.create(
        model=model,
        messages=[{"role":"user","content":prompt}],
        max_tokens=max_tokens,
        temperature=0.1,
    )
    return resp['choices'][0]['message']['content']

def refine_triples_with_llm(sent, candidates):
    prompt = f"""You are an assistant that extracts factual triples (subject;predicate;object) from this sentence:
Sentence: \"{sent}\"
Candidate triples: {candidates}
Please:
1) Confirm which candidate triples are correct (TRUE/FALSE),
2) Suggest canonicalized triple(s) if different,
3) Brief justification (1 short line per triple).
Return JSON list of objects: {{'triple': [s,p,o], 'keep': true/false, 'canonical': [s,p,o], 'note': '...'}}"""
    return call_llm(prompt)