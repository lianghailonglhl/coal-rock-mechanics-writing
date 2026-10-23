#!/usr/bin/env python3
"""Fast terminology and argument audit for UTF-8 coal/rock mechanics drafts."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


ACRONYMS = {
    "AE": [r"acoustic emission", r"声发射"],
    "DIC": [r"digital image correlation", r"数字图像相关"],
    "CT": [r"computed tomography", r"计算机断层扫描", r"CT扫描"],
    "SEM": [r"scanning electron microscopy", r"扫描电子显微镜"],
    "DEM": [r"discrete element method", r"离散元法"],
    "FDEM": [r"finite.?discrete element method", r"有限.?离散元法"],
    "PFC": [r"particle flow code", r"颗粒流程序"],
    "PFC2D": [r"particle flow code", r"颗粒流程序"],
    "PFC3D": [r"particle flow code", r"颗粒流程序"],
    "DFN": [r"discrete fracture network", r"离散裂隙网络"],
    "GBM": [r"grain-based model", r"颗粒模型", r"晶粒模型"],
    "UCS": [r"uniaxial compressive strength", r"单轴抗压强度"],
    "LTCC": [r"longwall top-coal caving", r"长壁综放"],
    "MDR": [r"mining-to-drawing ratio", r"采放比"],
}

CAUSAL_STRONG = re.compile(
    r"\b(?:prove[sd]?|demonstrate[sd]? conclusively|cause[sd]?|govern[sd]?|determine[sd]?|lead[sd]? to)\b|"
    r"证明|证实|导致|决定|完全控制",
    re.I,
)

RESULT_SIGNAL = re.compile(
    r"\b(?:results? (?:show|indicate|reveal|demonstrate)|compared with|increases?|decreases?|higher than|lower than)\b|"
    r"结果表明|相比|增加|降低|高于|低于|呈现|排序为",
    re.I,
)

NUMBER = re.compile(r"(?<!\w)[+-]?\d+(?:\.\d+)?\s*(?:%|MPa|GPa|kPa|mm|μm|mJ|J|Hz|s|°)?")


def sentence_split(text: str) -> list[str]:
    parts = re.split(r"(?<=[。！？.!?])\s+|(?<=[。！？])", text)
    return [re.sub(r"\s+", " ", part).strip() for part in parts if part.strip()]


def snippets(text: str, pattern: re.Pattern[str], limit: int = 5) -> list[str]:
    found: list[str] = []
    for sentence in sentence_split(text):
        if pattern.search(sentence):
            found.append(sentence[:260] + ("…" if len(sentence) > 260 else ""))
        if len(found) >= limit:
            break
    return found


def abbreviation_issues(text: str) -> list[str]:
    issues: list[str] = []
    for acronym, expansions in ACRONYMS.items():
        match = re.search(rf"\b{re.escape(acronym)}\b", text)
        if not match:
            continue
        prefix = text[: match.end()]
        if not any(re.search(pattern, prefix, re.I) for pattern in expansions):
            issues.append(f"`{acronym}` 首次出现前未找到全称定义。")
    return issues


def paragraph_issues(text: str) -> list[str]:
    issues: list[str] = []
    paragraphs = [re.sub(r"\s+", " ", item).strip() for item in re.split(r"\n\s*\n", text) if item.strip()]
    for index, paragraph in enumerate(paragraphs, 1):
        english_words = len(re.findall(r"\b[A-Za-z][A-Za-z0-9-]*\b", paragraph))
        chinese_chars = len(re.findall(r"[\u4e00-\u9fff]", paragraph))
        if english_words > 260 or chinese_chars > 520:
            issues.append(
                f"第 {index} 段过长（约 {english_words} 个英文词、{chinese_chars} 个汉字），检查是否混合多个论证任务。"
            )
    return issues[:12]


def terminology_notes(text: str) -> list[str]:
    notes: list[str] = []
    defect_terms = {
        "fissure": len(re.findall(r"\bfissures?\b", text, re.I)),
        "crack": len(re.findall(r"\bcracks?\b", text, re.I)),
        "fracture": len(re.findall(r"\bfractures?\b", text, re.I)),
        "joint": len(re.findall(r"\bjoints?\b", text, re.I)),
    }
    used_defects = [term for term, count in defect_terms.items() if count]
    if len(used_defects) >= 3:
        notes.append(
            "同时使用了 " + ", ".join(f"`{term}`({defect_terms[term]})" for term in used_defects)
            + "；确认它们已分别定义，且没有为避免重复而互换。"
        )
    composite_variants = {
        "coal-rock combination": len(re.findall(r"\bcoal.?rock combinations?\b", text, re.I)),
        "coal-rock composite": len(re.findall(r"\bcoal.?rock composites?\b", text, re.I)),
        "coal-rock assemblage": len(re.findall(r"\bcoal.?rock assemblages?\b", text, re.I)),
        "coal-rock combination body": len(re.findall(r"\bcoal.?rock combination bod(?:y|ies)\b", text, re.I)),
    }
    used_composites = [term for term, count in composite_variants.items() if count]
    if len(used_composites) > 1:
        notes.append("煤岩组合体英文存在多个形式：" + ", ".join(used_composites) + "。请选择一个规范形式。")
    energy_terms = [
        term
        for term in ["input energy", "elastic energy", "elastic strain energy", "dissipated energy", "energy release"]
        if re.search(rf"\b{term}\b", text, re.I)
    ]
    if re.search(r"\benergy evolution\b|能量演化", text, re.I) and len(energy_terms) < 2:
        notes.append("使用了“能量演化”，但未稳定识别至少两种具体能量分量；检查定义与能量平衡。")
    return notes


def evidence_notes(text: str) -> list[str]:
    notes: list[str] = []
    result_sentences = [sentence for sentence in sentence_split(text) if RESULT_SIGNAL.search(sentence)]
    quantified = [sentence for sentence in result_sentences if NUMBER.search(sentence)]
    if result_sentences:
        ratio = len(quantified) / len(result_sentences)
        if ratio < 0.25:
            notes.append(
                f"仅 {len(quantified)}/{len(result_sentences)} 个结果型句子含数字或单位；增加差值、排序、极值、范围或阈值。"
            )
    strong = snippets(text, CAUSAL_STRONG)
    if strong:
        notes.append(f"发现 {len(re.findall(CAUSAL_STRONG, text))} 处强因果/证明类词语；逐项确认设计能排除替代解释。")
    if re.search(r"\bsignificant(?:ly)?\b|显著", text, re.I) and not re.search(
        r"\bp\s*[<=>]|confidence interval|置信区间|统计检验|effect size", text, re.I
    ):
        notes.append("使用了 significant/显著，但未识别统计检验或工程显著性的定义；检查是否应改为量化描述。")
    if re.search(r"\b(?:optimal|optimum)\b|最优", text, re.I) and not re.search(
        r"tested range|investigated range|在.*范围|试验范围", text, re.I
    ):
        notes.append("出现“最优/optimal”，但未识别测试范围限定。")
    if re.search(r"\bprecursor\b|前兆", text, re.I) and not re.search(
        r"before failure|prior to failure|time window|提前|破坏前|时间窗", text, re.I
    ):
        notes.append("出现“前兆/precursor”，但未识别时间先后或窗口定义。")
    if not re.search(r"\blimitations?\b|局限|适用范围|tested range|within the range", text, re.I):
        notes.append("未识别局限或适用范围表述；完整论文应说明外推边界。")
    return notes


def build_report(path: Path, text: str) -> str:
    abbreviation = abbreviation_issues(text)
    terminology = terminology_notes(text)
    evidence = evidence_notes(text)
    paragraphs = paragraph_issues(text)
    causal_examples = snippets(text, CAUSAL_STRONG)
    score = max(0, 100 - 6 * len(abbreviation) - 7 * len(terminology) - 8 * len(evidence) - 3 * len(paragraphs))

    lines = [
        "# 煤岩力学稿件快速审查",
        "",
        f"- 文件：`{path.name}`",
        f"- 字符数：{len(text):,}",
        f"- 快速完整度分数：{score}/100（仅用于定位问题，不代表学术质量）",
        "",
    ]
    for title, items in [
        ("缩写首次定义", abbreviation),
        ("术语一致性", terminology),
        ("证据与论证", evidence),
        ("段落结构", paragraphs),
    ]:
        lines.extend([f"## {title}", ""])
        if items:
            lines.extend(f"- {item}" for item in items)
        else:
            lines.append("- 未发现自动规则可识别的问题。")
        lines.append("")
    if causal_examples:
        lines.extend(["## 强因果表达示例", ""])
        lines.extend(f"- {item}" for item in causal_examples)
        lines.append("")
    lines.extend(
        [
            "## 人工复核提醒",
            "",
            "- 对照技能中的术语账本和科学审查清单逐项核对。",
            "- 自动规则无法判断数据真实性、公式正确性、图表一致性或机制是否真正被实验设计隔离。",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="UTF-8 .txt or .md manuscript")
    parser.add_argument("--output", type=Path, help="Optional Markdown report path")
    args = parser.parse_args()

    if args.input.suffix.lower() not in {".txt", ".md"}:
        raise SystemExit("Only UTF-8 .txt and .md files are supported.")
    text = args.input.read_text(encoding="utf-8")
    report = build_report(args.input, text)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(report, encoding="utf-8")
    else:
        print(report)


if __name__ == "__main__":
    main()
