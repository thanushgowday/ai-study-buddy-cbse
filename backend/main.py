from fastapi import FastAPI

app = FastAPI(title="AI Study Buddy API")

@app.get("/")
def home():
    return {
        "status": "API running",
        "day": 1,
        "dev": "thanushgowday", 
        "msg": "1Cr journey started"
    }

@app.post("/extract-pdf")
async def extract_pdf():
    return {"status": "Day 2: Add PDF + Gemini logic"}