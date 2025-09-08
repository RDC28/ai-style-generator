from google import genai

client = genai.Client(api_key="AIzaSyDKkoG4kmMcgTt_CviOZH7lT1BARoeysAk")

models = client.models.list()
print("Models supporting generateContent:")
for m in models:
    if "generateContent" in m.supported_actions:
        print(m.name)