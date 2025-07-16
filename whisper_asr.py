import shutil
from fastapi import UploadFile
import re

# This is a MOCKED voice-to-text function.
# It simulates transcription to allow the app to run without a real ASR setup.
def mock_transcribe_audio(file: UploadFile):
    """
    Mocks the transcription of an audio file based on its filename.
    This allows for predictable demo behavior.
    """
    # Save the uploaded file temporarily to inspect it (optional)
    # with open(f"temp_{file.filename}", "wb") as buffer:
    #     shutil.copyfileobj(file.file, buffer)

    # In a real scenario, you'd use a library like OpenAI's Whisper here.
    # For the demo, we just return a pre-defined string.
    # This simulates the user saying: "Mirch powder, one kilo, one hundred rupees" in Hindi.
    mocked_hindi_transcription = "मिर्च पाउडर, एक किलो, सौ रुपये"
    
    print(f"🎤 Mock ASR: Simulating transcription for '{file.filename}'. Returning: '{mocked_hindi_transcription}'")
    
    return mocked_hindi_transcription

# --- REAL WHISPER IMPLEMENTATION (for reference) ---
# To use this, you need to `pip install openai-whisper` and have `ffmpeg` installed.

# import whisper

# model = None

# def load_whisper_model():
#     global model
#     if model is None:
#         print("Loading Whisper ASR model...")
#         # Using the "tiny" model for speed. "base" is a good compromise.
#         model = whisper.load_model("tiny")
#         print("Whisper model loaded.")

# def transcribe_audio_real(file: UploadFile):
#     """
#     Transcribes an audio file using OpenAI's Whisper model.
#     """
#     if model is None:
#         load_whisper_model()
        
#     # Save the uploaded file to a temporary path to be read by Whisper
#     temp_file_path = f"/tmp/{file.filename}"
#     with open(temp_file_path, "wb") as buffer:
#         shutil.copyfileobj(file.file, buffer)

#     print(f"Transcribing audio file: {temp_file_path}")
#     result = model.transcribe(temp_file_path, fp16=False) # fp16=False for CPU
#     print(f"Transcription result: {result['text']}")

#     return result['text']


def parse_transcription(text: str):
    """
    Parses transcribed text to extract product name, quantity, and price.
    This is a simplified parser and can be enhanced with more robust NLP techniques.
    """
    # A simple regex to find numbers.
    numbers = re.findall(r'\d+', text)
    price = numbers[-1] if numbers else "0"
    
    # Very basic parsing logic, can be improved.
    # Assumes a structure like "NAME, QUANTITY, PRICE"
    parts = re.split(r'[,\s]+', text)
    
    # A list of common quantity words in different languages
    quantity_keywords = ['kg', 'kilo', 'gram', 'piece', 'liter', 'dozen', 'किलो', 'ग्राम', 'लीटर', 'दर्जन', 'పీస్', 'కిలో', 'లీటరు', 'పీస్', 'కేజీ', 'లీటర్', 'পিস', 'কেজি', 'লিটার']

    product_name = []
    quantity_unit = ""

    # This is a very naive parser. A real-world app would use a more sophisticated NLP model.
    try:
        # A simple keyword-based approach
        for part in parts:
            if part.isdigit() or part in numbers:
                continue
            if part.lower() in quantity_keywords:
                quantity_unit += part + " "
            else:
                product_name.append(part)
    except Exception:
        # If parsing fails, just use the whole text as the name
        return {"name": text, "quantity": "1 unit", "price": "0"}

    return {
        "name": " ".join(product_name).strip(),
        "quantity": ("1 " + quantity_unit).strip(),
        "price": price
    }