import os
import re
import json
import base64
from groq import Groq
from dotenv import load_dotenv
from datetime import datetime
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

load_dotenv()
api_key_vigilant = os.getenv("API_KEY_VIGILANT")
encrypter1 = os.getenv("inte")
encrypter2 = os.getenv("joy")
hidden = os.getenv("hide")

client = Groq(api_key=api_key_vigilant)

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

port = int(os.environ.get('PORT', 8080))

app.mount("/public/static", StaticFiles(directory="public/static"), name="static")


def clean_response(output):
    return re.sub(r"<think>.*?</think>", "", output, flags=re.DOTALL).strip()

@app.get("/")
async def serve_homepage():
    return FileResponse("index.html")
@app.get("/chat")
async def serve_chatpage():
    file_path = os.path.abspath("public/templates/portfolio_management.html")
    print(f"Serving file: {file_path}")  # Debugging output
    if not os.path.exists(file_path):
        print("Error: File does not exist!")
        return JSONResponse(content={"error": "File not found"}, status_code=404)
    return FileResponse(file_path)
@app.post("/chat")
async def chat(request: Request):
    try:
        # >> it parses all user inputs <<
        data = await request.json()
        username = data.get("username", "Unknown User")
        user_input = data.get("message", "")

        if not user_input:
            return JSONResponse(content={"error": "No message provided"}, status_code=400) # error 

        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
        chat_completion = client.chat.completions.create(
            messages=[
                {
                "role": "system",
                "content": (
                    "You are **Moneto**, an AI financial expert for Indian users. 🏦💰\n\n"

                    "🎯 **Primary Role:**\n"
                    "- Evaluate user financial decisions with accuracy & responsibility.\n"
                    "- Guide users to make wise money choices, never agreeing to incorrect statements.\n"
                    "- Keep explanations concise yet detailed, balancing depth and clarity.\n\n"

                    "💡 **Answering Style:**\n"
                    "- Provide **direct, clear, and structured** responses.\n"
                    "- Prefer **Indian Rupees (₹)**, but show USD equivalents when needed.\n"
                    "- Use **real-time exchange rates** when discussing currency conversions.\n"
                    "- Format responses with **paragraphs and bullet points** for clarity.\n"
                    "- Add **emojis** to make interactions engaging. 🤩📊\n\n"

                    "📌 **Restrictions:**\n"
                    "- Never promote gambling apps or fraudulent financial schemes.\n"
                    "- For non-financial topics, briefly relate them to finance and say: "
                    "'I am not an expert in that field. Let's talk about finance! 😊'\n\n"

                    "✅ **Example Answer Formatting:**\n"
                    "- 📌 *Main Summary Point*\n"
                    "- 💡 *Key Insight*\n"
                    "- 💰 *Monetary Impact*\n"
                    "- 🔎 *Additional Considerations*\n\n"

                    "Always prioritize ethical, practical, and **India-focused** financial advice. 🇮🇳📈"
                    "Currently ==> 1 United States Dollar equals 86.00 Indian Rupee"
                    "If the question is finance-related, provide a direct, concise answer, "
                    "stating whether the user's thinking is correct and guiding them if necessary. "
                    "For non-financial questions, creatively relate them to finance and answer briefly. "
                    "Always end non-financial answers(dont write this in very general topics ) with: 'I am not an expert in that field of interest.Lets talk about finance :) '"
                    "Always give short and crisp answers which are to the point."
                    "Be responsible for other's hard earned money"
                    "Elaborate your response and make it big enoough for the user to make him understand the surrounding things related to his question"
                    "Never agree to anything wrong that the user says as it may lead him on a bad path"
                    "Do not promote 3-rd party gambling apps or companies"   
                    "Make sure that is suitable for indian users mainly"
                    "provide results in rupess ans main priority and if the resultis related to dollars then also show to rupee equivalent"
                    "Try using the current conversion rate of rupee and dollar"  
                    "Answer in both paragraph and bullet points"    
                    "If possible then always try adding bullet points either to ellaborate or to summarize the response" 
                    "Use emoji and make the experience fun for the user"
                    "Try using new lines more frequently"  
                )
                },
                {
                    "role": "user",
                    "content": user_input,
                },

            ],
            model="deepseek-r1-distill-llama-70b", 

            temperature=0.5,

            top_p=0.85,

            stop=None,

            stream=False,
        )

        ai_response = chat_completion.choices[0].message.content
        final_answer = clean_response(ai_response)

        # to save user data in encrypted form
        median = username.encode("ascii")
        base64_bytes = base64.b64encode(median)
        mixer = base64_bytes.decode("ascii")
        trans = encrypter1 + mixer + encrypter2
        median2 = mixer.encode("ascii")
        base64_bytes = base64.b64encode(median2)
        username = base64_bytes.decode("ascii")

        with open("user_data.txt", "a") as file:
            file.write(f"User: {username}\n")
            file.write(f"Time: {current_time}\n")
            file.write(f"User Input: {user_input}\n")
            file.write("-" * 69*2 + "\n")

        # print("Sending response:", final_answer)
        
        return JSONResponse(content={"response": final_answer}, media_type="application/json")
   
    except Exception as e:
        print("Error:", str(e))
        return JSONResponse(content={"error": "Internal Server Error"}, status_code=500)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=port, log_level="info")
