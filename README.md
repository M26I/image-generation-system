# 🧠 AI Image Generation CLI

A command-line tool for generating high-quality images from text prompts using Stable Diffusion v1.5. Built for speed, simplicity, and portfolio-ready presentation. Images are saved locally with timestamped filenames for easy tracking.

---

## ✨ Features

- 🎨 Text-to-image generation via Stable Diffusion v1.5
- 🖥️ CLI-based interface for fast experimentation
- 🧠 Uses Hugging Face `diffusers` and `safetensors`
- 🧊 Local model caching to avoid repeated downloads
- 🕓 Outputs are timestamped and saved in `outputs/`

---

## 🖼️ Example Usage

```bash
$ python generate.py
Enter your prompt: a futuristic city skyline at sunset
Image saved to outputs/generated_20250520_142301.png

```
---
## 📁 Project Structure
.
├── generate.py          # Main script to run image generation
├── model_cache/         # Local model cache (automatically created)
├── outputs/             # Folder for generated images
├── models/              # Folder for safetensor model files
├── requirements.txt     # Dependencies
└── README.md            # Project documentation

---
## ⚙️ Installation & Setup
1. Clone the Repository
```bash
git clone https://github.com/M26I/image-generation-system
cd image-generation-system

```

2. Set Up Virtual Environment (Recommended)
```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate


```

3. Install Requirements

```bash
pip install -r requirements.txt

```

4. Run the CLI
```bash
python generate.py

```

---

## ⚡ Optional: Speed Boost with GPU (If Available)
If you have an NVIDIA GPU and want faster image generation:

- Install PyTorch with CUDA support: https://pytorch.org/get-started/locally/

- Install accelerate:

```bash
pip install accelerate

```
- You can then modify .to("cpu") → .to("cuda") in generate.py

---

## ✅ Requirements

- Python 3.8+

- torch, diffusers, safetensors

- Optional: accelerate (for improved performance)
---

## 📌 Notes
- Model weights are cached in ./model_cache to reduce startup time.

- Generated images are saved with filenames like generated_20250520_142301.png in the outputs/ folder.

- No image is overwritten thanks to unique timestamping.

---

## 👤 Author
[M26I](https://github.com/M26I)