from app.database import SessionLocal
from app.models import Trace
import time


def trace_request(prompt, response, time_taken):
    db = SessionLocal()

    trace = Trace(
    prompt=prompt,
    response=response,
    time_taken=time_taken,
    model_name="llama3",
    timestamp=time.time()
    )

    db.add(trace)
    db.commit()

    print("\nNEW LLM TRACE")
    print(f"Prompt: {prompt}")
    print(f"Response: {response[:80]}...")
    print(f"Time Taken: {time_taken:.2f} sec")

    db.close()