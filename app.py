from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)

# مفتاح OpenAI السري - هنعمله بعدين كمتغير بيئي (environment variable)
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()
    question = data.get("question", "")

    if not question:
        return jsonify({"answer": "مفيش سؤال!"}), 400

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # أو gpt-4 لو عندك اشتراك
            messages=[{"role": "user", "content": question}],
            temperature=0.7,
            max_tokens=100
        )
        answer = response["choices"][0]["message"]["content"]
        return jsonify({"answer": answer})
    except Exception as e:
        return jsonify({"answer": f"حصل خطأ: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
