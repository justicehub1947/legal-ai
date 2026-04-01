from fastapi import FastAPI
from openai import OpenAI
import os

app = FastAPI()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@app.get("/")
def home():
    return {"message": "JusticeHub Legal AI Running 🚀"}

@app.post("/legal")
def legal_ai(input_text: str):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role":"system","content":"You are an Indian legal expert specialized in RBI and IPC laws."},
            {"role":"user","content":input_text}
        ]
    )
    return {"result": response.choices[0].message.content}
