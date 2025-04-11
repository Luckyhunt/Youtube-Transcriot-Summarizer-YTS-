
from flask import Flask, render_template, request, jsonify
from summarizer.youtube_transcript import get_transcript
from summarizer.summarization import summarize_text
from summarizer.audio_processing import extract_audio, convert_audio_to_text
from summarizer.text_to_speech import text_to_speech
from langdetect import detect
from googletrans import Translator

app = Flask(__name__)
translator = Translator()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/summarize', methods=['POST'])
def summarize():
    video_url = request.form['video_url']
    summary_type = request.form['summary_type']
    transcript = get_transcript(video_url)
    
    if transcript is None:
        return jsonify({'error': 'Failed to retrieve transcript.'}), 400

    summary = summarize_text(transcript, summary_type)

    if summary is None:
        return jsonify({'error': 'Failed to generate summary.'}), 500
    
    audio_path = text_to_speech(summary)
    return jsonify({'summary': summary, 'audio_path': audio_path})

if __name__ == '__main__':
    app.run(debug=True)