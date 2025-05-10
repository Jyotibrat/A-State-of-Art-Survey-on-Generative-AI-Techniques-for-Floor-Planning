# 🗂️ Datasets

This directory contains all the datasets used and referenced in the project **"A State-of-Art Survey on Generative AI Techniques for Floor Planning."**

It is organized into two subdirectories:

```

Datasets/
├── Augmented Dataset/
│   ├── bright_augmentation.jpg
│   ├── colored_augmentation.jpg
│   ├── dark_augmentation.jpg
│   ├── flipped_augmentation.jpg
│   ├── grayed_augmentation.jpg
│   ├── noisy_augmentation.jpg
│   ├── rotated_augmentation.jpg
│   └── README.md 
│
├── Original Dataset/
│   └── README.md
│
└── README.md
```

---

## 📁 Augmented Dataset

This subdirectory contains a **sample of the augmented dataset** generated using our custom image augmentation pipeline.

- The augmentations include:
  - Rotations (90° clockwise/counter-clockwise)
  - Horizontal and vertical flips
  - Brightness adjustments
  - Gaussian blur
  - Grayscale conversion
  - HSV color shifts
  - Random noise addition
- These augmentations were applied to enrich the diversity of the original dataset and improve model training performance.

👉 See the [`Augmented Dataset/README.md`](https://github.com/Jyotibrat/A-State-of-Art-Survey-on-Generative-AI-Techniques-for-Floor-Planning/blob/main/Datasets/Augmented%20Dataset/README.md) for more details.

---

## 📁 Original Dataset

This subdirectory **does not contain actual data** but provides licensing and citation information for the **ROBIN dataset**, which was used as the base for our experiments.

- Source: [https://github.com/gesstalt/ROBIN](https://github.com/gesstalt/ROBIN)
- License: GNU GPL v3.0
- Citation: Sharma et al., ICDAR 2017

👉 See the [`Original Dataset/README.md`](https://github.com/Jyotibrat/A-State-of-Art-Survey-on-Generative-AI-Techniques-for-Floor-Planning/blob/main/Datasets/Original%20Dataset/README.md) for citation and license details.

---

## ✅ Usage Summary

- Use the **Original Dataset** as the base input.
- Apply the **Augmented Dataset** for extended training and experimentation.
- This structure helps separate third-party datasets from project-specific contributions.

---

### Please refer to individual subdirectories for further instructions and licensing notes.