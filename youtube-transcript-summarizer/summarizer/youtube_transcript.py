from youtube_transcript_api import YouTubeTranscriptApi

def get_transcript(video_url):
    try:
        video_id = video_url.split('v=')[1]
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        return ' '.join([item['text'] for item in transcript])
    except Exception as e:
        print(f"Error fetching transcript: {e}")
        return None