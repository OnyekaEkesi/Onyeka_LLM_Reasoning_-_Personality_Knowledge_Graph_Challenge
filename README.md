# Onyeka_LLM_Reasoning_Personality_Knowledge_Graph_Challenge
The Intellumia Internship Challenge

# 🧠 LLM Reasoning & Personality Knowledge Graph Challenge

This repository contains my solution to the **LLM Reasoning & Personality Knowledge Graph Challenge**, a Data Science internship assessment focused on evaluating research capability, reasoning with LLMs, and practical implementation of knowledge graph concepts.

---

## 🚀 Project Overview

The goal of this challenge is to **develop a Python solution** that:
1. Takes a **text document** as input,
2. **Extracts entities and relationships** to build a **Knowledge Graph (KG)**, and
3. **Models personality traits** of the subjects within the graph.

This open-ended problem emphasizes **logical reasoning**, **independent research**, and **effective LLM utilization** — not just code writing.  
Hence, every major design decision, experiment, and refinement step was guided by LLM-assisted reasoning.

---

## 📁 Repository Structure

```bash
llm-kg-personality/
├─ data/
│ ├─ synthetic/ # Generated sample documents + ground-truth triples & traits
│ ├─ output/ # Saved graph outputs (GraphML / JSON)
│
├─ notebooks/
│ ├─ 01_pipeline.ipynb # Full end-to-end demonstration notebook
│
├─ src/
│ ├─ preprocessing.py # Text preprocessing and sentence segmentation
│ ├─ extractors.py # Entity and relation extraction
│ ├─ llm_prompts.py # LLM prompt templates & call functions
│ ├─ kg_builder.py # Knowledge Graph construction
│ ├─ synthetic_generator.py # Synthetic data generation with personality traits
│ ├─ evaluate.py # Evaluation metrics for triples & traits
│
├─ LLM_SESSION/ # Saved LLM session screenshots / exports
│ ├─ session1.txt
│ ├─ session2.txt
│
├─ REPORT.md # Final short report (generated using LLM)
├─ README.md # This documentation file
├─ requirements.txt # Python dependencies
```

---

## 🧩 Approach Summary

The pipeline follows a hybrid **rule-based + LLM-guided** approach:

1. **Preprocessing** – Tokenize, segment, and extract entities using `spaCy`.
2. **Candidate Triple Extraction** – Use dependency patterns to form preliminary triples `(subject, predicate, object)`.
3. **LLM Refinement** – Ask an LLM to:
   - Validate triples
   - Canonicalize relations
   - Infer missing relationships
   - Derive personality traits (Big Five model)
4. **Knowledge Graph Construction** – Build a directed graph using `NetworkX`, linking entities and traits.
5. **Evaluation** – Compare against synthetic ground-truth using F1 for triples and RMSE for traits.

---

## 🧠 Personality Modelling

Personality traits are represented using the **Big Five (OCEAN)** model:
- **Openness**
- **Conscientiousness**
- **Extraversion**
- **Agreeableness**
- **Neuroticism**

Each person node is connected to trait nodes through `"has_trait"` edges, where trait nodes carry numeric scores (0–1).

Example representation:
```bash
Person: Alice
├── has_trait → openness (0.82)
├── has_trait → conscientiousness (0.90)
└── has_trait → extraversion (0.65)
```

---

## 🧬 Synthetic Data Generation

Since no real data is provided, synthetic biographies were generated programmatically.  
Each document contains short biographical sentences describing:
- Profession
- Habits / behaviors
- Interests
- Emotional tendencies

Ground-truth **triples** and **trait scores** were created alongside to enable evaluation.

Example:
```json
{
  "text": "Alice is a careful and organised project manager who enjoys reading speculative fiction.",
  "triples": [
    ["Alice", "occupation", "project manager"],
    ["Alice", "hobby", "reading"]
  ],
  "traits": {
    "openness": 0.77,
    "conscientiousness": 0.92,
    "extraversion": 0.54,
    "agreeableness": 0.81,
    "neuroticism": 0.28
  }
}
```

## 🔄 Workflow Summary
### 1. Generate Synthetic Data

```bash
Generate Synthetic Data
python src/synthetic_generator.py
```
### 2. Run Pipeline (Extraction + LLM Refinement + KG Building)

```bash
python src/synthetic_generator.py
```
### 3. Evaluate Model

```bash
python src/evaluate.py
```
### 4. Visualize Knowledge Graph
Inside the notebook:

```bash
import networkx as nx
nx.draw(G, with_labels=True)
```
## 📊 Evaluation Metrics

```

| Task                      | Metric                | Description                                       |
| ------------------------- | --------------------- | ------------------------------------------------- |
| **Triple Extraction**     | Precision, Recall, F1 | Match predicted triples against ground truth      |
| **Personality Inference** | RMSE                  | Compare predicted trait scores to ground truth    |
| **Qualitative Analysis**  | Manual Review         | Sanity-check correctness and consistency of graph |

```

## 🧰 Tools & Libraries

```td
| Category               | Tools                          |
| ---------------------- | ------------------------------ |
| **Core NLP**           | `spaCy`, `transformers`        |
| **Graph Construction** | `NetworkX`                     |
| **Evaluation**         | `scikit-learn`, `pandas`       |
| **LLM Assistance**     | ChatGPT / OpenAI API           |
| **Environment**        | Python ≥ 3.9, Jupyter Notebook |

```

