# 结果、机制与证据语言

## 语料基线

30 篇语料在参考文献前约 20.2 万英文词。每篇平均约 263 个可识别句子，平均句长约 24 词；程序性描述大量使用被动语态，目标和贡献多使用 `this study`，第一人称 `we` 相对克制。该基线用于校准语气，不是硬性字数标准。

## 1. 结果强度阶梯

按证据强度选择动词：

| 强度 | 推荐表达 | 使用条件 |
|---|---|---|
| 直接观察 | `shows`, `exhibits`, `increases from ... to ...`, `is concentrated in ...` | 曲线、图像或测量直接支持。 |
| 比较结论 | `is higher/lower than`, `ranks as`, `differs by ...%` | 有明确基准和同口径比较。 |
| 关联 | `is associated with`, `correlates with`, `varies consistently with` | 未隔离因果，只观察同步变化。 |
| 受限解释 | `indicates`, `suggests`, `is consistent with` | 有间接机制证据或多指标互证。 |
| 因果 | `causes`, `governs`, `leads to`, `results from` | 控制变量、模型推导或充分证据排除主要替代解释。 |
| 证明 | `demonstrates conclusively`, `proves` | 一般避免；单组岩石力学试验几乎不应使用。 |

中文对应：`表明/呈现`用于事实，`说明/指示`用于解释，`可能与……有关/与……一致`用于间接机制，只有在设计支持时才写`导致/控制/决定`。

## 2. 把形容词换成证据

| 弱表达 | 改写方向 |
|---|---|
| 显著增大 | 给出起止值、增幅、效应量或统计检验；无统计检验时写“明显”也要给图中差值。 |
| 破坏更严重 | 给出裂纹数量/体积、峰后跌落、碎块尺度、能量峰值或可见剥落。 |
| AE 更活跃 | 给出事件数、累计计数、绝对能量、频段或时间窗口。 |
| 模型吻合良好 | 给出峰值、模量、曲线形状、裂纹路径等各自误差或一致性。 |
| 工程效果更好 | 给出回收率、含矸率、变形、稳定性指标、成本或约束。 |

`significant` 只在统计显著或工程意义明确时使用。若没有统计检验，优先 `marked`, `pronounced`, `substantial`，并紧跟量化证据。

## 3. 趋势词汇

### 单调与比较

- `increases/decreases monotonically with ...`
- `shows a positive/negative association with ...`
- `is X% higher/lower than the reference group`
- `follows the order A > B > C`
- 中文：`随……单调增大/减小`、`较对照组提高/降低 X%`、`排序为……`

### 非单调

- `first decreases and then increases, reaching a minimum at ...`
- `exhibits a U-shaped/inverted-U-shaped/wavy response`
- `shows a stepwise increase across successive stress levels`
- `remains stable before rising sharply near ...`
- 中文：`先降后升`、`呈U形/倒U形/波动型`、`阶梯式增长`、`在……前基本稳定，随后突增`

任何极值或“最优”必须同时写测试范围和基准，例如 `within the tested range of 0°–90°`。

### 阶段与转变

- `The response can be divided into three stages: ...`
- `A transition from tensile-dominated to shear-dominated failure occurs as ...`
- `The onset of unstable crack growth coincides with ...`
- `AE energy rises before/after the stress drop, indicating a temporal offset of ...`

不要把阶段命名当成证据；说明阶段边界由哪一曲线、阈值或事件定义。

## 4. 图表段落

推荐顺序：

1. `Figure X shows ...` 只用于定位；
2. 下一句立即说主趋势；
3. 给出关键值、差值或排名；
4. 指出异常、非单调或误差；
5. 给出受限解释。

英文示例骨架：

> Figure X compares [response] across [groups]. [Response] first [trend] and then [trend], reaching [extreme] at [condition]. Relative to [reference], [group] changes by [value]. This pattern coincides with [AE/crack/energy evidence], suggesting that [bounded mechanism].

中文示例骨架：

> 图X比较了不同[组别]下的[指标]。[指标]随[变量]先……后……，并在[条件]达到极值。与[基准]相比，[组别]变化[数值]。该变化与[AE/裂纹/能量证据]同步，说明/提示[有限机制解释]。

避免：`It can be seen from Fig. X that...` 连续出现；只描述每条曲线而不做比较；在图注之外重复设备信息。

## 5. 机制句的证据闭合

一条机制句至少包含“驱动—中介—响应”中的两个连接，并在邻句提供证据。

### 应力与裂纹

`The increase in [stress/rate] intensifies [stress concentration/redistribution] near [fissure/interface], promoting [crack initiation/coalescence] and thereby shifting the failure mode toward [mode].`

### 能量

`Because [constraint/path] limits lateral deformation, a larger fraction of the input energy is stored as elastic strain energy; its rapid release after [event] is consistent with [burst/ejection evidence].`

### 监测

`The decline in AE b-value, together with the rise in absolute energy and localized DIC strain, indicates a shift from distributed microcracking to fewer large-scale fracture events.`

### 颗粒与散体

`The rearrangement of force chains increases the coordination number in [region], reduces local voidage, and produces the observed layer-dependent compaction.`

如果只有数值模型中的力链或裂纹，应写“in the model”或“the simulation suggests”，不能直接声称真实材料内部已经被观察到。

## 6. 多源证据耦合

按独立性而不是仪器数量增强论证：

- 应力–应变 + AE：宏观承载与内部事件时序；
- DIC + CT：表面应变局部化与内部裂纹几何；
- 试验 + PFC/DEM/FDEM：现象与可解释的细观场；
- 能量 + 裂纹类型：能量分配与破坏模式；
- 数值 + 现场：机制可解释性与工程相关性。

不要把同一原始信号派生出的多个指标当成完全独立证据。AE counts、累计 counts 和 AE activity 可能高度相关；应说明它们的互补信息。

## 7. 结果与讨论的边界

结果句回答：

- 发生了什么？
- 在何条件下？
- 数量是多少？
- 与谁相比？

讨论句回答：

- 为什么可能发生？
- 哪些证据支持？
- 与既有研究何处一致/不同？
- 替代解释是什么？
- 结论适用于哪里？

合并 Results and Discussion 时，每一组仍保持 `事实 → 数字 → 机制 → 文献比较 → 边界`，不要先给机制再寻找数据。

## 8. 局限与展望

优先报告会改变结论外推的局限：

- 二维模型对三维裂纹几何的简化；
- 单一煤阶、岩性、含水状态或层理方向；
- 小样本、天然非均质性和重复不足；
- 预制裂隙与天然裂隙网络差异；
- 加载路径、围压、速率或角度范围有限；
- AE 阈值、窗口和传感器耦合影响；
- 数值参数非唯一性与标定/验证使用同一数据；
- 实验尺度到巷道/工作面尺度的跨尺度不确定性；
- 预印本或未经现场验证的工程建议。

局限句后接可执行展望：增加哪类变量、采用何种三维/原位监测、使用何种独立验证。不要只写 `more work is needed`。

## 9. 常见语病与逻辑风险

- `mechanical characterized parameters` → `mechanical parameters` 或 `characteristic mechanical parameters`。
- `cracks expansion` → `crack propagation`；`cracks distribution` → `crack distribution`。
- `with the increase of X` 可改为更紧凑的 `as X increases`。
- `the reason is because` 只保留一种因果结构。
- `respectively` 只在两个或多个序列一一对应且顺序清楚时使用。
- 不在同一句塞入背景、方法、结果和意义四种功能。
- 不把 `verified`、`validated` 用于仅与一条标定曲线一致的模型。
- 不把 `precursor` 用于峰后指标或仅一次出现的孤立信号。
