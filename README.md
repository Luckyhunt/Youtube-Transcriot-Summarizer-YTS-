# YouTube Transcript Summarizer

## Overview
The **YouTube Transcript Summarizer** is a web application that extracts and summarizes transcripts from YouTube videos. It leverages natural language processing techniques to provide concise summaries, allowing users to quickly grasp key points without watching the entire video.

## Features
- **Transcript Extraction**: Automatically retrieves transcripts from YouTube videos.
- **Summarization Methods**:
  - **Extractive Summarization**: Selects key sentences from the transcript.
  - **Abstractive Summarization**: Generates a summary by rephrasing the original text.
  - **Hybrid Summarization**: Combines both methods (future implementation).
- **Text-to-Speech**: Converts the generated summary into audio format for easy listening.
- **Multi-language Support**: Users can select their preferred language for the summary.

## Technologies Used
- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Python with Flask framework
- **NLP Libraries**: NLTK, Hugging Face Transformers
- **Audio Processing**: Google Text-to-Speech (gTTS)

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Luckyhunt/Youtube-Transcriot-Summarizer-YTS-.git
   ```
2. Navigate to the project directory:
   ```bash
   cd youtube-transcript-summarizer
   ```
3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the application:
   ```bash
   python app.py
   ```

## Usage
1. Open your web browser and navigate to `http://127.0.0.1:5000/`.
2. Enter the YouTube video link and select the desired summary type.
3. Click "Summarize" to generate the summary and download the audio.

## Contributing
Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments
- [YouTube Transcript API](https://github.com/jdepoix/youtube-transcript-api)
- [NLTK](https://www.nltk.org/)
- [Hugging Face Transformers](https://huggingface.co/transformers/)
- [gTTS](https://pypi.org/project/gTTS/)
