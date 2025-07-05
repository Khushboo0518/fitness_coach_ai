from fastapi import FastAPI
from pydantic import BaseModel
import requests

app = FastAPI()

class UserProfile(BaseModel):
    age: int
    gender: str
    height_cm: float
    weight_kg: float
    goal: str
    diet_type: str
    activity_level: str
    time_available: int

def calculate_bmr(gender, weight, height, age):
    return 10 * weight + 6.25 * height - 5 * age + (5 if gender == "male" else -161)

def calculate_tdee(bmr, activity_level):
    levels = {
        "sedentary": 1.2, "light": 1.375, "moderate": 1.55,
        "active": 1.725, "athlete": 1.9
    }
    return bmr * levels.get(activity_level.lower(), 1.2)

def build_prompt(profile, calories):
    return f"""
You are a fitness and nutrition expert.

Create a personalized plan:
- Age: {profile.age}, Gender: {profile.gender}
- Height: {profile.height_cm} cm, Weight: {profile.weight_kg} kg
- Goal: {profile.goal}, Activity Level: {profile.activity_level}
- Diet: {profile.diet_type}, Time: {profile.time_available} min/day
- Daily calories: {int(calories)} kcal

Give a 3-month plan with:
1. Estimated months to goal
2. Daily Exercise Plan
3. Daily Indian + Global Meals (Veg/Non-Veg based on diet_type)
Output in JSON.
"""

@app.post("/generate-plan")
def generate_fitness_plan(profile: UserProfile):
    bmr = calculate_bmr(profile.gender, profile.weight_kg, profile.height_cm, profile.age)
    calories = calculate_tdee(bmr, profile.activity_level)
    prompt = build_prompt(profile, calories)

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={"model": "llama3", "prompt": prompt, "stream": False}
    )

    return {"plan": response.json()["response"]}
