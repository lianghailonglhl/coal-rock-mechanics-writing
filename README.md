# Coal–Rock Mechanics Writing Skill

面向煤岩力学论文写作的 Codex skill，用于中文或英文稿件的论证设计、章节起草、学术润色和一致性审查。

它适用于加载—卸载路径、裂隙与损伤、能量演化、声发射、DIC/CT、PFC/DEM/FDEM、蠕变和综放开采等主题。核心目标是把作者已有的实验、数值或现场证据组织成严谨的论文论证，而不是代替文献检索或从缺失数据中推断结论。

## 安装

将本仓库完整复制到 Codex skills 目录：

```text
$CODEX_HOME/skills/coal-rock-mechanics-writing
```

重新打开 Codex 后，可在煤岩力学论文写作、重构、润色或审查任务中自动触发，也可以明确指定：

```text
$coal-rock-mechanics-writing
```

## 内容

- `SKILL.md`：适用范围、工作流程和证据边界
- `references/terminology-ledger.md`：煤岩力学术语与表达规范
- `references/argument-logic.md`：引言、结果、讨论和结论的论证结构
- `references/evidence-language.md`：趋势、比较、机制和不确定性的表述强度
- `references/method-patterns.md`：试验、数值及联合验证的方法写法
- `references/audit-checklist.md`：投稿前审查清单
- `references/corpus-index.md`：形成该 skill 的文献范围与来源索引
- `scripts/audit_manuscript.py`：稿件一致性和常见风险的辅助检查脚本

## 设计原则

- 先锁定作者提供的证据，再组织论证。
- 保持术语、变量、单位和因果强度一致。
- 优先采用“力学响应 → 能量演化 → 裂纹/损伤证据 → 机制 → 工程意义”的证据链，但不补写缺失环节。
- 只学习文献中的术语、论证方式和结构模式，不复制原文，也不把文献结论当作用户自己的研究结果。

## 语料说明

该 skill 由 30 篇用户提供的煤岩力学论文归纳形成。仓库仅包含抽象后的写作规则、术语表和来源索引，不包含论文 PDF、论文正文或大段受版权保护的原文。

