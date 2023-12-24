# app.py

from flask import Flask, render_template, request, jsonify
import openai
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

openai.api_key = os.getenv("OPENAI_API_KEY")
if not openai.api_key:
    raise ValueError("OpenAI API Key not set")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    prompt = request.form.get("prompt")

    response = generate_text(prompt)

    return jsonify({"response": response})

def generate_text(prompt):
    model = "text-davinci-002"
    max_tokens = 1000

    response = openai.Completion.create(
        engine=model,
        prompt=prompt,
        max_tokens=max_tokens
    )

    return response["choices"][0]["text"]

if __name__ == "__main__":
    app.run(debug=True)
