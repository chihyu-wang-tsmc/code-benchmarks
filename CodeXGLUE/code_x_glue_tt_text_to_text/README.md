---
annotations_creators:
- found
language_creators:
- found
language:
- da
- en
- lv
- nb
- zh
license:
- c-uda
multilinguality:
- multilingual
size_categories:
- 10K<n<100K
source_datasets:
- original
task_categories:
- translation
task_ids: []
pretty_name: CodeXGlueTtTextToText
tags:
- code-documentation-translation
dataset_info:
- config_name: da_en
  features:
  - name: id
    dtype: int32
  - name: source
    dtype: string
  - name: target
    dtype: string
  splits:
  - name: train
    num_bytes: 8163175
    num_examples: 42701
  - name: validation
    num_bytes: 190332
    num_examples: 1000
  - name: test
    num_bytes: 190772
    num_examples: 1000
  download_size: 4322666
  dataset_size: 8544279
- config_name: lv_en
  features:
  - name: id
    dtype: int32
  - name: source
    dtype: string
  - name: target
    dtype: string
  splits:
  - name: train
    num_bytes: 3644111
    num_examples: 18749
  - name: validation
    num_bytes: 192511
    num_examples: 1000
  - name: test
    num_bytes: 190867
    num_examples: 1000
  download_size: 1997959
  dataset_size: 4027489
- config_name: no_en
  features:
  - name: id
    dtype: int32
  - name: source
    dtype: string
  - name: target
    dtype: string
  splits:
  - name: train
    num_bytes: 8761755
    num_examples: 44322
  - name: validation
    num_bytes: 203815
    num_examples: 1000
  - name: test
    num_bytes: 197127
    num_examples: 1000
  download_size: 4661188
  dataset_size: 9162697
- config_name: zh_en
  features:
  - name: id
    dtype: int32
  - name: source
    dtype: string
  - name: target
    dtype: string
  splits:
  - name: train
    num_bytes: 9592148
    num_examples: 50154
  - name: validation
    num_bytes: 192147
    num_examples: 1000
  - name: test
    num_bytes: 195237
    num_examples: 1000
  download_size: 4733144
  dataset_size: 9979532
configs:
- config_name: da_en
  data_files:
  - split: train
    path: da_en/train-*
  - split: validation
    path: da_en/validation-*
  - split: test
    path: da_en/test-*
- config_name: lv_en
  data_files:
  - split: train
    path: lv_en/train-*
  - split: validation
    path: lv_en/validation-*
  - split: test
    path: lv_en/test-*
- config_name: no_en
  data_files:
  - split: train
    path: no_en/train-*
  - split: validation
    path: no_en/validation-*
  - split: test
    path: no_en/test-*
- config_name: zh_en
  data_files:
  - split: train
    path: zh_en/train-*
  - split: validation
    path: zh_en/validation-*
  - split: test
    path: zh_en/test-*
---
# Dataset Card for "code_x_glue_tt_text_to_text"

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

- **Homepage:** https://github.com/microsoft/CodeXGLUE/tree/main/Text-Text/text-to-text
- **Paper:** https://arxiv.org/abs/2102.04664

### Dataset Summary

CodeXGLUE text-to-text dataset, available at https://github.com/microsoft/CodeXGLUE/tree/main/Text-Text/text-to-text

The dataset we use is crawled and filtered from Microsoft Documentation, whose document located at https://github.com/MicrosoftDocs/.

### Supported Tasks and Leaderboards

- `machine-translation`: The dataset can be used to train a model for translating Technical documentation between languages.

### Languages

da_en, lv_en, no_en, zh_en

## Dataset Structure

### Data Instances

#### da_en

An example of 'test' looks as follows.
```
{
    "id": 0, 
    "source": "4 . K\u00f8r modellen , og udgiv den som en webtjeneste .\n", 
    "target": "4 . Run the model , and publish it as a web service .\n"
}
```

#### lv_en

An example of 'train' looks as follows.
```
{
    "id": 0, 
    "source": "title : Pakalpojumu objektu izveide\n", 
    "target": "title : Create service objects\n"
}
```

#### no_en

An example of 'validation' looks as follows.
```
{
    "id": 0, 
    "source": "2 . \u00c5pne servicevaren du vil definere komponenter fra en stykkliste for .\n", 
    "target": "2 . Open the service item for which you want to set up components from a BOM .\n"
}
```

#### zh_en

An example of 'validation' looks as follows.
```
{
    "id": 0, 
    "source": "& # 124 ; MCDUserNotificationReadStateFilterAny & # 124 ; 0 & # 124 ; \u5305\u62ec \u901a\u77e5 , \u800c \u4e0d \u8003\u8651 \u8bfb\u53d6 \u72b6\u6001 \u3002 & # 124 ;\n", 
    "target": "&#124; MCDUserNotificationReadStateFilterAny &#124; 0 &#124; Include notifications regardless of read state . &#124;\n"
}
```

### Data Fields

In the following each data field in go is explained for each config. The data fields are the same among all splits.

#### da_en, lv_en, no_en, zh_en

|field name| type |              description               |
|----------|------|----------------------------------------|
|id        |int32 | The index of the sample                |
|source    |string| The source language version of the text|
|target    |string| The target language version of the text|

### Data Splits

|name |train|validation|test|
|-----|----:|---------:|---:|
|da_en|42701|      1000|1000|
|lv_en|18749|      1000|1000|
|no_en|44322|      1000|1000|
|zh_en|50154|      1000|1000|

## Dataset Creation

### Curation Rationale

[More Information Needed]

### Source Data

#### Initial Data Collection and Normalization

[More Information Needed]

#### Who are the source language producers?

[More Information Needed]

### Annotations

#### Annotation process

[More Information Needed]

#### Who are the annotators?

[More Information Needed]

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
```

### Contributions

Thanks to @madlag (and partly also @ncoop57) for adding this dataset.