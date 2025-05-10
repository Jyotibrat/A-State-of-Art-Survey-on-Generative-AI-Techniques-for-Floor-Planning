# 🏗️ Prototype 1 – Text-to-Floorplan (Stable Diffusion)

This prototype demonstrates the ability to **generate architectural floor plan images from natural language prompts** using a Stable Diffusion model.

It forms the first practical implementation based on the survey paper titled  
***"A State-of-Art Survey on Generative AI Techniques for Floor Planning."***

---

## 🎯 Objective

To convert simple textual descriptions into synthetic floor plan images using a pre-trained **Stable Diffusion 2.0** model, guided by prompt engineering and configuration control.

---

## ⚙️ Tech Stack

- 🧠 `diffusers` (Stable Diffusion v2 from Hugging Face)
- 📝 `transformers` (for future text preprocessing if needed)
- 🧪 Python & PyTorch
- 🎨 `matplotlib`, `PIL`, `cv2` (for image rendering and display)

---

## 🚀 How It Works

1. **Prompt Input**: A textual prompt (e.g., *"Generate an image of a floor plan of a house."*) is provided.
2. **Diffusion Model**: The prompt is passed to a pre-trained Stable Diffusion v2 model.
3. **Image Generation**: The model generates a synthetic image conditioned on the prompt.
4. **Post-processing**: The output image is resized to (400x400) and saved.

---

## 🧪 Sample Prompt

```python
"Generate an image of a floor plan of a house."
```

---

## 📥 Setup Instructions

1. **Install Dependencies**
   You can run this directly in a Google Colab environment:

   ```python
   !pip install --upgrade diffusers transformers -q
   ```

2. **Authentication Required**
   To use Stable Diffusion, you'll need a Hugging Face API token:

   * Sign up at: [https://huggingface.co](https://huggingface.co)
   * Accept the terms for the model [here](https://huggingface.co/stabilityai/stable-diffusion-2)
   * Replace `'api_token'` in the code with your token.

3. **Run the Notebook**

---

## 📸 Output

* The generated image is saved as:

  ```
  floor_plan_output.png
  ```
* It is also displayed using `matplotlib`.

---

## 📌 Notes

* GPU (`cuda`) is required for faster inference.
* The code is easily extensible to support prompt templates, batch generation, or architectural control tokens.

---