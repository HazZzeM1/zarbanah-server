from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)

# خُد المفتاح من environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/ask", methods=["POST"])
def ask():
    try:
        data = request.get_json()
        question = data.get("question", "")

        if not question:
            return jsonify({"error": "No question provided"}), 400

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "أنت مساعد ذكي يتحدث بالعربية."},
                {"role": "user", "content": question}
            ]
        )

        answer = response["choices"][0]["message"]["content"]
        return jsonify({"answer": answer})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
