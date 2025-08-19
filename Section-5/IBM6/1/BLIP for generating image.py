# First, install the necessary libraries
!pip install transformers Pillow torch torchvision torchaudio

from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import requests

# --- Image Captioning Section ---

# Load the processor and model (base version)
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

# Open an image from your local path
image = Image.open("path_to_your_image.jpg")

# Convert image into model-compatible format
inputs = processor(image, return_tensors="pt")

# Generate captions
output_ids = model.generate(**inputs)
caption_text = processor.decode(output_ids[0], skip_special_tokens=True)

print("Generated Caption:", caption_text)


# --- Visual Question Answering (VQA) Section ---

# Load a larger BLIP model for better VQA performance
processor_vqa = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-large")
model_vqa = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-large")

# Fetch an image from a URL
img_url = "https://storage.googleapis.com/sfr-vision-language-research/BLIP/demo.jpg"
raw_image = Image.open(requests.get(img_url, stream=True).raw).convert("RGB")

# Define a question about the image
question = "What is in the image?"

# Prepare the image and question together
vqa_inputs = processor_vqa(raw_image, question, return_tensors="pt")

# Generate the answer
vqa_output_ids = model_vqa.generate(**vqa_inputs)
answer_text = processor_vqa.decode(vqa_output_ids[0], skip_special_tokens=True)

print(f"Answer: {answer_text}")
