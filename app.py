from flask import Flask, render_template, request, jsonify
from openai import OpenAI

app = Flask(__name__, template_folder='templates', static_folder='static')

role = ("You are a healthy living chatbot and you answer questions about healthy living, diet and fitness. You state that you cannot answer on other issues."
        "You give advice and suggestions to people about sports, motivation, and a healthy and organized life. If you want, you can support this with the words of important people. Give your answers in a neat, readable order.")

# Initialize an empty chat history
chat_history = []

def chat_with_gpt(prompt):
    global chat_history
    client = OpenAI(api_key='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')  # Enter Your API KEY
    model = "gpt-4-0314"  # gpt-4-0314 # gpt-3.5-turbo

    # Add the user's input to the chat history
    chat_history.append({"role": "user", "content": prompt})

    messages = [
        {"role": "system", "content": role},
    ]

    # Add all previous messages to the conversation
    messages.extend(chat_history)

    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0
    )

    # Get the model's response
    model_response = response.choices[0].message.content

    # Add the model's response to the chat history
    chat_history.append({"role": "assistant", "content": model_response})

    return model_response

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/send_message', methods=['POST'])
def send_message():
    data = request.get_json()
    user_input = data.get('message')

    # Process the user input
    # Send the user input to ChatGPT and get the response
    gpt_response = chat_with_gpt(user_input)

    # Return the response to the client
    response = {"status": "success", "message": gpt_response}
    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)
