import torch
from diffusers import StableDiffusionPipeline
from pathlib import Path

# Define model path
model_path = "./models/v1-5-pruned-emaonly.safetensors"

# Load the model
pipe = StableDiffusionPipeline.from_single_file(
    model_path,
    torch_dtype=torch.float16,
    use_safetensors=True,
    safety_checker=None,
    requires_safety_checker=False,
)
# Load once and reuse cached files
pipe = StableDiffusionPipeline.from_pretrained(
    "runwayml/stable-diffusion-v1-5", 
    cache_dir="./model_cache"
).to("cpu")


# Prompt for image generation
prompt = input("Enter your prompt: ")

# Generate image
image = pipe(prompt).images[0]

# Save the image
output_dir = Path("outputs")
output_dir.mkdir(exist_ok=True)
image_path = output_dir / "generated_image.png"
image.save(image_path)

print(f" Image saved to {image_path}")
