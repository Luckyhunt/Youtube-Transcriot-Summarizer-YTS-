import moviepy.editor as mp
import speech_recognition as sr
import os

def extract_audio(video_url):
    try:
        video = mp.VideoFileClip(video_url)
        audio_path = 'audio.wav'
        video.audio.write_audiofile(audio_path)
        return audio_path
    except Exception as e:
        print(f"Error extracting audio: {e}")
        return None

def convert_audio_to_text(audio_path):
    try:
        recognizer = sr.Recognizer()
        with sr.AudioFile(audio_path) as source:
            audio = recognizer.record(source)
            return recognizer.recognize_google(audio)
    except Exception as e:
        print(f"Error converting audio to text: {e}")
        return None
    finally:
        if os.path.exists(audio_path):
            os.remove(audio_path)