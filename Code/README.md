# 🧠 Code

This directory contains all the source code developed as part of the survey project titled ***"A State-of-the-Art Survey on Generative AI Techniques for Floor Planning."*** The codebase is organized into two subdirectories:

- **Data Augmentation Code**: Scripts used to *increase the size* and variability of the *dataset*.
- **Main Source Code**: Core *model and implementations* used to train and evaluate *floor planning model*.

---

## 🌿 Directory Structure

```
Code/
├──Data Augmentation Code/
│  ├──Image_Augmentation.ipynb
│  └──README.md
│
├──Main Source Code/
│  ├──Floor Planning GEN AI.ipynb
│  └──README.md
│
└──README.md
```

---

## 📁 Data Augmentation Code

This subdirectory contains a Jupyter Notebook (`.ipynb`) that is used to perform data augmentation on the floor plan images.

### 📌 Instructions to Run:

**1.** Open the `Image_Augmentation.ipynb` file in **Google Colab**.

**2.** **Mount Google Drive** by running the appropriate Colab cell.

**3.** Upload the **original dataset** to your Google Drive.

**4.** Ensure that at least **5GB of free space** is available in your Drive.

**5.** Run all cells in the notebook.

**6.** The **augmented dataset** will be automatically saved back to your Drive.

This helps increase the robustness of our dataset by synthetically generating new floor plan samples.

---

## 📁 Main Source Code

This subdirectory contains the core model implementation notebook that trains and evaluates the generative AI model for floor planning.

### 📌 Instructions to Run:

**1.** Open the `Floor Planning GEN AI.ipynb` file in **Google Colab**.

**2.** Mount your **Google Drive** where the dataset is located.

**3.** Run all cells to begin **training** the model on the dataset.

**4.** After training completes, the model can **generate floor plan images** based on user-defined prompts.

This is the main model developed for the project, showcasing the effectiveness of generative AI in the context of architectural design and floor plan synthesis.

---

## For any issues or questions, feel free to open an [issue](https://github.com/Jyotibrat/Floor-Planning-Generative-AI/issues) in the repository.