from flask import Flask, render_template, request, jsonify
from openai import OpenAI
from difflib import SequenceMatcher  # Benzerlik kontrolü için eklenen kütüphane
import pandas as pd

app = Flask(__name__, template_folder='templates', static_folder='static')

role = ("Your name is Mia, and you are a fitness trainer with extensive experience in creating diets and designing workout programs."
"You have been actively involved in sports for many years, participating in competitions, achieving accolades, and mentoring numerous athletes. Your expertise lies in diet planning, healthy eating, and fitness training."
"When faced with questions in these areas, you provide clear and informative answers. You don't answer questions other than these subjects."
"When asked, 'Who are you?' you introduce yourself in a simple manner. When people seek new diet or fitness programs from you, you initially request information from them so that you can tailor personalized programs for their needs."
"Don't forget to make jokes and jokes once in a while while answering. Be a little more sympathetic.")

# Initialize an empty chat history
chat_history = []

# Load data from JSON file into a Pandas DataFrame
df = pd.read_json('./mydata.json')
# Extract questions and answers from the DataFrame
question_answer_data = []

def extract_question_answer(row):
    question = row['sorular']
    answer = row['cevaplar']
    return {"soru": question, "cevap": answer}

question_answer_data = df['veriler'].apply(extract_question_answer).tolist()

def find_answer_in_dataset(question):
    # Check if the question is in the dataset with case-insensitive comparison
    question = question.lower()
    for dataset_item in question_answer_data:
        if SequenceMatcher(None, question, dataset_item['soru'].lower()).ratio() > 0.7:
            return dataset_item['cevap']
        

def chat_with_gpt(prompt):
    global chat_history
    answer = find_answer_in_dataset(prompt)
    
    if answer:
        chat_history.append({"role": "assistant", "content": answer})
        return answer
    else:
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
            temperature=1,
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
