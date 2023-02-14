import io
import os

# Google Cloud API client library
from google.cloud import speech

import env

# API Key
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = env.google_application_credentials

# Instantiates a client
client = speech.SpeechClient()

# The audio file to transcribe
file_name = os.path.join(
    os.path.dirname(__file__),
    'resources',
    env.audio_file_name + '.wav')

# Loads the audio into memory
with io.open(file_name, 'rb') as audio_file:
    content = audio_file.read()
    audio = speech.RecognitionAudio(content=content)

# Transcribe the audio
config = speech.RecognitionConfig(
    encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
    sample_rate_hertz=48000,
    language_code='ja-JP')

response = client.recognize(config=config, audio=audio)
print(response)

# Print the transcribed text
for result in response.results:
    print('Transcript: {}'.format(result.alternatives[0].transcript))
