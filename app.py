from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)

# قراءة مفتاح OpenAI من متغير البيئة
openai.api_key = os.environ.get("OPENAI_API_KEY")

@app.route("/")
def home():
    return "Zarbanah AI Server is running."

@app.route("/ask", methods=["POST"])
def ask():
    try:
        data = request.get_json()
        question = data.get("question", "")

        if not question:
            return jsonify({"answer": "اكتب سؤال يا نجم!"}), 400

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": question}
            ],
            temperature=0.7
        )

        answer = response['choices'][0]['message']['content']
        return jsonify({"answer": answer})

    except Exception as e:
        return jsonify({"answer": f"حصل خطأ: {str(e)}"}), 500

# تشغيل السيرفر بالطريقة الصحيحة لبيئة Render
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
