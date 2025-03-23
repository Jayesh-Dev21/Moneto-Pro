import os
import re
import base64
from groq import Groq
from dotenv import load_dotenv
from datetime import datetime

current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

load_dotenv()
api_key_vigilant = os.getenv("API_KEY_VIGILANT")
encrypter1 = os.getenv("inte")
encrypter2 = os.getenv("joy")
hidden = os.getenv("hide")

client = Groq(api_key=api_key_vigilant)


username = input("Username: ")
user_input = input("You: ")  

if user_input.lower() in ["exit", "quit"]:
    print("Exiting chat...")
    exit() # bye!!! code ended



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

def clean_response(output):
    # removes <think>...</think> block paring the output
    output = re.sub(r"<think>.*?</think>", "", output, flags=re.DOTALL).strip()
    return output

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

with open("deepseek_thoughts.txt", "a") as file:
    file.write(f"User: {username}\n")
    file.write(f"Time: {current_time}\n")
    file.write(f"User Input: {user_input}\n")
    file.write("-" * 69*2 + "\n")


# prints the final result
print(clean_response(final_answer))