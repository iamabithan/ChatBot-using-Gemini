import os
import google.generativeai as genai
from google.cloud import vision
from google.cloud.vision_v1 import types

# Configure Gemini API
genai.configure(api_key="AIzaSyDBuv7rHsjlMlWlATqpNoruBB_W3Qb9f6c")

# Initialize the Vision API client
vision_client = vision.ImageAnnotatorClient()

def analyze_image(image_path):
    with open(image_path, 'rb') as image_file:
        content = image_file.read()

    image = types.Image(content=content)
    response = vision_client.label_detection(image=image)
    labels = response.label_annotations

    return [label.description for label in labels]

def generate_response(image_path, prompt):
    labels = analyze_image(image_path)
    image_description = ', '.join(labels)
    
    full_prompt = f"{prompt}. The image contains: {image_description}"

    # Generate response using Gemini model
    response = model.generate(prompt=full_prompt)
    return response.text

# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
)

# Example usage
image_path = "image1.jpg"
prompt = "Describe the scene"
response_text = generate_response(image_path, prompt)
print(response_text)
