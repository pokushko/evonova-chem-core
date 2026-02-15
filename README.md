# EvoNova Chem Core

![License](https://img.shields.io/badge/license-Commercial-blue.svg)
![Status](https://img.shields.io/badge/TRL-3_Prototype-orange.svg)
![Validation](https://img.shields.io/badge/Double_Lock-Active-green.svg)

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

*   **PrEVM No. 2025681960:** "Information system for generating input data for the DEA method based on a multiple regression model" (Basis for QSAR module).
*   **Pending (2026):** "EvoNova Engine — genetic algorithm optimization module".

## 📫 Contact & Access

For access to the private repository or to request a demo of the **EvoNova Catalyst** platform, please contact:

*   **Principal Investigator:** Roman Pokushko
*   **Email:** pokushko@mail.ru
*   **Profile:** [VC.ru/id4836339](https://vc.ru/id4836339)

---
*Copyright © 2023-2026 EvoNova Team. All Rights Reserved.*
