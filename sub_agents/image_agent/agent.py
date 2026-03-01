import os
import requests
from google.adk.agents.llm_agent import Agent


def generate_image_with_stability(prompt: str, output_format: str = "jpeg") -> str:
    """
    Generate an image using Stability.ai API.
    
    Args:
        prompt: The text description of the image to generate
        output_format: Output format (jpeg, png, or webp). Default is jpeg.
    
    Returns:
        str: Path to the saved image file
    """
    api_key = os.getenv('STABILITY_API_KEY')
    
    response = requests.post(
        "https://api.stability.ai/v2beta/stable-image/generate/sd3",
        headers={
            "authorization": f"Bearer {api_key}",
            "accept": "image/*"
        },
        files={"none": ''},
        data={
            "prompt": prompt,
            "output_format": output_format,
            "model" : "sd3.5-flash"
        },
    )
    
    if response.status_code == 200:
        # Create output directory if it doesn't exist
        os.makedirs("generated_images", exist_ok=True)
        
        # Generate filename from prompt (sanitized)
        filename = "".join(c if c.isalnum() or c in (' ', '-', '_') else '_' for c in prompt[:50])
        filepath = f"./generated_images/{filename}.{output_format}"
        
        with open(filepath, 'wb') as file:
            file.write(response.content)
        
        return f"Image successfully generated and saved to: {filepath}"
    else:
        raise Exception(f"Image generation failed: {response.json()}")


image_agent = Agent(
    model='gemini-2.5-flash',
    name='ImageAgent',
    description='An agent that generates images using Stability.ai SD3 model.',
    instruction="You are an Image Agent. When users request image generation, use the generate_image_with_stability tool to create images based on their descriptions. Always extract the key visual details from the user's request to create a detailed prompt.",
    tools=[generate_image_with_stability]
)
