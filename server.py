"""
Flask server for emotion detection application.
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route ('/')
def render_index_page():
    """Render the home page."""
    return render_template('index.html')

@app.route('/emotionDetector')
def emotion_detector_route():
    """Analyze text and return emotion analysis."""
    text_to_analyse = request.args.get("textToAnalyze")

    if text_to_analyse is None or text_to_analyse.strip() == "":
        return "Invalid text! Please try again!"

    result = emotion_detector(text_to_analyse)

    if not result or result.get("dominant_emotion") is None:
        return "Invalid text! Please try again!"

    return (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )

if __name__ == "__main__":
    # ✅ Deploy on localhost:5000
    app.run(host="0.0.0.0", port=5000, debug=True)
