# 🧠 A State-of-Art Survey on Generative AI Techniques for Floor Planning

This repository contains the full research and survey workflow, source code, experiments, datasets, and results related to our Project.

Our Paper:
***"A State-of-Art Survey on Generative AI Techniques for Floor Planning"***

The goal of this paper is to explore how modern generative AI models, particularly text-to-image architectures like **Stable Diffusion**, can be applied to synthesize architectural floor plans from textual descriptions.

> ⚠️ **Note:** The paper itself is **not about the specific models we created** in this repository. Instead, it is a **survey-based study** that reviews how **architectural floor plans are being generated using generative AI techniques** in the current research and industry landscape.
> The included models and prototypes were developed as part of our own exploratory implementations inspired by the techniques surveyed.

---

## 🏆 Publication Highlight

📢 Our paper was **accepted** to the workshop **GenAICHI 2025** at the prestigious **CHI 2025** conference.

- 🗓️ **Workshop Date**: April 27, 2025  
- 🧩 **Workshop**: [GenAICHI 2025 – Generative AI and Human-Computer Interaction](https://generativeaiandhci.github.io/)  
- 🧠 **Conference**: [CHI 2025 – ACM Conference on Human Factors in Computing Systems](https://chi2025.acm.org/)  
- 📄 **Read the Paper**: [View PDF](https://generativeaiandhci.github.io/papers/2025/genaichi2025_6.pdf)

---

## 📁 Repository Structure

```
├── .github/
│   ├── ISSUE_TEMPLATE/
│   │   ├── bug_report.md
│   │   └── feature_request.md
│   └── README.md
│
├── Code/
│   ├── Data Augmentation Code/
│   │   ├── Image_Augmentation.ipynb
│   │   └── README.md
│   ├── Main Source Code/
│   │   ├── Floor Planning GEN AI.ipynb
│   │   ├── floor_planning_gen_ai.py
│   │   ├── requirements.txt
│   │   └── README.md
│   └── README.md
│
├── Datasets/
│   ├── Augmented Dataset/
│   │   ├── bright_augmentation.jpg
│   │   ├── colored_augmentation.jpg
│   │   ├── dark_augmentation.jpg
│   │   ├── flipped_augmentation.jpg
│   │   ├── grayed_augmentation.jpg
│   │   ├── noisy_augmentation.jpg
│   │   ├── rotated_augmentation.jpg
│   │   └── README.md
│   ├── Original Dataset/
│   │   └── README.md
│   └── README.md
│
├── Papers/
│   ├── Graphs and Charts/
│   │   ├── flowchart.png
│   │   ├── graph.png
│   │   ├── pie chart.png
│   │   └── titled graph.png
│   ├── Tables/
│   │   ├── Accuracy Table of papers.csv
│   │   ├── Datasets of papers.csv
│   │   ├── Final Table of Research Papers.csv
│   │   ├── Links of Datasets of papers.csv
│   │   ├── Search Strings.csv
│   │   └── Technologies table.csv
│   └── README.md
│
├── Prototypes/
│   ├── 01_First Prototype/
│   │   ├── First_Prototype.ipynb
│   │   └── README.md
│   ├── 02_Second Prototype/
│   │   ├── Second_Prototype.py
│   │   └── README.md
│   ├── 03_Third Prototype/
│   │   ├── Third_Prototype.ipynb
│   │   └── README.md
│   └── README.md
│
├── Results/
│   ├── IMAGE 1.png
│   ├── IMAGE 2.png
│   ├── IMAGE 3.png
│   ├── IMAGE 4.png
│   └── README.md
└── LICENSE
```

---

## 📌 Description

- **[Code/](https://github.com/Jyotibrat/Floor-Planning-Generative-AI/tree/main/Code)**: Contains all implementation files, including model training, inference, and data augmentation code.
- **[Datasets/](https://github.com/Jyotibrat/Floor-Planning-Generative-AI/tree/main/Datasets)**: Organized into the original dataset reference and the augmented dataset created during the project.
- **[Papers/](https://github.com/Jyotibrat/Floor-Planning-Generative-AI/tree/main/Papers)**: Includes visualizations, graphs, and raw table data used in our paper.
- **[Prototypes/](https://github.com/Jyotibrat/Floor-Planning-Generative-AI/tree/main/Prototypes)**: Experimental models built using Stable Diffusion to generate floor plans from text.
- **[Results/](https://github.com/Jyotibrat/Floor-Planning-Generative-AI/tree/main/Results)**: A small set of output images generated from the trained models and prototypes.

---

## 🛠️ How to Run

1. Clone this repo:
   ```bash
   git clone https://github.com/Jyotibrat/A-State-of-Art-Survey-on-Generative-AI-Techniques-for-Floor-Planning.git
   ```

2. Run the Colab notebooks or Python scripts from the respective prototype folders.

---

## 📄 Citation Details

If you use this repository or refer to our work, please cite:

### Plain Text

```text
JAIN, ANKUR, BINDUPAUTRA JYOTIBRAT, ARUNIM GOGOI, RANA TALUKDAR, AVINASH KUSHWAHA, and NAVJOT SINGH GILL. "A State-of-Art Survey on Generative AI Techniques for Floor Planning." (2025).
```

### BibTex

```bibtex
@article{jain2025state,
  title={A State-of-Art Survey on Generative AI Techniques for Floor Planning},
  author={JAIN, ANKUR and JYOTIBRAT, BINDUPAUTRA and GOGOI, ARUNIM and TALUKDAR, RANA and KUSHWAHA, AVINASH and GILL, NAVJOT SINGH},
  year={2025}
}
```

---

## 🔖 [License](LICENSE)

This repository is licensed under the **Creative Commons Attribution 4.0 International (CC BY 4.0)** license.

> Full license details: [https://creativecommons.org/licenses/by/4.0/](https://creativecommons.org/licenses/by/4.0/)

---

## ✨ Contributors

<div align="center">
  <a href="https://github.com/Arunim-Gogoi">
    <img src="./Assets/Arunim_Gogoi.png" alt="Arunim Gogoi" style="border-radius: 50%; margin: 5px; width: 100px; height: 100px;">
  </a>
  <a href="https://github.com/AvinashK47">
    <img src="./Assets/Avinash_Kushwaha.png" alt="Avinash Kushwaha" style="border-radius: 50%; margin: 5px; width: 100px; height: 100px;">
  </a>
  <a href="https://github.com/NAVJOT2005">
    <img src="./Assets/Navjot_Singh_Gill.png" alt="Navjot Singh Gill" style="border-radius: 50%; margin: 5px; width: 100px; height: 100px;">
  </a>
  <a href="https://github.com/Jyotibrat">
    <img src="./Assets/Bindupautra_Jyotibrat.png" alt="Bindupautra Jyotibrat" style="border-radius: 50%; margin: 5px; width: 100px; height: 100px;">
  </a>
  <a href="https://github.com/Auth0r-C0dez">
    <img src="./Assets/Rana_Talukdar.png" alt="Rana Talukdar" style="border-radius: 50%; margin: 5px; width: 100px; height: 100px;">
  </a>
</div>

---

## 🙏 Acknowledgements

Special thanks to:

* The authors of the [**ROBIN dataset**](https://github.com/gesstalt/ROBIN).
* Developers and maintainers of **Stable Diffusion**, **Hugging Face**, **PyTorch**, and the open-source ML community

---

### 💬 For questions, feedback, or collaboration, feel free to open an issue or [contact us](mailto:bjyotibrat@gmail.com)!