# 🤖 Healthy ChatBot - ChatGPT API Integration

Hello there! In this project, my goal was to create an interactive platform where users can ask questions about health and nutrition and receive instant answers via the ChatGPT API.

I developed this project to strengthen my skills in web development (`Flask`, `JavaScript`), API integration (`OpenAI ChatGPT API`), and data processing (`Pandas`).

## 🎯 Project Goal and Approach

The main objective of this project is to guide users by providing quick and accurate answers to their health and nutrition questions. The chatbot leverages both a predefined dataset for information retrieval and ChatGPT's extensive knowledge base for more complex queries.

### 📊 Technologies Used

The project brings together modern web technologies and powerful artificial intelligence tools:

* **Python (Flask)**: A lightweight and flexible web framework for backend development.
* **JavaScript**: Used to provide dynamic interactions in the user interface.
* **OpenAI ChatGPT API**: Serves as the core AI engine of the chatbot, offering natural language processing capabilities across a wide range of information.
* **Pandas**: Used to load and process the JSON formatted dataset (`mydata.json`).
* **difflib.SequenceMatcher**: Used to measure the similarity between user questions and questions in the local dataset.

---

## 📝 System Architecture

The system is based on a simple client-server model:

1.  **User Interface (Frontend)**: A simple web page created with `index.html` and CSS/JS files in the `static` folder. Users enter their questions here.
2.  **Web Server (Backend - Flask)**: Receives and processes requests from the user, then sends back responses.
    * Each incoming user message is first searched within the **local dataset** (`mydata.json`). If a similar question is found, the predefined answer is returned directly.
    * If no suitable answer is found in the local dataset, the question is sent to the **ChatGPT API**.
    * The response from ChatGPT is formatted to match the chatbot's persona, named `Mia`, who is a fitness trainer.
3.  **ChatGPT API**: As an external service, it provides sophisticated natural language understanding and generation capabilities.
4.  **Dataset (`mydata.json`)**: A JSON file within the application that contains specific question-answer pairs. It provides quick responses to frequently asked questions.

---

## 🛠️ Setup and Running

To run this project on your local machine, follow these steps:

1.  **Clone the Repository**:
    ```bash
    git clone https://github.com/BahriDogru/GPT-Based_Personalized_Health_Chatbot.git
    ```
2.  **Navigate to the project directory after cloning**:
    ```bash
    cd GPT-Based_Personalized_Health_Chatbot
    ```
3.  **Install Required Libraries**:
    ```bash
    conda install Flask openai pandas
    ```
    Alternatively, from an `environment.yaml` file:
    ```bash
    conda env create -f environment.yaml
    ```
4.  **Configure Your OpenAI API Key**:
    You need to enter your OpenAI API key where `<YOUR_API_KEY>` is written in the `app.py` file:
    ```python
    client = OpenAI(api_key='YOUR_API_KEY') # Enter your API key here
    ```
    For security, it is highly recommended to set your API key as an environment variable instead of embedding it directly in the code. For example: `os.environ.get("OPENAI_API_KEY")`.
5.  **Place Necessary Files**:
    * Ensure that the `ChatGPT_API_ROLE.txt` file is in the same directory as `app.py`.
    * Ensure that the `mydata.json` file is in the same directory as `app.py`.
    * The `templates` folder (containing `index.html`) and the `static` folder (containing `style.css`, `script.js`, etc.) should be in the same directory as `app.py`.
6.  **Run the Application**:
    ```bash
    python app.py
    ```
    The application will run by default at `http://127.0.0.1:5000/`. You can open your browser and navigate to this address.

7.  **Acknowledgements**:

    I would like to express my gratitude to [meteyilmaz28](https://github.com/meteyilmaz28) for their contributions to this project!
