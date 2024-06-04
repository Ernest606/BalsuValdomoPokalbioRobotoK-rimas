import tkinter as tk
from tkinter import messagebox
import subprocess
import sys
import os

venv_python = os.path.join(os.path.dirname(sys.executable), 'python.exe')


def ask_question():
    try:
        # Call recordVoice.py to record the voice
        subprocess.run([venv_python, "recordVoice.py"], check=True)
        # Call transcriptVoice.py to transcribe the audio
        subprocess.run([venv_python, "transcriptVoice.py"], check=True)
        # Call dialogflowReq.py to send text to Dialogflow CX and get the response
        subprocess.run([venv_python, "dialogflowReq.py"], check=True)
        # Call text2speech.py to convert the response to speech
        subprocess.run([venv_python, "text2speech.py"], check=True)
        # Play the audio response
        subprocess.run(["start", "output.mp3"], shell=True)
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"An error occurred: {e}")


# Create the main window
root = tk.Tk()
root.title("Dialogflow Voice Interaction")

# Create and place the button
button = tk.Button(root, text="Užduoti klausimą",
                   command=ask_question, padx=20, pady=10)
button.pack(pady=20)

# Run the GUI event loop
root.mainloop()
