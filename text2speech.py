from google.cloud import texttospeech

client = texttospeech.TextToSpeechClient()
RESPONSE_INPUT_FILENAME = "response.txt"


def synthesize_text(text):
    input_text = texttospeech.SynthesisInput(text=text)
    voice = texttospeech.VoiceSelectionParams(
        language_code="lt-LT",
        ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL,
    )
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )

    response = client.synthesize_speech(
        input=input_text, voice=voice, audio_config=audio_config
    )

    with open("output.mp3", "wb") as out:
        out.write(response.audio_content)
        print('Audio content written to file "output.mp3"')


if __name__ == '__main__':
    # Read the response from the file
    with open(RESPONSE_INPUT_FILENAME, "r", encoding="utf-8") as in_file:
        response_text = in_file.read()

    # Synthesize the response text to speech
    synthesize_text(response_text)
