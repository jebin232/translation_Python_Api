from fastapi import FastAPI, HTTPException
from googletrans import Translator

app = FastAPI()
translator = Translator()

@app.post('/translate/')
async def translate_text(text: str):
    if not text:
        raise HTTPException(status_code=400, detail='Text to translate is missing')
    
    try:
        translation = translator.translate(text, src='en', dest='ta')
        translated_text = translation.text
        return {'translated_text': translated_text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='127.0.0.1', port=8000)
