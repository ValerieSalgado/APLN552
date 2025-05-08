# APLN552: Special Topics in Natural Language Processing
## How Code-Switching and Cognates Affect Surprisal In Language Models 

# Project Overview

This project explores how a language model trained only on English handles bilingual input, particularly code-switching and cognates between English and Spanish. Inspired by Degani et al. (2018), who found that bilinguals activate both languages during reading, this project investigates whether a statistical bigram model shows similar difficulty when encountering unexpected language switches.

The main question:  
**Does a model trained on English struggle to predict the next word when it sees Spanish or cognates?**

## Hypothesis

- The model will show **low surprisal** for English input (which it's trained on).
- It will show **high surprisal** for Spanish input and for sentences with cognates.
- Cognates alone won’t help the model predict if the surrounding context is unfamiliar.
