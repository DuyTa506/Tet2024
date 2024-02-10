"""
Generate images using DALL-E-3
Author: Duy Khanh Ta
"""
from generator import generate_image
from fileio import download_image
import os

PROMPTS = [
    "Chúc mừng năm mới 2024, thắng lợi mới nhé !"
]

ROOT = os.path.dirname(os.path.abspath(__file__))
DIRECTORY = os.path.join(ROOT, "images")


if __name__ == "__main__":
    for prompt in PROMPTS:
        url = generate_image(prompt)
        download_image(url, save_path=os.path.join(DIRECTORY, f"{prompt}.png"))
