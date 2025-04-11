from gtts import gTTS

def text_to_speech(text, lang='en'):
    try:
        tts = gTTS(text=text, lang=lang)
        audio_path = 'static/summary.mp3'
        tts.save(audio_path)
        return audio_path
    except Exception as e:
        print(f"Error during text-to-speech conversion: {e}")
        return None