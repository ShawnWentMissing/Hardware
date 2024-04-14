# from gtts import gTTS
import asyncio

import websockets
from openai import OpenAI
from pygame import mixer

mixer.init()
client = OpenAI(api_key="")


def text_to_speech(text, language="en", filename="output2.mp3"):
    """
    Convert text to speech and save it as an MP3 file.

    Args:
        text (str): The text to be converted to speech.
        language (str, optional): The language code (default is 'en' for English).
        filename (str, optional): The filename for the output MP3 file (default is 'output.mp3').
    """
    # tts = gTTS(text=text, lang=language, slow=False)
    response = client.audio.speech.create(model="tts-1", voice="alloy", input=text)

    response.stream_to_file(filename)
    # print(f"Saved TTS as '{filename}'")


def play_audio(filename="output2.mp3"):
    """
    Play the audio file.

    Args:
        filename (str, optional): The filename of the audio file to play (default is 'output.mp3').
    """
    mixer.music.load(filename)
    mixer.music.play()
    while mixer.music.get_busy():
        pass


def play_score(player1, player2, handout=False):
    text = f"{player1} {player2}"
    if handout:
        text += " Handout"
    text_to_speech(text)
    play_audio()


async def receive_data():
    uri = "ws://localhost:8080/ws"
    async with websockets.connect(uri) as websocket:
        try:
            while True:
                data = await websocket.recv()
                print("Received:", data)
        except websockets.exceptions.ConnectionClosed:
            print("WebSocket connection closed")


asyncio.run(receive_data())
