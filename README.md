# Med-KGRAG
我们将完成这个工作用于投稿 WWW 会议

## 介绍

### 当前 KG 中的实体标签类型
| labels                              | discription          |
|-------------------------------------|----------------------|
| ["Gene", "ALL_NODE"]                | 基因                 |
| ["SideEffect", "ALL_NODE"]          | 副作用               |
| ["BiologicalProcess", "ALL_NODE"]   | 生物过程             |
| ["MolecularFunction", "ALL_NODE"]   | 分子功能             |
| ["Compound", "ALL_NODE"]            | 化合物               |
| ["CellularComponent", "ALL_NODE"]   | 细胞成分             |
| ["PharmacologicClass", "ALL_NODE"]  | 药理分类             |
| ["Pathway", "ALL_NODE"]             | 路径                 |
| ["Disease", "ALL_NODE"]             | 疾病                 |
| ["Symptom", "ALL_NODE"]             | 症状                 |
| ["Anatomy", "ALL_NODE"]             | 解剖学               |
| ["Body", "ALL_NODE"]                | 身体                 |
| ["Item", "ALL_NODE"]                | 项目                 |
| ["Procedure", "ALL_NODE"]           | 程序                 |
| ["BioFragment", "ALL_NODE"]         | 生物片段             |
| ["Drug", "ALL_NODE"]                | 药物                 |
| ["Equipment", "ALL_NODE"]           | 设备                 |
| ["Microorganism", "ALL_NODE"]       | 微生物               |
| ["DNA", "ALL_NODE"]                 | DNA（脱氧核糖核酸）  |
| ["Protein", "ALL_NODE"]             | 蛋白质               |
| ["CellType", "ALL_NODE"]            | 细胞类型             |
| ["CellLine", "ALL_NODE"]            | 细胞系               |
| ["Department", "ALL_NODE"]          | 部门                 |
| ["RNA", "ALL_NODE"]                 | RNA（核糖核酸）      |
| ["DiseaseAndDiagnosis", "ALL_NODE"] | 疾病与诊断           |
| ["AnatomicalSite", "ALL_NODE"]      | 解剖位置             |
| ["Operation", "ALL_NODE"]           | 手术                 |
| ["Lab_Tests", "ALL_NODE"]           | 实验室测试           |
| ["ImagingExamination", "ALL_NODE"]  | 影像检查             |
| ["DiseaseOrPhenotypicFeature", "ALL_NODE"] | 疾病或表型特征 |
| ["GeneOrGeneProduct", "ALL_NODE"]   | 基因或基因产物       |
| ["ChemicalEntity", "ALL_NODE"]      | 化学实体             |
| ["OrganismTaxon", "ALL_NODE"]       | 生物分类             |
| ["SequenceVariant", "ALL_NODE"]     | 序列变异             |
| ["Test_Value", "ALL_NODE"]          | 测试值               |
| ["Test_items", "ALL_NODE"]          | 测试项目             |
| ["Test", "ALL_NODE"]                | 测试                 |
| ["Treatment", "ALL_NODE"]           | 治疗                 |
| ["ADE", "ALL_NODE"]                 | 不良反应（Adverse Drug Event）|
| ["Amount", "ALL_NODE"]              | 数量                 |
| ["Frequency", "ALL_NODE"]           | 频率                 |
| ["Duration", "ALL_NODE"]            | 持续时间             |
| ["Level", "ALL_NODE"]               | 等级                 |
| ["Pathogenesis", "ALL_NODE"]        | 发病机制             |
| ["Reason", "ALL_NODE"]              | 原因                 |
| ["Class", "ALL_NODE"]               | 分类                 |
| ["Method", "ALL_NODE"]              | 方法                 |
| ["CHEMICAL", "ALL_NODE"]            | 化学物质             |
| ["GENE", "ALL_NODE"]                | 基因                 |
| ["GENE-Y", "ALL_NODE"]              | 基因Y                |
| ["GENE-N", "ALL_NODE"]              | 基因N                |
| ["BRAND", "ALL_NODE"]               | 品牌                 |
| ["DRUG", "ALL_NODE"]                | 药物                 |
| ["GROUP", "ALL_NODE"]               | 组                   |
| ["DRUG_N", "ALL_NODE"]              | 药物N                |

### 当前 KG 中的关系类型
| relationshipType          | discription                |
|---------------------------|----------------------------|
| "INTERACTS_GiG"           | 基因间互作                  |
| "EXPRESSES_AeG"           | 表达                        |
| "DOWNREGULATES_AdG"       | 下调表达                    |
| "PARTICIPATES_GpBP"       | 参与生物过程                |
| "CAUSES_CcSE"             | 引起副作用                  |
| "REGULATES_GrG"           | 调节基因                    |
| "PARTICIPATES_GpMF"       | 参与分子功能                |
| "UPREGULATES_AuG"         | 上调表达                    |
| "COVARIES_GcG"            | 共同变异                    |
| "PARTICIPATES_GpPW"       | 参与路径                    |
| "DOWNREGULATES_DdG"       | 下调基因表达                |
| "PARTICIPATES_GpCC"       | 参与细胞成分                |
| "DOWNREGULATES_CdG"       | 下调化合物表达              |
| "UPREGULATES_DuG"         | 上调基因表达                |
| "BINDS_CbG"               | 结合基因                    |
| "UPREGULATES_CuG"         | 上调化合物表达              |
| "RESEMBLES_CrC"           | 类似                        |
| "LOCALIZES_DlA"           | 定位于                      |
| "ASSOCIATES_DaG"          | 关联基因                    |
| "PRESENTS_DpS"            | 显示症状                    |
| "TREATS_CtD"              | 治疗疾病                    |
| "PALLIATES_CpD"           | 缓解疾病                    |
| "RESEMBLES_DrD"           | 疾病类似                    |
| "INCLUDES_PCiC"           | 包含                        |
| "Association"             | 关联                        |
| "Positive_Correlation"    | 正相关                      |
| "Negative_Correlation"    | 负相关                      |
| "Bind"                    | 结合                        |
| "Drug_Disease"            | 药物与疾病                  |
| "Class_Disease"           | 分类与疾病                  |
| "Amount_Drug"             | 药物剂量                    |
| "Frequency_Drug"          | 药物频率                    |
| "ADE_Drug"                | 药物不良反应                |
| "Test_Disease"            | 测试与疾病                  |
| "Anatomy_Disease"         | 解剖与疾病                  |
| "Operation_Disease"       | 手术与疾病                  |
| "Treatment_Disease"       | 治疗与疾病                  |
| "Test_items_Disease"      | 测试项目与疾病              |
| "Symptom_Disease"         | 症状与疾病                  |
| "Reason_Disease"          | 疾病原因                    |
| "Pathogenesis_Disease"    | 疾病发病机制                |
| "Method_Drug"             | 药物方法                    |
| "Duration_Drug"           | 药物持续时间                |
| "Cotreatment"             | 联合治疗                    |
| "Drug_Interaction"        | 药物相互作用                |
| "Comparison"              | 比较                        |
| "Conversion"              | 转换                        |
| "ADE_Disease"             | 疾病的不良反应              |
| "Extract_From"            | 提取自                      |
| "EFFECT"                  | 效果                        |
| "MECHANISM"               | 机制                        |
| "INT"                     | 互作                        |
| "ADVISE"                  | 建议                        |
| "DIRECT-REGULATOR"        | 直接调节                     |
| "SUBSTRATE"               | 底物                        |
| "INDIRECT-DOWNREGULATOR"  | 间接下调                     |
| "INDIRECT-UPREGULATOR"    | 间接上调                     |
| "AGONIST"                 | 激动剂                      |
| "ANTAGONIST"              | 拮抗剂                      |
| "INHIBITOR"               | 抑制剂                      |
| "ACTIVATOR"               | 激活剂                      |
| "PART-OF"                 | 一部分                      |
| "PRODUCT-OF"              | 产物                        |
| "AGONIST-ACTIVATOR"       | 激动剂激活                   |
| "SUBSTRATE_PRODUCT-OF"    | 底物的产物                  |
| "UPREGULATOR"             | 上调调节剂                  |
| "DOWNREGULATOR"           | 下调调节剂                  |
| "AGONIST-INHIBITOR"       | 激动剂抑制                  |


### 生成推理数据集结构
```
vqa-rad # 根目录
├── data
│   ├── test
│       ├── image
│       ├── data-reasoning-pre.json  # 包含推理数据的json文件
│       ├── data.json  # vqa-rad原始测试数据
│   ├── train
│       ├── image
│       ├── data.json  # vqa-rad原始训练数据
│   ├── test-00000-of-00001-e5bc3d208bb4deeb.parquet
│   ├── train-00000-of-00001-eb8844602202be60.parquet
```