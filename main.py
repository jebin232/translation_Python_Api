from flask import Flask, request, jsonify
import traceback
from googletrans import Translator
import json

app = Flask(__name__)
translator = Translator()

@app.route('/translate', methods=['POST'])
def translate_text():
    try:
        data = request.get_json()
        text = data.get('text')

        if not isinstance(text, str):
            return jsonify({'error': 'Invalid input. Text should be a string.'}), 400

        if not text:
            return jsonify({'error': 'Text to translate is missing'}), 400

        translation = translator.translate(text, src='en', dest='ta')
        translated_text = translation.text if translation else "Translation failed"
        # Convert to JSON string with Unicode characters
        return json.dumps({'translated_text': translated_text}, ensure_ascii=False), 200

    except Exception as e:
        traceback.print_exc()
        return jsonify({'error': 'An unexpected error occurred.'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
