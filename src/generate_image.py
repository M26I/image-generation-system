import io
import os
from dotenv import load_dotenv
from stability_sdk import client
import stability_sdk.interfaces.gooseai.generation.generation_pb2 as generation
from PIL import Image

# Load environment variables from .env
load_dotenv()

STABILITY_API_KEY = os.getenv("STABILITY_API_KEY")

if not STABILITY_API_KEY:
    raise ValueError("Missing Stability API key! Please set STABILITY_API_KEY in your environment.")

def generate_image(prompt: str, output_path: str):
    stability_api = client.StabilityInference(
        key=STABILITY_API_KEY,
        verbose=True,
        engine="stable-diffusion-512-v2-1",

    )

    answers = stability_api.generate(
        prompt=prompt,
        seed=42,
        steps=30,
        cfg_scale=7.0,
        width=512,
        height=512,
        samples=1,
        sampler=generation.SAMPLER_K_DPMPP_2M
    )

    for resp in answers:
        for artifact in resp.artifacts:
            if artifact.type == generation.ARTIFACT_IMAGE:
                img = Image.open(io.BytesIO(artifact.binary))
                img.save(output_path)
                print(f"Image saved to {output_path}")

if __name__ == "__main__":
    prompt_text = "A futuristic city skyline at sunset, digital art"
    generate_image(prompt_text, "../outputs/generated_image.png")
