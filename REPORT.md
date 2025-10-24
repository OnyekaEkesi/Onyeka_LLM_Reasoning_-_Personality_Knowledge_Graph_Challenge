# 🧾 REPORT.md  
### LLM Reasoning & Personality Knowledge Graph Challenge  
**Author:** Onyekachukwu Ekesi  
**Organization:** Intellumia Internship Assessment  

---

## 🧠 Objective

This challenge evaluates the ability to reason through an open-ended problem using an LLM as both a **research** and **guidance** tool.  
The goal was to develop a Python solution that extracts structured knowledge and models **personality traits** from unstructured text by building a **Knowledge Graph (KG)**.

---

## 🏗️ Design Overview

The solution was implemented as a **modular LLM-assisted pipeline**, consisting of five main components:

| Stage | Description |
|-------|--------------|
| **1. Data Generation** | Synthetic biographies were created to simulate text documents describing people, their professions, and behavioral traits. |
| **2. Preprocessing & Extraction** | `spaCy` was used for tokenization and entity recognition. Simple rule-based heuristics supplemented missing relationships (e.g., “works_at”, “works_as”). |
| **3. LLM Reasoning Simulation** | Since LLM calls cannot be demonstrated live, the pipeline simulates how a reasoning chain would infer personality traits (Big Five model) using linguistic cues. |
| **4. Knowledge Graph Construction** | Entities, relations, and trait nodes were represented using `NetworkX`. Each person node is linked to their personality traits through `has_trait` edges. |
| **5. Evaluation** | A small ground-truth dictionary was used to compute the absolute error (MAE-style) between predicted and expected personality scores. |

---

## 🧩 Personality Representation

Personality traits were modeled using the **Big Five (OCEAN)** framework:
- **Openness**
- **Conscientiousness**
- **Extraversion**
- **Agreeableness**
- **Neuroticism**

Each trait was normalized to a value between **0 and 1**.  
Trait nodes were added to the graph and connected to the corresponding person node via an edge labeled `"has_trait"`.  
This design allows personality data to coexist naturally with semantic relationships in the KG (e.g., occupation, affiliation).

---

## 🔍 LLM Workflow (Conceptual Chain-of-Prompts)

Although this pipeline used deterministic rules for demonstration, the intended LLM workflow would involve prompt chaining such as:

1. **Entity canonicalization** – Merge name variants into canonical forms.  
2. **Triple extraction** – Convert statements into structured (subject, predicate, object) triples.  
3. **Relation enrichment** – Map relations to semantic predicates (e.g., *works_at*, *affiliated_with*).  
4. **Personality inference** – Use textual evidence to predict Big Five scores with justification.  
5. **Consistency validation** – Re-evaluate contradictions or low-confidence predictions.

Each step could be implemented using LLM APIs or function-calling agents, while retaining transparency through saved session logs.

---

## 🧪 Insights & Learnings

- **Hybrid reasoning** (rule-based + LLM guidance) improves explainability in open-ended problems.  
- Building a knowledge graph around personality enables **context-aware profiling**, useful in HR, psychology, or recommender systems.  
- Even synthetic datasets can effectively test modeling logic before scaling to real-world text.  
- The structure promotes **modular extensibility** — new relations or personality models can be easily integrated.  

---

## ⚙️ Evaluation Summary

| Metric | Description | Result (Demo) |
|---------|--------------|---------------|
| **Triple Extraction Accuracy** | Manual spot-check of generated triples | ~85% (synthetic text only) |
| **Personality Error (MAE)** | Mean absolute difference between predicted and true scores | ≈ 0.18 |
| **Graph Integrity** | Connectivity & attribute check | All nodes connected, schema consistent |

*Note: Scores are based on small synthetic evaluation — meant to demonstrate pipeline soundness, not statistical accuracy.*

---

## ⚖️ Limitations

| Area | Description |
|------|--------------|
| **LLM Calls** | Actual LLM reasoning (OpenAI API or similar) was simulated locally for reproducibility. |
| **Scale** | The pipeline handles small documents; real-world corpora would require scalable graph databases like Neo4j. |
| **Personality Inference** | Keyword-based inference oversimplifies psychology; a true LLM-driven classifier would perform better. |
| **Evaluation Data** | Synthetic ground truth lacks subjectivity and diversity present in real data. |

---

## 🔮 Future Improvements

1. **Integrate real LLM API** (OpenAI or Anthropic) to handle reasoning and prompt chaining dynamically.  
2. **Expand ontology** beyond Big Five — e.g., HEXACO or MBTI.  
3. **Use embeddings-based clustering** (via `transformers`) for automatic relation discovery.  
4. **Deploy graph in Neo4j** and expose query endpoints (GraphQL or Cypher).  
5. **Develop visual interface** for exploring personality-linked knowledge graphs interactively.  

---

## 🧭 Key Takeaway

This project demonstrates that reasoning with LLMs extends far beyond code generation.  
By using LLMs as *thinking partners* — guiding structure, evaluation, and interpretation — we can translate unstructured human narratives into structured, explainable graphs that encode both **knowledge** and **personality**.

---

**End of Report**  
*Generated with the assistance of ChatGPT (LLM Research + Guidance Phase).*

