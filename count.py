from fastapi import FastAPI
app = FastAPI()

Dashboard_data = {
    
    "Active_users": 87483456,
    "Query_success_rate": "99%",
    "Transaction_success": "99%" ,
    "Total_collections_made" : "Rs. 63,26,596"
}

@app.get("/dashboard")
async def dashboard():
    return Dashboard_data