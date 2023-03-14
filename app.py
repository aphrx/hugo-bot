import os
import openai
from dotenv import load_dotenv
from slack_bolt.adapter.socket_mode import SocketModeHandler
from slack_bolt import App
from database import setup_db

db = [{}]

load_dotenv()

app = App(token=os.environ["SLACK_BOT_TOKEN"])
openai.api_key = os.environ["OPENAI_API_KEY"]
messages = [
        {"role": "system", "content": "You are an Australian Shepherd named Hugo whose owner is Yves Mayotte."}
]

@app.command("/say-hi")
def hello_command(ack, body):
    user_id = body["user_id"]
    ack(f"Hi, <@{user_id}>!")

@app.event("app_mention")
def event_test(say, event):
    question = str(event['text'])
    messages.append({'role': 'user', 'content': question})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
        )
    resp = str(response['choices'][0]['message']['content'])
    messages.append({'role': 'assistant', 'content': resp})
    say(resp)



if __name__ == "__main__":
    conn = setup_db()
    SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"]).start()