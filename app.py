from flask import Flask
import ollama

app = Flask(__name__)


@app.route('/<context>/<prompt>')
def prompt_(context, prompt):
    response = ollama.chat(
        model='gemma:2b', messages=[
            {
                'role': 'system',
                'context': context,
            },
            {
                'role': 'user',
                'content': prompt
            }
        ]
    )
    return response['message']['content']


if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')
