"""
server.py

Defines the Flask application that exposes the emotion-detection endpoint
using IBM Watson’s EmotionPredict NLP service.
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")


@app.route("/emotionDetector")
def sent_analyzer():
    """
    Retrive the result
    """
    text_to_analyze = request.args.get('textToAnalyze')

    response = emotion_detector(text_to_analyze)

    # Extract the label and score from the response
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']

    if dominant_emotion is None:
        return "Invalid text! Please try again!"
    # Return a formatted string with the sentiment label and score
    output = (
        f"For the given statement, the system response is 'anger': {anger}, "
        f"'disgust': {disgust}, 'fear': {fear}, 'joy': {joy}, "
        f"'sadness': {sadness}. The dominant emotion is {dominant_emotion}")

    return output

@app.route("/")
def render_index_page():
    """
    Render the page
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
