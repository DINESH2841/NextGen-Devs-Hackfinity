import random

def analyze_feedback(comment: str):
    """
    Mocks AI-based feedback analysis (e.g., sentiment analysis).
    """
    sentiments = ["Positive", "Neutral", "Negative"]
    mock_sentiment = random.choice(sentiments)
    
    print(f"🧠 Mock Feedback AI: Analyzed comment. Sentiment is '{mock_sentiment}'.")
    
    return {
        "sentiment": mock_sentiment,
        "keywords": ["mock", "feedback", "analysis"]
    }