# --- Step 1: Install required packages ---
# pip install gradio transformers torch torchvision Pillow

import gradio as gr
from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import torch
from torchvision import transforms
import requests

# -------------------------------
# Section 1: Simple Greeting Demo
# -------------------------------
def greet_user(name, intensity):
    """
    Returns a fun greeting repeated 'intensity' times.
    """
    return "Hello, " + name + "!" * int(intensity)

greet_demo = gr.Interface(
    fn=greet_user,
    inputs=["text", "slider"],
    outputs="text",
    title="Fun Greeting App",
    description="Type your name and choose the intensity of the greeting."
)

# Launch the greeting interface (local server)
greet_demo.launch(server_name="127.0.0.1", server_port=7860)


# --------------------------------------
# Section 2: Image Captioning with BLIP
# --------------------------------------
# Load BLIP processor and model
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
blip_model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

def generate_caption(image):
    """
    Takes a PIL Image and generates a caption using BLIP.
    """
    inputs = processor(images=image, return_tensors="pt")
    outputs = blip_model.generate(**inputs)
    caption_text = processor.decode(outputs[0], skip_special_tokens=True)
    return caption_text

# Gradio interface for image captioning
caption_demo = gr.Interface(
    fn=generate_caption,
    inputs=gr.Image(type="pil"),
    outputs="text",
    title="Image Captioning with BLIP",
    description="Upload an image and get an AI-generated caption."
)

caption_demo.launch(server_name="127.0.0.1", server_port=7860)


# -----------------------------------------
# Section 3: Image Classification with ResNet
# -----------------------------------------
# Load pretrained ResNet-18 model
resnet_model = torch.hub.load('pytorch/vision:v0.6.0', 'resnet18', pretrained=True).eval()

# Load human-readable ImageNet labels
imagenet_labels_url = "https://git.io/JJkYN"
response = requests.get(imagenet_labels_url)
imagenet_labels = response.text.split("\n")

def classify_image(image):
    """
    Classifies a PIL Image using pretrained ResNet-18 and returns top 3 predictions.
    """
    image_tensor = transforms.ToTensor()(image).unsqueeze(0)
    with torch.no_grad():
        logits = resnet_model(image_tensor)[0]
        probs = torch.nn.functional.softmax(logits, dim=0)
    
    confidences = {imagenet_labels[i]: float(probs[i]) for i in range(len(imagenet_labels))}
    return confidences

# Gradio interface for image classification
classification_demo = gr.Interface(
    fn=classify_image,
    inputs=gr.Image(type="pil"),
    outputs=gr.Label(num_top_classes=3),
    title="Image Classification with ResNet-18",
    description="Upload an image to see the top predicted classes."
)

classification_demo.launch()
