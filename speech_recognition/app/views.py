# nltk.download('punkt')
import os

import nltk
import requests
from bs4 import BeautifulSoup
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from gtts import gTTS
from nltk.tokenize import word_tokenize
from spacy import displacy

import speech_recognition as sr


def index(request):
    return render(request,'index.html')

# # Speech-to-Text
# def recognize_speech():
#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#         audio = r.listen(source)
#         try:
#             text = r.recognize_google(audio, language="en-US")
#             return text
#         except sr.UnknownValueError:
#             return "Sorry, I didn't understand"

# # NLP Processing
# def process_text(text):
#     # Tokenize text
#     tokens = word_tokenize(text)
#     # Part-of-speech tagging
#     pos_tags = nltk.pos_tag(tokens)
#     # Dependency parsing
#     dependencies = displacy(text)
#     # Entity recognition
#     entities = []
#     # ... (add more NLP tasks as needed)
#     return pos_tags, dependencies, entities

# # Text-to-Speech
# def speak_text(text):
#     tts = gTTS(text=text, lang="en")
#     filename = "temp.mp3"
#     tts.save(filename)
#     os.system(f"mpg321 {filename}")

# # Webhook endpoint
# @csrf_exempt
# def assistant(request):
#     if request.method == 'POST':
#         text = request.POST.get('text')
#         pos_tags, dependencies, entities = process_text(text)
#         response = {
#             'text': text,
#             'pos_tags': pos_tags,
#             'dependencies': dependencies,
#             'entities': entities
#         }
#         return JsonResponse(response)
#     return JsonResponse({'error': 'Invalid request'})


# Function to recognize speech from the microphone
def recognize_speech_from_mic():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    with microphone as source:
        print("Say something!")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        print(f"You said: {text}")
        return text
    except sr.RequestError:
        print("API unavailable")
        return "API unavailable"
    except sr.UnknownValueError:
        print("Unable to recognize speech")
        return "Unable to recognize speech"

# Function to process the recognized text
def process_text(text):
    if "search" in text.lower():
        search_term = text.lower().replace("search", "").strip()
        return search_term
    return None

# Function to perform a web search
def perform_search(query):
    search_url = f"https://www.google.com/search?q={query}"
    response = requests.get(search_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    results = [a.text for a in soup.find_all('a', href=True)]
    return results

# Function to convert text to speech and play it
def text_to_speech(text):
    tts = gTTS(text=text, lang='en')
    tts.save("response.mp3")
    os.system("start response.mp3")  # 'start' command works on Windows, use 'open' on macOS

# Main function to handle voice commands
def voice_command(request):
    text = recognize_speech_from_mic()
    query = process_text(text)
    if query:
        results = perform_search(query)
        response_text = "Here are the results for your search."
        text_to_speech(response_text)
        return JsonResponse({"results": results})
    return JsonResponse({"error": "Could not process the voice input"})

# Debugging: Run the voice_command function
if __name__ == "__main__":
    # Simulating a request
    class MockRequest:
        pass

    mock_request = MockRequest()
    response = voice_command(mock_request)
    print(response)
