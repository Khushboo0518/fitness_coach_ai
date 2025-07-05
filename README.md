# fitness_coach_ai
AI Fitness Coach — Personalized Health & Fitness Plan Generator
This is a locally-hosted AI-powered Fitness Coach that helps users become fit based on their age, weight, gender, lifestyle, current health, and fitness goals.

💡 What It Does:
Accepts user details like age, weight, lifestyle, etc.

Uses a locally running AI model (via Ollama) to generate:

✅ Personalized fitness plans

🥗 Daily diet charts (Indian & international, veg/non-veg)

🏋️ Workout suggestions

📆 Timeline for visible progress (in weeks/months)

Supports both male & female, and beginner to advanced levels.

🧩 Technologies Used:
🐍 Python

⚡ FastAPI – for backend API

🧠 Ollama + LLaMA 3 – for AI generation (locally hosted)

🖼️ Gradio – for simple UI

💻 Runs fully offline (no API keys needed)

How to Run:
# Start the backend
uvicorn main:app --reload
# Then open the Gradio UI
python ui.py

📸 Features Coming Soon:
1.Save user progress
2.Weekly tracking dashboard
3.Voice assistant mode

🙋 Made by:
Khushboo
