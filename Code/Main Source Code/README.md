# 🧠 Main Source Code

This directory contains the **core implementation** of our project titled ***"A State-of-Art Survey on Generative AI Techniques for Floor Planning"***. The provided code enables training and generation of architectural floor plans from natural language prompts using deep learning models.

---

## 📁 Directory Contents

```
Main Source Code/
├── Floor Planning GEN AI.ipynb
├── floor_planning_gen_ai.py
├── requirements.txt
└── README.md
```

---

## 📌 Description

This is the **main model** that we developed for generating floor plans from text prompts. It includes both the Colab notebook (`.ipynb`) for easy cloud execution and a `.py` script for local or production-level integration.

---

## 🚀 How to Use

### Option 1: Run on Google Colab (Recommended)

1. **Upload Dataset to Google Drive**

   * Make sure the dataset is uploaded to your Google Drive.
   * The dataset should be organized in the expected format used in training.

2. **Open `Floor Planning GEN AI.ipynb` in Google Colab**

3. **Mount Google Drive**

   ```python
   from google.colab import drive
   drive.mount('/content/drive')
   ```

4. **Run the Notebook**

   * The notebook contains sections for:

     * Dataset loading
     * Preprocessing
     * Model training
     * Prompt-based floor plan generation

5. **Generated Output**

   * The model will produce floor plan images based on the text prompt you provide.
   * All output will be saved automatically to your Google Drive.

---

### Option 2: Run Locally (Advanced)

1. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

2. **Ensure Dataset Path is Correct**

   * Modify the dataset path in the script to point to your local copy.

3. **Run Script**

   ```bash
   python3 "floor_planning_gen_ai.py"
   ```

---

## ⚠️ Notes

* Your Google Drive should have **at least 5GB** of free space to store model outputs and generated images.
* For best performance, use GPU-enabled runtime in Colab.