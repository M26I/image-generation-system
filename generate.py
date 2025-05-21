# © 2025 M26I - For educational/portfolio use only

import torch
from diffusers import StableDiffusionPipeline
from pathlib import Path
from PIL import Image
import sys
from datetime import datetime


# Check device
device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Using device: {device}")

# Define model cache directory (kept out of Git if possible)
cache_dir = "./model_cache"

# Load model
pipe = StableDiffusionPipeline.from_pretrained(
    "runwayml/stable-diffusion-v1-5",
    cache_dir=cache_dir,
    torch_dtype=torch.float16 if device == "cuda" else torch.float32,
    safety_checker=None,
    requires_safety_checker=False,
)
pipe.to(device)

# Prompt from CLI
prompt = input("Enter your prompt: ")

# Generate image
print("Generating image...")
image = pipe(prompt).images[0]

# Save image
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

output_dir = Path("outputs")
output_dir.mkdir(exist_ok=True)
short_prompt = "_".join(prompt.lower().split()[:4])[:30]
image_path = output_dir / f"{short_prompt}_{timestamp}.png"

image.save(image_path)

# Show image
image.show()

print(f"Image saved to {image_path}")
