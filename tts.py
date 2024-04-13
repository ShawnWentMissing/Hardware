from gtts import gTTS
import os

def text_to_speech(text, language='en', filename='output2.mp3'):
    """
    Convert text to speech and save it as an MP3 file.
    
    Args:
        text (str): The text to be converted to speech.
        language (str, optional): The language code (default is 'en' for English).
        filename (str, optional): The filename for the output MP3 file (default is 'output.mp3').
    """
    tts = gTTS(text=text, lang=language, slow=False)
    tts.save(filename)
    print(f"Saved TTS as '{filename}'")

if __name__ == "__main__":
    input_text = input("Enter the text to convert to speech: ")
    text_to_speech(input_text)