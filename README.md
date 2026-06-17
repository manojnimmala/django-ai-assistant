# Django + Groq AI Chatbot

A simple AI-powered chatbot built using Django and Groq API. Users can enter questions through a web interface and receive AI-generated responses in real time.

## Features

* Django web application
* Groq API integration
* AI-powered question answering
* Simple and responsive user interface
* Markdown-formatted AI responses
* Custom CSS styling
* Secure API key management using `.env`

## Technologies Used

* Python
* Django
* Groq API
* HTML
* CSS
* Markdown
* python-dotenv

## Project Structure

```text
chatbot/
├── static/
│   └── css/
│       └── style.css
├── templates/
│   └── chat.html
├── ai.py
├── urls.py
├── views.py
└── models.py

myproject/
├── settings.py
├── urls.py
└── wsgi.py

manage.py
```

## Installation

1. Clone the repository

```bash
git clone <repository-url>
cd <repository-name>
```

2. Create a virtual environment

```bash
python -m venv venv
```

3. Activate the virtual environment

Windows:

```bash
venv\Scripts\activate
```

4. Install dependencies

```bash
pip install django groq python-dotenv markdown
```

5. Create a `.env` file in the project root

```env
GROQ_API_KEY=your_groq_api_key
```

6. Run the server

```bash
python manage.py runserver
```

7. Open in browser

```text
http://127.0.0.1:8000
```

## How It Works

1. User enters a question in the web interface.
2. Django receives the request.
3. The question is sent to the Groq API.
4. The AI model generates a response.
5. Django renders the response on the webpage.

## Future Improvements

* Chat history
* User authentication
* Multiple conversations
* Dark mode
* Streaming AI responses
* Database storage for conversations

## Author

Manoj

Built as a learning project to explore Django and AI integration using Groq.
