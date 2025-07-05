import gradio as gr
import requests

def get_plan(age, gender, height, weight, goal, diet, activity, time):
    data = {
        "age": int(age), "gender": gender, "height_cm": float(height),
        "weight_kg": float(weight), "goal": goal,
        "diet_type": diet, "activity_level": activity,
        "time_available": int(time)
    }
    response = requests.post("http://localhost:8000/generate-plan", json=data)
    return response.json()["plan"]

iface = gr.Interface(
    fn=get_plan,
    inputs=[
        gr.Number(label="Age"),
        gr.Radio(["male", "female"], label="Gender"),
        gr.Number(label="Height (cm)"),
        gr.Number(label="Weight (kg)"),
        gr.Textbox(label="Goal (e.g. Lose 5 kg)"),
        gr.Radio(["indian_veg", "indian_nonveg", "global_veg", "global_nonveg"], label="Diet Type"),
        gr.Radio(["sedentary", "light", "moderate", "active", "athlete"], label="Activity Level"),
        gr.Number(label="Available Time (minutes/day)")
    ],
    outputs="text",
    title="Offline Fitness & Diet Coach"
)

iface.launch()
