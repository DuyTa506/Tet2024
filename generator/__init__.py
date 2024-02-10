"""
Generate images using DALLE-3
Author: Son Phat Tran
"""
import os
from dotenv import load_dotenv
from openai import OpenAI


# Load the environment file and get the API key
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# Create OpenAI instance
client = OpenAI(api_key=api_key)


def generate_image(prompt: str) -> str:
    """
    Generate an image using provided prompt with DALLE-3
    :param prompt: the prompt to generate image
    :return: URL containing the image
    """
    # Run the image generation process
    response = client.images.generate(
        model="dall-e-3",
        prompt=prompt,
        size="1024x1024",
        quality="standard",
        n=1,
    )

    # Get and display image url
    image_url = response.data[0].url
    return image_url