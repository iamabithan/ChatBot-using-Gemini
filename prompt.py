
import google.generativeai as genai


genai.configure(api_key="AIzaSyDBuv7rHsjlMlWlATqpNoruBB_W3Qb9f6c")

generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
)

chat_session = model.start_chat(
  history=[
  ]
)

response = chat_session.send_message("Notable alumni of Dr. SNS Rajakalshimi College of Arts and Science")

print(response.text)