---
annotations_creators:
- expert-generated
language_creators:
- found
language:
- code
license:
- c-uda
multilinguality:
- other-programming-languages
size_categories:
- 10K<n<100K
source_datasets:
- original
task_categories:
- text2text-generation
task_ids: []
pretty_name: CodeXGlueCcCodeRefinement
tags:
- debugging
dataset_info:
- config_name: medium
  features:
  - name: id
    dtype: int32
  - name: buggy
    dtype: string
  - name: fixed
    dtype: string
  splits:
  - name: train
    num_bytes: 32614786
    num_examples: 52364
  - name: validation
    num_bytes: 4086733
    num_examples: 6546
  - name: test
    num_bytes: 4063665
    num_examples: 6545
  download_size: 14929559
  dataset_size: 40765184
- config_name: small
  features:
  - name: id
    dtype: int32
  - name: buggy
    dtype: string
  - name: fixed
    dtype: string
  splits:
  - name: train
    num_bytes: 13006679
    num_examples: 46680
  - name: validation
    num_bytes: 1629242
    num_examples: 5835
  - name: test
    num_bytes: 1619700
    num_examples: 5835
  download_size: 5894462
  dataset_size: 16255621
configs:
- config_name: medium
  data_files:
  - split: train
    path: medium/train-*
  - split: validation
    path: medium/validation-*
  - split: test
    path: medium/test-*
- config_name: small
  data_files:
  - split: train
    path: small/train-*
  - split: validation
    path: small/validation-*
  - split: test
    path: small/test-*
---

# Dataset Card for "code_x_glue_cc_code_refinement"

## Table of Contents
- [Dataset Description](#dataset-description)
  - [Dataset Summary](#dataset-summary)
  - [Supported Tasks and Leaderboards](#supported-tasks)
  - [Languages](#languages)
- [Dataset Structure](#dataset-structure)
  - [Data Instances](#data-instances)
  - [Data Fields](#data-fields)
  - [Data Splits](#data-splits-sample-size)
- [Dataset Creation](#dataset-creation)
  - [Curation Rationale](#curation-rationale)
  - [Source Data](#source-data)
  - [Annotations](#annotations)
  - [Personal and Sensitive Information](#personal-and-sensitive-information)
- [Considerations for Using the Data](#considerations-for-using-the-data)
  - [Social Impact of Dataset](#social-impact-of-dataset)
  - [Discussion of Biases](#discussion-of-biases)
  - [Other Known Limitations](#other-known-limitations)
- [Additional Information](#additional-information)
  - [Dataset Curators](#dataset-curators)
  - [Licensing Information](#licensing-information)
  - [Citation Information](#citation-information)
  - [Contributions](#contributions)

## Dataset Description

- **Homepage:** https://github.com/microsoft/CodeXGLUE/tree/main/Code-Code/code-refinement
- **Paper:** https://arxiv.org/abs/2102.04664

### Dataset Summary

CodeXGLUE code-refinement dataset, available at https://github.com/microsoft/CodeXGLUE/tree/main/Code-Code/code-refinement

We use the dataset released by this paper(https://arxiv.org/pdf/1812.08693.pdf). The source side is a Java function with bugs and the target side is the refined one. All the function and variable names are normalized. Their dataset contains two subsets ( i.e.small and medium) based on the function length.

### Supported Tasks and Leaderboards

- `text2text-generation-other-debugging`: The dataset can be used to train a model for automatically fixing buggy code.

### Languages

- Java **programming** language

## Dataset Structure

### Data Instances

#### medium

An example of 'train' looks as follows.
```
{
    "buggy": "public static TYPE_1 init ( java.lang.String name , java.util.Date date ) { TYPE_1 VAR_1 = new TYPE_1 ( ) ; VAR_1 . METHOD_1 ( name ) ; java.util.Calendar VAR_2 = java.util.Calendar.getInstance ( ) ; VAR_2 . METHOD_2 ( date ) ; VAR_1 . METHOD_3 ( VAR_2 ) ; return VAR_1 ; }\n", 
    "fixed": "public static TYPE_1 init ( java.lang.String name , java.util.Date date ) { TYPE_1 VAR_1 = new TYPE_1 ( ) ; VAR_1 . METHOD_1 ( name ) ; java.util.Calendar VAR_2 = null ; if ( date != null ) { VAR_2 = java.util.Calendar.getInstance ( ) ; VAR_2 . METHOD_2 ( date ) ; } VAR_1 . METHOD_3 ( VAR_2 ) ; return VAR_1 ; }\n", 
    "id": 0
}
```

#### small

An example of 'validation' looks as follows.
```
{
    "buggy": "public java.util.List < TYPE_1 > METHOD_1 ( ) { java.util.ArrayList < TYPE_1 > VAR_1 = new java.util.ArrayList < TYPE_1 > ( ) ; for ( TYPE_2 VAR_2 : VAR_3 ) { VAR_1 . METHOD_2 ( VAR_2 . METHOD_1 ( ) ) ; } return VAR_1 ; } \n", 
    "fixed": "public java.util.List < TYPE_1 > METHOD_1 ( ) { return VAR_1 ; } \n", 
    "id": 0
}
```

### Data Fields

In the following each data field in go is explained for each config. The data fields are the same among all splits.

#### medium, small

|field name| type |          description           |
|----------|------|--------------------------------|
|id        |int32 | Index of the sample            |
|buggy     |string| The buggy version of the code  |
|fixed     |string| The correct version of the code|

### Data Splits

| name |train|validation|test|
|------|----:|---------:|---:|
|medium|52364|      6546|6545|
|small |46680|      5835|5835|

## Dataset Creation

### Curation Rationale

[More Information Needed]

### Source Data

#### Initial Data Collection and Normalization

Downloaded from GitHub Archive every public GitHub event between March 2011 and October 2017 and used the Google BigQuery APIs.
[More Information Needed]

#### Who are the source language producers?

Software Engineering developers.

### Annotations

#### Annotation process

Automatically annotated by filtering commit messages containing the pattern: ("fix" or "solve") and ("bug" or "issue" or "problem" or "error"). A statistically significant amount of samples (95% confidence level with 5% confidence interval) were manually evaluated by two authors to check if the filtered bug/fix pairs were correct. After all disagreements were settled, authors conclude that 97.6% were true positives.

#### Who are the annotators?

Heuristics and the authors of the paper.

### Personal and Sensitive Information

[More Information Needed]

## Considerations for Using the Data

### Social Impact of Dataset

[More Information Needed]

### Discussion of Biases

[More Information Needed]

### Other Known Limitations

[More Information Needed]

## Additional Information

### Dataset Curators

https://github.com/microsoft, https://github.com/madlag

### Licensing Information

Computational Use of Data Agreement (C-UDA) License.

### Citation Information

```
@article{DBLP:journals/corr/abs-2102-04664,
  author    = {Shuai Lu and
               Daya Guo and
               Shuo Ren and
               Junjie Huang and
               Alexey Svyatkovskiy and
               Ambrosio Blanco and
               Colin B. Clement and
               Dawn Drain and
               Daxin Jiang and
               Duyu Tang and
               Ge Li and
               Lidong Zhou and
               Linjun Shou and
               Long Zhou and
               Michele Tufano and
               Ming Gong and
               Ming Zhou and
               Nan Duan and
               Neel Sundaresan and
               Shao Kun Deng and
               Shengyu Fu and
               Shujie Liu},
  title     = {CodeXGLUE: {A} Machine Learning Benchmark Dataset for Code Understanding
               and Generation},
  journal   = {CoRR},
  volume    = {abs/2102.04664},
  year      = {2021}
}
@article{tufano2019empirical,
  title={An empirical study on learning bug-fixing patches in the wild via neural machine translation},
  author={Tufano, Michele and Watson, Cody and Bavota, Gabriele and Penta, Massimiliano Di and White, Martin and Poshyvanyk, Denys},
  journal={ACM Transactions on Software Engineering and Methodology (TOSEM)},
  volume={28},
  number={4},
  pages={1--29},
  year={2019},
  publisher={ACM New York, NY, USA}
}
```

### Contributions

Thanks to @madlag (and partly also @ncoop57) for adding this dataset.