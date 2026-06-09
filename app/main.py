from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from app.ollama_client import ask_llama
from app.tracer import trace_request
from fastapi.responses import RedirectResponse
import time

app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get("/")
def home():
    return {"message": "LLM Observability Running 🚀"}


@app.get("/ask")
def ask(prompt: str, replay: bool = False):
    start_time = time.time()

    response = ask_llama(prompt)

    end_time = time.time()
    time_taken = end_time - start_time

    trace_request(prompt, response, time_taken)

    if replay:
        return RedirectResponse(
            url="/traces-ui",
            status_code=302
        )

    return {"response": response}

from app.database import SessionLocal
from app.models import Trace

@app.get("/traces")
def get_traces():
    db = SessionLocal()

    traces = db.query(Trace).all()

    result = []

    for trace in traces:
        result.append({
            "id": trace.id,
            "prompt": trace.prompt,
            "response": trace.response,
            "time_taken": trace.time_taken,
            "model_name": trace.model_name,
            "timestamp": trace.timestamp
        })

    db.close()

    return result

@app.get("/traces-ui")
def traces_ui(request: Request):
    db = SessionLocal()

    traces = db.query(Trace).all()

    total_requests = len(traces)

    if traces:
        avg_latency = round(
            sum(trace.time_taken for trace in traces)
            / total_requests,
            2
        )

        fastest = round(
            min(trace.time_taken for trace in traces),
            2
        )

        slowest = round(
            max(trace.time_taken for trace in traces),
            2
        )
    else:
        avg_latency = 0
        fastest = 0
        slowest = 0

    db.close()

    return templates.TemplateResponse(
        request=request,
        name="traces.html",
        context={
            "traces": traces,
            "total_requests": total_requests,
            "avg_latency": avg_latency,
            "fastest": fastest,
            "slowest": slowest
        }
    )

from fastapi.responses import HTMLResponse


@app.get("/traces-ui")
def traces_ui(request: Request, search: str = ""):
    db = SessionLocal()

    if search:
        traces = db.query(Trace).filter(
        Trace.prompt.ilike(f"%{search}%")
        ).all()
    else:
        traces = db.query(Trace).all()

    total_requests = len(traces)

    if traces:
        avg_latency = round(
            sum(trace.time_taken for trace in traces)
            / total_requests,
            2
        )

        fastest = round(
            min(trace.time_taken for trace in traces),
            2
        )

        slowest = round(
            max(trace.time_taken for trace in traces),
            2
        )
    else:
        avg_latency = 0
        fastest = 0
        slowest = 0

    db.close()

    return templates.TemplateResponse(
        request=request,
        name="traces.html",
        context={
            "traces": traces,
            "total_requests": total_requests,
            "avg_latency": avg_latency,
            "fastest": fastest,
            "slowest": slowest,
            "search": search
        }
    )