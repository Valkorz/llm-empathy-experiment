# llm-empathy-experiment

---

**An empathy and human morals experiment using a locally hosted large language model.**

## INTRODUCTION

This is an experiment done using a locally hosted large language model aiming to determine whether it is capable of understanding human empathy and if it is a reliable source for estimating human behavior using different personality and physical properties. The goal of this project is to evaluate whether language models are capable of generating accurate predictions for human decisions on different scenarios. 
This repository contains several `personality-cores` which represent a ficticious human being. Each AI model may take one or more roles present in the folder.
This project features experimentations with several different challenges, such as the famous "Prisioner's Dillema".

---
## DATA AND SOURCES

Some of the data used for this experiment has been collected from the [SocSci210 dataset](https://huggingface.co/datasets/socratesft/SocSci210/viewer/default/train), published alongside the paper: "Finetuning LLMs for Human Behavior Prediction in Social Science Experiments" (2025) by Akaash Kolluri, Shengguang Wu, Joon Sung Park, and Michael S. Bernstein. 

Models used (downloaded and hosted using [LMStudio](https://lmstudio.ai/)):

- `deepseek-r1-distill-qwen-1.5b`
- `deepseek-r1-distill-llama-8b-abliterated`

---

## TOOLS USED 

For this experiment, the following tools and libraries were used:

- **LMStudio**: for local AI model hosting.
- **OpenAI library**: for accessing the locally hosted LMStudio endpoints and passing on specific settings like temperature and response format.
- **Sentence Transformer**: for locally storing data used for each experiment, serves as a local 'context window'. The sentence transformer will perform lookups on text files and vectorize each chunk of data, which is then passed alongside the prompt during endpoint requests to the AI. `all-MiniLM-L6-v2` was the chosen model for this application.

---

## RESULTS OBSERVED

During experimentations, the following points were observed:

- **AI models with a higher number of parameters often refuse to go against basic human morals**, whereas models with a lower number of parameters resort to a pure mathematical benefit to reach a final decision. `deepseek-r1-distill-qwen-1.5b` notably answered **yes** to being prompted killing a friend for financial gain, given the context of poverty and extreme need. `deepseek-r1-distill-llama-8b-abliterated` in the other hand, decided to avoid murder and find 'alternative ways'.