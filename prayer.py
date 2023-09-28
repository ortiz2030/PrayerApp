import os
import openai
import json
from flask import Flask, render_template, request, jsonify

app = Flask(__name__, template_folder="templates")

# Set up OpenAI API credentials using environment variables
openai.api_key = os.getenv("OPENAI_API_KEY")

# Define the filename for storing conversations
CONVERSATION_FILE = "conversations.json"

class ChatApp:
    def __init__(self):
        self.conversations = self.load_conversations()

    def load_conversations(self):
        # Load existing conversations from the JSON file
        if os.path.exists(CONVERSATION_FILE):
            with open(CONVERSATION_FILE, "r") as file:
                return json.load(file)
        return []

    def save_conversations(self):
        # Save the conversations to the JSON file
        with open(CONVERSATION_FILE, "w") as file:
            json.dump(self.conversations, file)

    def custom_chat_gpt(self, user_input, conversation=None):
        if conversation is None:
            conversation = []

        conversation.append({"role": "system", "content": '''
             you are a senior clergy with deep knowledge in prayers and the bible.
             your role is to generate prayers and bible verses as directed by the user. Do not break character'''})

        conversation.append({"role": "user", "content": f"generate for me prayer for {user_input}"})

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=conversation
        )

        chat_gpt_reply = response["choices"][0]["message"]["content"]
        paragraphs = chat_gpt_reply.split('\n')
        formatted_reply = ''
        for paragraph in paragraphs:
            if paragraph.startswith('-'):
                formatted_reply += f'• {paragraph[2:]}<br>'
            else:
                formatted_reply += f'{paragraph}<br>'

        conversation.append({"role": "assistant", "content": chat_gpt_reply})
        
        # Add the conversation to the list
        self.conversations.append({
            "user_input": user_input,
            "response": formatted_reply
        })

        # Save the conversations to the JSON file
        self.save_conversations()

        return formatted_reply, conversation

chat_instance = ChatApp()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_message', methods=['POST'])
def send_message():
    user_input = request.form['user_input']
    response, _ = chat_instance.custom_chat_gpt(user_input, chat_instance.conversations.copy())
    return response

@app.route('/get_conversations', methods=['GET'])
def get_conversations():
    return jsonify(chat_instance.conversations)

if __name__ == '__main__':
    app.run(debug=True)
