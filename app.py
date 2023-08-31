from flask import Flask, request, jsonify

from flask_cors import CORS
import openai


app = Flask(__name__)
CORS(app)

openai.api_type = "azure"
openai.api_base = ""
openai.api_version = "2023-03-15-preview"
openai.api_key = ""


def chat_response(question):
    return openai.ChatCompletion.create(
        engine="",
        messages=[{"role": "system",
                   "content": "You are an AI assistant that helps people find information."},
                  {
                      "role": "user",
                      "content": question
                  },
                  ],
        temperature=0.7,
        max_tokens=800,
        top_p=0.95,
        frequency_penalty=0,
        presence_penalty=0,
        stop=None)


def get_parameter(req_data):
    data = None
    if req_data.method == 'POST':
        data = req_data.json
    elif req_data.method == 'GET':
        data = req_data.args
    return data


@app.route("/hello")
def hello():
    return "hello"


@app.route('/req_prompt', methods=['POST'])
def req_prompt():
    try:
        question = get_parameter(request)['question']

        response = chat_response(question)
        if response:
            return jsonify({'response': response})
        else:
            return jsonify({'error': 'url not provided'}), 400
    except Exception as e:
        print(e)
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True, host='0.0.0.0', port=80)
