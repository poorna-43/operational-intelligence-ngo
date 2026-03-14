from fastapi import FastAPI
from analytics.analysis import load_data, compute_metrics, generate_summary, generate_insights

app = FastAPI()

data = load_data()
data = compute_metrics(data)


@app.get("/")
def home():
    return {"message": "NGO Operational Intelligence API"}


@app.get("/summary")
def summary():
    return generate_summary(data)


@app.get("/insights")
def insights():
    return generate_insights(data)


@app.get("/programs")
def programs():
    return data.to_dict(orient="records")