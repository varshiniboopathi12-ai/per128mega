from diffusers import StableDiffusionPipeline
import torch
import os


# Load Stable Diffusion model
pipe = StableDiffusionPipeline.from_pretrained(
    "runwayml/stable-diffusion-v1-5"
)


# Use GPU if available, otherwise CPU
device = "cuda" if torch.cuda.is_available() else "cpu"

pipe = pipe.to(device)


def generate_image(prompt, panel_number):

    # Generate image
    image = pipe(prompt).images[0]

    # Create panels folder
    os.makedirs(
        "static/panels",
        exist_ok=True
    )

    # Image file path
    filepath = f"static/panels/panel_{panel_number}.png"

    # Save image
    image.save(filepath)

    return filepath