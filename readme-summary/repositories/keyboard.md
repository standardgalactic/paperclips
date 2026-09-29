# keyboard

**Summary**

The *Keyboard* repository hosts a neural‑network classifier that decides whether a given English word is more efficiently typed on the **QWERTY** or **Dvorak** keyboard layouts. It uses features derived from typing ergonomics—home‑row usage, common bigram patterns, letter frequency, and total key travel distance—to train a TensorFlow/Keras model (2 hidden layers, sigmoid output) achieving ~81 % accuracy on a curated dataset of the top 10,000 English words. The tool can be run from the command line to classify individual or multiple words, returning a score between 0 (QWERTY) and 1 (Dvorak). It is implemented entirely in CPU‑only Python code.

**KEYWORDS:** keyboard layout classifier, QWERTY, Dvorak, neural network, TensorFlow, Keras, typing ergonomics, home row usage, bigram patterns, letter frequency, key travel distance, word classification, command line tool.
