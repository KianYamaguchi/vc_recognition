from fastapi import FastAPI, WebSocket
import speech_recognition as sr

app = FastAPI()
recognizer = sr.Recognizer()

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    with sr.Microphone() as source:
        while True:
            try:
                audio = recognizer.listen(source)
                text = recognizer.recognize_google(audio, language="ja-JP")
                await websocket.send_text(text)
            except sr.UnknownValueError:
                await websocket.send_text("音声を認識できませんでした。")
            except sr.RequestError:
                await websocket.send_text("Google音声認識サービスに接続できませんでした。")