from fastapi import FastAPI
app = FastAPI()

queries_per_topic={
    "Account Balance": 34834623,
    "Pay EMI": 34376374,
    "Apply for Loan": 25436472,
    "Recent Transactions": 23562437,
    "Account Statement": 57326473,
    "Deposits": 64324627
}

@app.get("/queries")
def get_queries_per_topic():
    return {"queries": queries_per_topic}

