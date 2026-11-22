# EvoNova Chem Core

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
![Status](https://img.shields.io/badge/TRL-3_Prototype-orange.svg)
![Validation](https://img.shields.io/badge/Double_Lock-Active-green.svg)
[![EvoNova Labs Ecosystem](https://img.shields.io/badge/EvoNova_Labs-Resilience_Stack-00F0FF)](https://github.com/pokushko/awesome-autonomous-agent-resilience)

**Evonova Chem Core** is the scientific kernel of the [EvoNova Catalyst](https://evonova.ai) platform. It implements the proprietary **Double Lock Validation™** and **EvoNova Engine** for evolutionary molecular design.

> **⚠️ Proprietary Technology:** The full source code of EvoNova Core is currently private and available only to authorized partners and grant reviewers upon request. This repository serves as a public documentation hub and issue tracker.

## 🧬 Core Technologies

### 1. Double Lock Validation™ (DLV)
A proprietary two-tier validation mechanism designed to eliminate "hallucinations" in generative AI models for chemistry.

*   **Lock 1 (Bibliographic):** Semantic verification against a cached corpus of 5M+ scientific articles (arXiv, PubMed, USPTO).
*   **Lock 2 (Domain-Specific):** Hard-coded physicochemical validation using RDKit and proprietary rulesets (Lipinski, QED, Synthetic Accessibility).

*Status: Validated in silico (Accuracy: 85% on ChEMBL benchmark).*

### 2. EvoNova Engine (Optimization)
A hybrid neuro-evolutionary engine that combines Large Language Models (LLM) with Genetic Algorithms (NSGA-II).

*   **Crossover Operator:** BRICS-based fragmentation and recombination.
*   **Mutation Operator:** Atom/Bond modification with valence checks.
*   **Selection:** Pareto-based selection for multi-objective optimization (Novelty vs. Stability vs. Toxicity).

*Status: TRL 3 Prototype Operational.*

### 3. QSAR Toxicity Module
Quantitative Structure-Activity Relationship prediction module based on multiple regression analysis.

*   **Registration:** Russian Federation Software Registration Certificate (RID) **No. 2025681960**.
*   **Methodology:** Weighted linear regression on 4 key descriptors (MW, LogP, TPSA, H-Donors).

## 📄 Intellectual Property

This software and its algorithms are protected by intellectual property laws of the Russian Federation.

*   **Rospatent Certificate No. 2025681960:** *Input Data Evaluation Software Based on Multiple Regression and Least Squares* (basis for regression/QSAR preprocessing).
*   **Rospatent Certificate No. 2026695054:** *Cascading Evolution System*.
*   **Rospatent Certificate No. 2026690237:** *Causal Analysis System*.
*   **Rospatent Certificate No. 2026667533:** *AI-Based Collective Hypothesis Verification Module*.
*   **FIPS Invention Patent App No. 2026161956:** *Hardware-Software Complex for Generating Physicochemical Synthesis Passports, Structural Novelty Control, and Cascading Compute Dispatch*.

## 📫 Contact & Access

For access to the private repository or to request a demo of the **EvoNova Catalyst** platform, please contact:

*   **Principal Investigator:** Roman Pokushko
*   **Email:** pokusko.roman@gmail.com
*   **Profile:** [VC.ru/id4836339](https://vc.ru/id4836339)

---
## 🌐 EvoNova Labs Open-Source Ecosystem

Part of the **[EvoNova Labs](https://pokushko.github.io)** open-source AI resilience & scientific integrity stack by **[Roman Pokushko](https://github.com/pokushko)**:

| Project | Role in Stack | Link |
| :--- | :--- | :--- |
| **Awesome Agent Resilience** | Curated index (`160` entries), MAST/OWASP Failure Taxonomy & `F01–F10` chaos benchmark | [pokushko/awesome-autonomous-agent-resilience](https://github.com/pokushko/awesome-autonomous-agent-resilience) |
| **AgentBunker** | 24/7 WAL intent journal, RSS memory ceiling watchdog & tri-state circuit breakers | [pokushko/agent-bunker](https://github.com/pokushko/agent-bunker) |
| **Orchestration Engine** | Zero-dependency `asyncio` MAS router, Kahn DAG waves & consensus reducers | [pokushko/orchestration-engine](https://github.com/pokushko/orchestration-engine) |
| **Agent Security Sandbox** | Pre-flight Python AST guard against dunder escapes & prompt-injection sanitizer | [pokushko/agent-security-sandbox](https://github.com/pokushko/agent-security-sandbox) |
| **Agentic Vector Memory** | Dual-store episodic & semantic memory with exponential decay & SQLite persistence | [pokushko/agentic-vector-memory](https://github.com/pokushko/agentic-vector-memory) |
| **EvoNova Causal Guard** | Pearl *do*-calculus DAG verifier, Tabu memory & multi-agent debate arbiter | [pokushko/evonova-causal-guard](https://github.com/pokushko/evonova-causal-guard) |
| **Sci Integrity Guard** | Cross-table numeric parity linter, CrossRef/OpenAlex DOI checker & LaTeX-to-OMML | [pokushko/sci-integrity-guard](https://github.com/pokushko/sci-integrity-guard) |
| **KTK ELOU-AVT Core** | Industrial cybernetic digital twin prototype for crude oil ELOU-AVT units | [pokushko/ktk_elou_avt_core](https://github.com/pokushko/ktk_elou_avt_core) |
| **EvoNova Chem Core** | RDKit molecular descriptor screening core for physical constraint enforcement | [pokushko/evonova-chem-core](https://github.com/pokushko/evonova-chem-core) |

---

## License

MIT License. Copyright (c) 2026 Roman Pokushko. See [LICENSE](LICENSE).
