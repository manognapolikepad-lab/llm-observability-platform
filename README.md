# Local-First LLM Observability Platform

A local-first observability platform for monitoring, tracing, and analyzing Large Language Model (LLM) interactions using Ollama.

This project enables prompt tracking, latency monitoring, replay functionality, model tracking, and experiment visibility for local LLM workflows.

## Features

* Prompt and response tracing
* Latency tracking
* Model tracking (Llama3 support)
* Dashboard UI for observability
* Latency visualization charts
* Replay prompts
* SQLite database storage
* Timestamp tracking
* Interactive dashboard interface

## Tech Stack

* Python
* FastAPI
* Ollama
* SQLite
* SQLAlchemy
* Jinja2
* HTML/CSS
* Chart.js

## Project Structure

```text
llm-observability/
│
├── app/
│   ├── main.py
│   ├── tracer.py
│   ├── ollama_client.py
│   ├── database.py
│   └── models.py
│
├── storage/
│   └── traces.db
│
├── templates/
│   └── traces.html
│
├── README.md
└── requirements.txt
```

## How to Run

### 1. Activate virtual environment

Mac/Linux:

```bash
source venv/bin/activate
```

### 2. Run server

```bash
uvicorn app.main:app --reload
```

### 3. Open browser

Dashboard:

```text
http://127.0.0.1:8000/traces-ui
```

Ask endpoint:

```text
http://127.0.0.1:8000/ask?prompt=hello
```

## Future Improvements

* Multi-LLM benchmarking
* Model comparison dashboard
* Search and filtering
* Prompt experiment tracking
* Token analytics
* Response quality evaluation
* Authentication

## Why I Built This

I wanted to better understand how local LLM systems work and explore observability for AI applications. This project helped me learn backend engineering, local model inference, tracing systems, and dashboard development.
