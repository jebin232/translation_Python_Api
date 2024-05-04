from flask import Flask, request, jsonify, get_asgi_application
from googletrans import Translator
from requests.exceptions import RequestException

app = Flask(__name__)
translator = Translator()

@app.route('/translate', methods=['POST'])
async def translate_text():
    data = await request.get_json()
    text = data.get('text')

    if not text:
        return jsonify({'error': 'Text to translate is missing'}), 400

    try:
        translation = translator.translate(text, src='en', dest='ta')
        translated_text = translation.text if translation else "Translation failed"
        return jsonify({'translated_text': translated_text}), 200
    except RequestException as e:
        # traceback.print_exc()
        return jsonify({'error': 'Failed to connect to translation service. Please try again later.'}), 500
    except Exception as e:
        # traceback.print_exc()
        return jsonify({'error': str(e)}), 500

asgi_app = get_asgi_application(app)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(asgi_app, host='0.0.0.0', port=8000)
