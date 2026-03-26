from flask import Flask, request
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector")
def detect_emotion():
    text = request.args.get('textToAnalyze')

    if text is None or text.strip() == "":
        return "Invalid text! Please try again."

    result = emotion_detector(text)

    if "dominant_emotion" in result:
        return (
            f"For the given statement, the system response is "
            f"'anger': {result['anger']}, "
            f"'disgust': {result['disgust']}, "
            f"'fear': {result['fear']}, "
            f"'joy': {result['joy']}, "
            f"'sadness': {result['sadness']}. "
            f"The dominant emotion is {result['dominant_emotion']}."
        )
    else:
        return "Invalid input"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
