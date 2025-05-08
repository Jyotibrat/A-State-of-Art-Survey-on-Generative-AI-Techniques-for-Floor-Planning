# 🏗️ Prototype 2 – Text-to-Floorplan (Standalone Script)

This prototype builds on the first implementation and introduces a **modular, script-based approach** to generate architectural floor plans from natural language prompts using **Stable Diffusion v2**.

This version is designed to be **standalone** and **production-ready**, capable of being run as a Python script (`.py`) instead of a notebook.

---

## 🎯 Objective

To allow flexible and reproducible generation of synthetic floor plan images from prompts like  
> *"Generate an image of a floor plan of a building"*

---

## ⚙️ Tech Stack

- `diffusers` (Stable Diffusion 2.0 from Hugging Face)
- `transformers` (for future prompt enhancements)
- `torch` (for GPU/CPU acceleration)
- `matplotlib`, `cv2`, `PIL` (for image visualization and processing)

---

## 🚀 How to Run

1. **Install Dependencies**
   ```bash
   pip install diffusers transformers torch matplotlib opencv-python
   ```

2. **Authenticate with Hugging Face**

   * Create an account at: [https://huggingface.co](https://huggingface.co)
   * Accept the license for the [Stable Diffusion model](https://huggingface.co/stabilityai/stable-diffusion-2)
   * Replace `'api_token'` in the script with your actual Hugging Face token.

3. **Run the Script**

   ```bash
   python Second_Prototype.py
   ```

4. **Output**

   * The image will be saved as `generated_output.png`
   * It will also be displayed using `matplotlib`

---

## 📌 Highlights

* Uses `Config` class for centralized hyperparameter and hardware control.
* Can easily be extended for:

  * Batch generation
  * Command-line prompt input
  * Integration into a web API

---