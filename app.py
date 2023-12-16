from flask import Flask, render_template, request, jsonify
from openai import OpenAI

app = Flask(__name__, template_folder='templates', static_folder='static')

role = ("You are a healthy living chatbot and you answer questions about healthy living, diet and fitness. You state that you cannot answer on other issues."
        "You give advice and suggestions to people about sports, motivation, and a healthy and organized life. If you want, you can support this with the words of important people.")

def chat_with_gpt(prompt):
    client = OpenAI(api_key='YOUR_APİ_KEY')  # Enter Yur API KEY
    model = "gpt-3.5-turbo"  # gpt-4-0314 # gpt-3.5-turbo
    messages = [
        {"role": "system", "content": role},
        {"role": "user", "content": prompt},
    ]
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0
    )
    return response.choices[0].message.content

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
