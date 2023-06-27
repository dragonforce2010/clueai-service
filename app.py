from flask import Flask, request
from flask_cors import CORS
import clueai

app = Flask(__name__)
CORS(app)
cli = clueai.Client('75RYl0B76oYvpua-hfc2P10110101101', check_api_key=True)


def init():
    pass


@app.route('/')
def index():
    return 'hello world!'


@app.route('/test')
def test():
    return 'test path'


@app.route('/api/chat', methods=['POST'])
def chat():
    prompt = request.json.get('Message')
    if not prompt:
        return r'can not resolve your input, please try again later'
    predition = cli.generate(model_name='ChatYuan-large', prompt=prompt)
    print('response: ', predition.generations[0].text)
    return {
        "content": predition.generations[0].text
    }


if __name__ == '__main__':
    app.run(port=5000)
