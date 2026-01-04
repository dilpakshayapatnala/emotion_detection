from flask import Flask, render_template, request
from transformers import pipeline

app = Flask(__name__)

# Pre-trained emotion classifier
emotion_classifier = pipeline(
    "text-classification",
    model="j-hartmann/emotion-english-distilroberta-base",
    return_all_scores=True
)

emoji_map = {
    "joy": "😄",
    "sadness": "😢",
    "anger": "😡",
    "fear": "😨",
    "surprise": "😲",
    "love": "😍",
    "neutral": "😐"
}

@app.route("/", methods=["GET", "POST"])
def home():
    emotion = None
    confidence = 0
    emoji = ""
    if request.method == "POST":
        feedback = request.form["feedback"]
        result = emotion_classifier(feedback)[0]
        top = max(result, key=lambda x: x['score'])
        emotion = top['label'].capitalize()
        confidence = round(top['score']*100,2)
        emoji = emoji_map.get(top['label'], "🤔")
    return render_template("index.html", emotion=emotion, confidence=confidence, emoji=emoji)

if __name__ == "__main__":
    app.run(debug=True)
