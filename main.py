from flask import Flask, request, jsonify
from googletrans import Translator
import asyncio
import uvicorn

app = Flask(__name__)
translator = Translator()

@app.route('/translate', methods=['POST'])
def translate_text():
    data = request.get_json()
    text = data.get('text')

    if not text:
        return jsonify({'error': 'Text to translate is missing'}), 400

    try:
        translation = translator.translate(text, src='en', dest='ta')
        translated_text = translation.text if translation else "Translation failed"
        return jsonify({'translated_text': translated_text}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
