import torch
import librosa
from transformers import WhisperProcessor, WhisperForConditionalGeneration

# Load processor (tokenizer + feature extractor)
processor = WhisperProcessor.from_pretrained("openai/whisper-tiny.en")

# Load model
model = WhisperForConditionalGeneration.from_pretrained("openai/whisper-tiny.en")

# Step 1: Load the audio
# (librosa converts mp3 → float32 numpy array, 16kHz sample rate)
audio, sr = librosa.load("downloaded_audio.mp3", sr=16000)

# Step 2: Preprocess audio (convert waveform into model input features)
input_features = processor(audio, sampling_rate=16000, return_tensors="pt").input_features

# Step 3: Run the model (get predicted tokens)
predicted_ids = model.generate(input_features)

# Step 4: Decode tokens into text
transcription = processor.batch_decode(predicted_ids, skip_special_tokens=True)[0]

print(transcription)

# -----------------------------------------------------------------------------
# with pipeline we do 
from transformers import pipeline

pipe = pipeline(
    "automatic-speech-recognition",
    model="openai/whisper-tiny.en",
    chunk_length_s=30,
)
prediction = pipe("downloaded_audio.mp3", batch_size=8)["text"]
print(prediction)
