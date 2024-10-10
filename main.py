from flask import Flask, request, jsonify
import traceback
from googletrans import Translator
import json
from flask_cors import CORS


app = Flask(__name__)
translator = Translator()

CORS(app, resources={r"/*": {"origins": "https://reactapp.lifechangersind.cloud/"}})


@app.route('/tamil', methods=['POST'])
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

@app.route('/japan', methods=['POST'])
def translate_textj():
    try:
        data = request.get_json()
        text = data.get('text')

        if not isinstance(text, str):
            return jsonify({'error': 'Invalid input. Text should be a string.'}), 400

        if not text:
            return jsonify({'error': 'Text to translate is missing'}), 400

        translation = translator.translate(text, src='en', dest='ja')
        translated_text = translation.text if translation else "Translation failed"
        # Convert to JSON string with Unicode characters
        return json.dumps({'translated_text': translated_text}, ensure_ascii=False), 200

    except Exception as e:
        traceback.print_exc()
        return jsonify({'error': 'An unexpected error occurred.'}), 500

@app.route('/german', methods=['POST'])
def translate_textg():
    try:
        data = request.get_json()
        text = data.get('text')

        if not isinstance(text, str):
            return jsonify({'error': 'Invalid input. Text should be a string.'}), 400

        if not text:
            return jsonify({'error': 'Text to translate is missing'}), 400

        translation = translator.translate(text, src='en', dest='de')
        translated_text = translation.text if translation else "Translation failed"
        # Convert to JSON string with Unicode characters
        return json.dumps({'translated_text': translated_text}, ensure_ascii=False), 200

    except Exception as e:
        traceback.print_exc()
        return jsonify({'error': 'An unexpected error occurred.'}), 500

@app.route('/hindi', methods=['POST'])
def translate_texth():
    try:
        data = request.get_json()
        text = data.get('text')

        if not isinstance(text, str):
            return jsonify({'error': 'Invalid input. Text should be a string.'}), 400

        if not text:
            return jsonify({'error': 'Text to translate is missing'}), 400

        translation = translator.translate(text, src='en', dest='hi')
        translated_text = translation.text if translation else "Translation failed"
        # Convert to JSON string with Unicode characters
        return json.dumps({'translated_text': translated_text}, ensure_ascii=False), 200

    except Exception as e:
        traceback.print_exc()
        return jsonify({'error': 'An unexpected error occurred.'}), 500
        
@app.route('/arb', methods=['OPTIONS', 'POST'])
def translate_ar():
    # Handle CORS preflight requests (OPTIONS method)
    if request.method == 'OPTIONS':
        response = jsonify({})
        response.headers.add('Access-Control-Allow-Origin', 'https://reactapp.lifechangersind.cloud')
        response.headers.add('Access-Control-Allow-Methods', 'POST')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
        return response

    # Process POST request for translation
    try:
        data = request.get_json()

        # Check if data contains 'text' and it's a string
        if not data or not isinstance(data.get('text'), str):
            return jsonify({'error': 'Invalid input. Text should be a string.'}), 400

        text = data['text']

        if not text:
            return jsonify({'error': 'Text to translate is missing.'}), 400

        # Perform translation
        translation = translator.translate(text, src='en', dest='ar')
        translated_text = translation.text if translation else "Translation failed"

        # Return translated text as JSON with Unicode characters
        response = jsonify({'translated_text': translated_text})
        response.headers.add('Access-Control-Allow-Origin', 'https://reactapp.lifechangersind.cloud')
        return response, 200

    except Exception as e:
        traceback.print_exc()
        response = jsonify({'error': 'An unexpected error occurred.'})
        response.headers.add('Access-Control-Allow-Origin', 'https://reactapp.lifechangersind.cloud')
        return response, 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
