import nltk
from nltk.tokenize import sent_tokenize
from transformers import pipeline
import tensorflow as tf

# Ensure the punkt tokenizer is downloaded
nltk.download('punkt')

# Define the model name globally
model_name = "sshleifer/distilbart-cnn-12-6"

# Initialize the pipeline variable globally
pipeline_instance = None

def initialize_pipeline():
    global pipeline_instance
    try:
        if model_name:
            pipeline_instance = pipeline("summarization", model=model_name)
    except Exception as e:
        print(f"Error initializing pipeline: {e}")

def summarize_text(text, summary_type):
    try:
        if summary_type == 'extractive':
            sentences = sent_tokenize(text)
            return ' '.join(sentences[:5])
        elif summary_type == 'abstractive':
            initialize_pipeline()
            if pipeline_instance is not None:
                summary = pipeline_instance(text, max_length=150, min_length=30, do_sample=False)
                return summary[0]['summary_text']
            else:
                raise ValueError("Pipeline is not initialized.")
        elif summary_type == 'hybrid':
            return "Hybrid summarization not implemented yet."
    except Exception as e:
        print(f"Error during summarization: {e}")
        return None

def split_into_chunks(input_sequence, max_length=1024):
    return [input_sequence[i:i + max_length] for i in range(0, len(input_sequence), max_length)]