#!/path/to/your/venv/bin/python  # or venv\Scripts\python.exe on Windows

import os
from google.oauth2 import service_account
from google.cloud import dialogflowcx_v3beta1 as dialogflowcx
from google.cloud import translate_v2 as translate

# Path to your service account key file
SERVICE_ACCOUNT_FILE = '****************************'
PROJECT_ID = '********************'
LOCATION = 'europe-west3'  # Specify your region
AGENT_ID = '**********************'
SESSION_ID = '8'  # Unique identifier for the session
LANGUAGE_CODE = 'lt'  # Lithuanian language code
TRANSCRIPTION_INPUT_FILENAME = "transcription.txt"
RESPONSE_OUTPUT_FILENAME = "response.txt"

# Load the service account credentials
credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=[
        'https://www.googleapis.com/auth/cloud-platform']
)

# Initialize the Translation client
translate_client = translate.Client(credentials=credentials)


def translate_text(text, target_language):
    result = translate_client.translate(text, target_language=target_language)
    return result['translatedText']


def detect_intent_texts(credentials, project_id, location, agent_id, session_id, texts, language_code):
    client_options = {"api_endpoint": f"{location}-dialogflow.googleapis.com"}
    client = dialogflowcx.SessionsClient(
        credentials=credentials, client_options=client_options)
    session_path = f"projects/{project_id}/locations/{location}/agents/{agent_id}/sessions/{session_id}"

    for text in texts:
        # Translate text from Lithuanian to English
        translated_text = translate_text(text, target_language='en')

        query_input = dialogflowcx.QueryInput(
            text=dialogflowcx.TextInput(text=translated_text),
            language_code='en',
        )

        response = client.detect_intent(
            request={"session": session_path, "query_input": query_input}
        )

        for message in response.query_result.response_messages:
            if message.text:
                # Translate response text from English to Lithuanian
                translated_response = translate_text(
                    message.text.text[0], target_language='lt')
                print('=' * 20)
                print('Original query text:', text)
                print('Translated query text:', translated_text)
                print('Detected intent:',
                      response.query_result.match.intent.display_name)
                print('Confidence:', response.query_result.match.confidence)
                print('Response text:', translated_response)
                # Save the response to a file
                with open(RESPONSE_OUTPUT_FILENAME, "w", encoding="utf-8") as out_file:
                    out_file.write(translated_response)


if __name__ == '__main__':
    # Read the transcription from the file
    with open(TRANSCRIPTION_INPUT_FILENAME, "r", encoding="utf-8") as in_file:
        transcription = in_file.read()

    # Pass the transcription to detect_intent_texts
    detect_intent_texts(credentials, PROJECT_ID, LOCATION,
                        AGENT_ID, SESSION_ID, [transcription], LANGUAGE_CODE)
