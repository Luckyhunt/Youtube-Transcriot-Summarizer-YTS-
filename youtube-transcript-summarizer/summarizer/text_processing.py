import nltk

nltk.download('punkt')

def tokenize_text(text):
    try:
        return nltk.word_tokenize(text)
    except Exception as e:
        print(f"Error during tokenization: {e}")
        return None
