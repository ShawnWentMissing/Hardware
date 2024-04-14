# from gtts import gTTS
from pygame import mixer
import os
from openai import OpenAI
mixer.init()
client = OpenAI( api_key="")
def text_to_speech(text, language='en', filename='output2.mp3'):
    """
    Convert text to speech and save it as an MP3 file.
    
    Args:
        text (str): The text to be converted to speech.
        language (str, optional): The language code (default is 'en' for English).
        filename (str, optional): The filename for the output MP3 file (default is 'output.mp3').
    """
    # tts = gTTS(text=text, lang=language, slow=False)
    response = client.audio.speech.create(
        model="tts-1",
        voice="alloy",
        input=text
        )

    response.stream_to_file(filename)
    # print(f"Saved TTS as '{filename}'")


def play_audio(filename='output2.mp3'):
    """
    Play the audio file.
    
    Args:
        filename (str, optional): The filename of the audio file to play (default is 'output.mp3').
    """
    mixer.music.load(filename)
    mixer.music.play()
    while mixer.music.get_busy():
        pass


def play_score(player1,player2, handout = False):
    text = f"{player1} {player2}"
    if handout:
        text += " Handout"
    text_to_speech(text)
    play_audio()

if __name__ == "__main__":
    play_score(5, 3, True)