![](https://github.com/acmucsd-projects/fa21-lion/blob/ML-setup/ML/img/banner.png?raw=true)

[![Python](https://img.shields.io/badge/Python-3.7-002c5c?logo=python&labelColor=002c5c)](https://www.python.org/)
[![PyTorch](https://img.shields.io/badge/Pytorch-1.10-ffffff?logo=pytorch&labelColor=ffffff)](https://pytorch.org/)
[![Kaggle](https://img.shields.io/badge/Kaggle-ffffff?logo=kaggle&labelColor=ffffff)](https://www.kaggle.com/)
[![Google Colab](https://img.shields.io/badge/Google%20Colab-ffffff?logo=googlecolab&labelColor=ffffff)](https://colab.research.google.com/)

## Table of Contents:
- [Requirements](https://github.com/acmucsd-projects/fa21-lion/tree/ML-setup/ML#requirements)
- [Source](https://github.com/acmucsd-projects/fa21-lion/tree/ML-setup/ML#source)
- [Datasets](https://github.com/acmucsd-projects/fa21-lion/tree/ML-setup/ML#datasets)
- [Logging](https://github.com/acmucsd-projects/fa21-lion/tree/ML-setup/ML#logging)
- [Difficulties](https://github.com/acmucsd-projects/fa21-lion/tree/ML-setup/ML#difficulties)
- [Author Info](https://github.com/acmucsd-projects/fa21-lion/tree/ML-setup/ML#author-info)
- [Thank you!](https://github.com/acmucsd-projects/fa21-lion/tree/ML-setup/ML#thank-you)

## Requirements ‼️

Refer to `requirements.txt` for the packages and dependencies. Note: `requirements.txt` was created via the command:

```cmd
!pip freeze > requirements.txt
```

within a *Colab* environment. Ensure you have a **Google account** —for experiment tracking of StyleGAN scripts. Ensure you have a Wandb account.
**Wandb** is another critical tool for our projects as it is used as an experiment tracker, a logger, and an artifact storage for our 
model weights and test runs. We also utilize **Kaggle** for creating, managing, and using datasets. Some of our files require a Kaggle account 
and an uploaded Kaggle.json API key for Kaggle datasets to download. 

Hardware-wise, a **Tesla P100** (offered in the Colab Pro subscription) is sufficient. There is an exception, however. Training StyleGAN requires heavy computational
power. Thus, a stronger GPU would be encouraged.

## Source 💡

Our source files are all written in python. However, the source files were originally executed in different environments. 
Below is a table indicating where the src files were ran for best convenience.

| src file                                 | Kaggle             | Colab              | Local              |
| :--------------------------------------: | :----------------: | :----------------: | :----------------: |
| DCGAN_TL2021.ipynb                       | :x:                | :heavy_check_mark: | :x:                |
| preprocess_mini_ffhq_1024.ipynb          | :x:                | :x:                | :heavy_check_mark: |
| pretrained_stylegan_morph.ipynb          | :x:                | :heavy_check_mark: | :x:                |
| pretrained_stylegan2ada_morph.ipynb      | :x:                | :heavy_check_mark: | :x:                |
| stylegan2ada_train.ipynb                 | :x:                | :heavy_check_mark: | :heavy_check_mark: |
| trained_stylegan2ada_morph.ipynb         | :x:                | :heavy_check_mark: | :x:                |
| trained_stylegan2ada_morph_exp.ipynb     | :x:                | :heavy_check_mark: | :x:                |
| trained_stylegan2ada_morph_logstep.ipynb | :x:                | :heavy_check_mark: | :x:                |

Below is another table indicating where our src/predict files were ran.

| src file   | Kaggle             | Colab              | Local              |
| :--------: | :----------------: | :----------------: | :----------------: |
| predict.py | :x:                | :x:                | :heavy_check_mark: |
| config.py  | :x:                | :x:                | :heavy_check_mark: |
| utils.py   | :x:                | :x:                | :heavy_check_mark: |


## Datasets 🗃️

- [Animal Faces](https://www.kaggle.com/andrewmvd/animal-faces) by Larxel
- [My Kaggle Dataset Version](https://www.kaggle.com/vincenttu/catfacesdatasetfferlito?select=dataset-part1) of the [GitHub Version of Cat Faces Dataset](https://github.com/fferlito/Cat-faces-dataset) by fferlito
- [Cats faces 64x64 (For generative models)](https://www.kaggle.com/spandan2/cats-faces-64x64-for-generative-models) by Spandan
- [cat2dog](https://www.kaggle.com/waifuai/cat2dog) by waifuai
- [celeba](https://www.kaggle.com/zuozhaorui/celeba) by Zhuo Zhaorui
- [FFHQ Face Data Set](https://www.kaggle.com/greatgamedota/ffhq-face-data-set) by GreatGameDota (ported from NVLabs)
- [celeba-hq](https://www.kaggle.com/lamsimon/celebahq) by Lam Simon
- [My Custom Cats Faces Dataset](https://www.kaggle.com/vincenttu/larxel-cat-faces) by Vincent Tu (created from AFHQ and Animal Faces by Larxel)
- [My Custom Human Faces Dataset](https://www.kaggle.com/vincenttu/mini-ffhq-512) by Vincent Tu (created from FFHQ)
- [My Custom Cat & Human Faces Dataset](https://www.kaggle.com/vincenttu/cat-human-faces) by Vincent Tu (created from FFHQ & AFHQ)
- [StyleGAN2-ADA Training Snapshots](https://www.kaggle.com/edwardyangiscool/stylegan-weights) by Edward Yang 

## Logging 📈

All logs, metrics, results, samples, and model weight files are kept on my (Vincent) wandb project [here](https://wandb.ai/vincenttu/DCGAN_TL2021?workspace=user-vincenttu).

![](https://github.com/acmucsd-projects/fa21-lion/blob/ML-setup/ML/img/OIP.jfif?raw=true)

![](https://github.com/acmucsd-projects/fa21-lion/blob/ML-setup/ML/img/wandb_showcase.gif?raw=true)


## Difficulties ❌

  There were a number of difficulties. Our objective of converting human faces to cat faces (ideally with an additional argument specifying how much to morph the human face) proved to be difficult. This task is not paired image translation. Morphing the structure of the human face and incorporating cat elements where appropriate is more so geometric transfiguration. Other difficulties included the traditional GAN issues such as instability, oscillation (lack of convergence), failure to learn, and learning static images to fool the discriminator. Our difficulties also entailed long training runs and experiment organization. 

This summary is non-exhaustive. More can be found in the presentation folder!

## Author Info 📚

- [Vincent Tu](https://github.com/alckasoc)
- [Arth Shukla](https://github.com/arth-shukla)
- [Edward Yang](https://www.linkedin.com/in/~edwardyang/) (Advisor)

## Thank you! 😀
