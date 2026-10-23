---
name: coal-rock-mechanics-writing
description: Draft, restructure, polish, or audit Chinese and English coal/rock mechanics manuscripts involving loading-unloading paths, fracture and damage, energy evolution, acoustic emission, DIC/CT, PFC/DEM/FDEM, creep, or top-coal caving. Use for manuscript sections and argument design in this domain; do not use for literature retrieval or for inventing analyses from absent data.
metadata:
  version: "1.0.0"
  corpus: "30 user-provided coal-rock mechanics papers, 536 pages"
---

# Coal–Rock Mechanics Writing

Use this skill to turn author-provided evidence into a rigorous coal/rock mechanics argument. It distills recurring terminology and reasoning patterns from a 30-paper corpus while avoiding phrase copying and unsupported factual transfer.

## Route the task

Always read [references/terminology-ledger.md](references/terminology-ledger.md) before drafting or revising. Then load only what the request needs:

- Abstract, introduction, conclusion, contribution framing, or full-paper architecture → [references/argument-logic.md](references/argument-logic.md).
- Results, discussion, figure interpretation, trend comparison, mechanism explanation, or limitations → [references/evidence-language.md](references/evidence-language.md).
- Experimental, numerical, coupled experimental–numerical, or field-validation methods → [references/method-patterns.md](references/method-patterns.md).
- Manuscript or section audit → [references/audit-checklist.md](references/audit-checklist.md), then run `scripts/audit_manuscript.py` when a local draft is available.
- Corpus provenance, coverage, or source-family questions → [references/corpus-index.md](references/corpus-index.md).

## Working method

1. **Lock the evidence boundary.** List the supplied materials, variables, loading path, specimen/model type, monitoring methods, comparisons, and measured outcomes. Mark missing information; never fill it with a value or conclusion borrowed from the corpus.
2. **Build the terminology ledger.** Select one canonical term for each material, defect, stress variable, energy component, monitoring index, and numerical model. Define abbreviations once and enforce them throughout.
3. **Identify the paper's contribution type.** Choose one primary type: stress-path effect, structural-defect effect, monitoring/precursor method, numerical-model development, experiment–simulation mechanism study, or engineering parameter optimization.
4. **Map the evidence ladder.** Prefer the domain sequence `mechanical response → energy partition/evolution → crack or damage evidence → mechanism → engineering implication`. Omit any rung unsupported by the author's evidence.
5. **Assign one argumentative job to each paragraph.** Common jobs are context, known evidence, unresolved gap, objective, method choice, trend, comparison, transition/threshold, mechanism, boundary, and implication.
6. **Draft conclusion-first paragraphs.** State the local finding, give quantitative or directly observable evidence, explain the mechanism at a strength justified by the evidence, then state the limited engineering meaning.
7. **Audit before delivery.** Check terminology, symbols, units, variable directions, figure/table references, causal strength, limitations, and consistency between abstract, results, discussion, and conclusion.

## Corpus-derived writing invariants

- Introductions narrow from engineering setting to the specific stress path, material structure, or monitoring gap; they end with an explicit objective and evidence package.
- Results paragraphs normally follow `finding → comparison/number → figure or signal evidence → local interpretation`.
- Discussions are strongest when they connect macro response to mesoscopic evidence instead of repeating trends: stress redistribution or force-chain change → crack initiation/propagation/coalescence → energy storage/dissipation/release → instability or failure mode.
- Conclusions use numbered, evidence-matched claims. Each item should answer a different question; do not restate the same trend with new wording.
- Quantified comparisons, rankings, extrema, thresholds, and transition points carry more weight than adjectives such as “obvious” or “significant”.
- Passive constructions are common for procedures; active constructions such as “this study investigates” are preferred for objectives and contributions. First-person plural should remain restrained.
- Engineering implications must name the operating condition or decision they inform. Avoid generic endings such as “provides theoretical support” without specifying support for what.

## Evidence and safety constraints

- Do not invent experimental conditions, sample counts, statistical significance, equations, model parameters, field validation, or uncertainty.
- Do not convert correlation into causation. Use “is associated with”, “is consistent with”, or “suggests” unless the design isolates the mechanism.
- Treat `fissure`, `fracture`, `crack`, and `joint` as different concepts unless the manuscript explicitly defines them as equivalent.
- Distinguish energy accumulation/storage, dissipation, release, and conversion. Do not call all of them “energy evolution” in the same sentence.
- Keep Results and Discussion separate when the target journal does; when combined, keep the evidence sentence before the mechanism sentence.
- Preserve negative and non-monotonic results. U-shaped, inverted-U, stepwise, wavy, threshold, and stage-dependent responses must not be flattened into “increases” or “decreases”.
- State the tested range when presenting an optimum, minimum-damage angle, threshold, or recommended parameter.
- Explicitly label preprints, numerical-only results, and model-dependent interpretations when relevant.
- Learn rhetorical moves from the corpus, not reusable wording. Do not reproduce long source passages or present corpus conclusions as the user's findings.

## Deliverable shape

For drafting or major restructuring, normally provide:

1. a compact terminology ledger;
2. a section-level argument map;
3. the requested prose;
4. a short evidence-boundary note listing unsupported or still-needed items.

For a narrow rewrite, return the revised passage directly and add only material terminology or evidence warnings. Match the user's requested language and journal style.
