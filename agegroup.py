from fastapi import FastAPI
app = FastAPI()



service_utilization_by_age_group = {
    0: {"id":1,"age_group": "18-30", "customers": 45300},
    1: {"id":2,"age_group": "31-40", "customers": 34400},
    2: {"id":3,"age_group": "41-50", "customers": 24400},
    3: {"id":4,"age_group": "51-60", "customers": 13400},
    4: {"id":5,"age_group": "Above 60", "customers": 7800}
}


@app.get("/service_utilization")
def get_service_utilization_by_age_group():
    return {"service_utilization": service_utilization_by_age_group}