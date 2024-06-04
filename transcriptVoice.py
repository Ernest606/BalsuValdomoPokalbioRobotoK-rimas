from google.cloud import speech_v1p1beta1 as speech
import requests
import json
import base64


API_KEY = '*************************'
WAVE_OUTPUT_FILENAME = "input.wav"
TRANSCRIPTION_OUTPUT_FILENAME = "transcription.txt"
client = speech.SpeechClient()


def transcribe_speech(audio_file):
    with open(audio_file, "rb") as f:
        audio_content = f.read()

    audio_content_base64 = base64.b64encode(audio_content).decode('utf-8')

    audio = {
        "content": audio_content_base64
    }

    config = {
        "encoding": "LINEAR16",
        "sample_rate_hertz": 16000,
        "language_code": "lt-LT",
    }

    data = {
        "config": config,
        "audio": audio
    }

    headers = {
        "Content-Type": "application/json"
    }

    url = f"https://speech.googleapis.com/v1/speech:recognize?key={API_KEY}"

    response = requests.post(url, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        result = response.json()
        if "results" in result:
            transcript = result["results"][0]["alternatives"][0]["transcript"]
            print(f"Transcript: {transcript}")
            # Save the transcription to a file
            with open(TRANSCRIPTION_OUTPUT_FILENAME, "w", encoding="utf-8") as out_file:
                out_file.write(transcript)
        else:
            print("No results found")
    else:
        print(f"Error: {response.status_code}, {response.text}")


if __name__ == "__main__":
    transcribe_speech(WAVE_OUTPUT_FILENAME)
