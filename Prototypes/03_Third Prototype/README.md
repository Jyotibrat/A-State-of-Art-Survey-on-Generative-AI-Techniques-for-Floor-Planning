# 🏗️ Prototype 3 – Text-to-Floorplan (Secure Token-Based Generation)

This prototype demonstrates the generation of architectural floor plans from textual prompts using **Stable Diffusion 2.0** with a focus on **secure Hugging Face token handling** via `google.colab.userdata`.

It is functionally similar to Prototype 1 but enhanced for **secure execution in Google Colab environments**, where the token is not hardcoded.

---

## 🎯 Objective

To safely generate synthetic floor plan images using Stable Diffusion while protecting authentication credentials.

---

## ⚙️ Tech Stack

- `diffusers` (Stable Diffusion 2.0)
- `transformers` (for zero-shot classification if extended)
- `google.colab.userdata` (for secure token access)
- `torch`, `matplotlib`, `PIL`

---

## 🚀 How It Works

1. **Prompt Input**: A string like `"Generate an image of a floor plan of a house."`
2. **Model Initialization**: 
   - Uses `StableDiffusionPipeline` from Hugging Face.
   - Access token is fetched securely using:
     ```python
     from google.colab import userdata
     token = userdata.get('HGF_auth_token')
     ```
3. **Image Generation**:
   - Diffusion model processes the prompt.
   - Result is resized to (400x400) and displayed.

---

## 🧪 Sample Prompt

```python
"Generate an image of a floor plan of a house."
```

---

## 📥 Setup Instructions (in Google Colab)

1. **Install Dependencies**:

   ```python
   !pip install --upgrade diffusers transformers
   ```

2. **Store Hugging Face Token Securely**:

   ```python
   from google.colab import userdata
   token = userdata.get('HGF_auth_token')  # Stored in Colab session
   ```

3. **Run the Notebook**: All images will be generated and displayed inline.

---

## 🔐 Highlights

* ✅ Uses `userdata.get()` for secure token usage
* ✅ GPU (`cuda`) enabled for fast inference
* ✅ Image output is saved locally (`floor_plan_output.png`)

---

### This prototype is ideal for Colab environments where **sensitive information must be kept secure** during public or collaborative sessions.