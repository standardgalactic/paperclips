# Poisoned_prediction

The Poisoned_prediction repository implements a machine‑learning based detector for adversarial examples—inputs crafted to cause misclassification in neural networks. It builds on the concept of "poisoning attacks," where malicious data is injected into training sets to compromise model robustness. The project provides:

- A Python library (poisoned_prediction) with utilities to generate and evaluate poisoned datasets.
- Example scripts demonstrating how to apply poisoning techniques to common image classification models (e.g., ResNet, VGG).
- Benchmark experiments comparing detection accuracy against baseline methods like adversarial training.
- Documentation on the theoretical underpinnings, including mathematical formulations of perturbation strategies (e.g., Fast Gradient Sign Method).

The implementation is currently in beta; some features (e.g., support for transformer models) are marked as experimental. Dependencies include TensorFlow and NumPy.

KEYWORDS:
poisoning attack machine learning adversarial examples neural networks image classification fast gradient sign method tensorflow numpy
