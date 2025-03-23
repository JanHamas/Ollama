import requests
import json

def ask_query(prompt):
    url = "http://127.0.0.1:11434/api/generate"
    data = {
        "model": "llama3.1:8b",
        "prompt": prompt,
        "stream": True  # Stream response for real-time output
    }

    response = requests.post(url, json=data, stream=True)

    if response.status_code == 200:
        full_response = ""  # Store the complete response
        for line in response.iter_lines():
            if line:
                try:
                    json_data = json.loads(line)  # Parse JSON
                    text = json_data["response"]
                    print(text, end="", flush=True)  # Print response in real-time
                    full_response += text  # Append response text
                except json.JSONDecodeError:
                    continue  # Skip invalid lines
        return full_response  # Return full response instead of None
    else:
        print("\nError:", response.status_code, response.text)
        return None  # Return None if request fails

while True:
    # query = input("\nWhat's on your mind? : ")
    query=input("What's are you minds today? :")
    if query.lower() in ["exit", "quit"]:
        break  # Exit the loop if user types "exit" or "quit"
    
    model_response = ask_query(query)
    print("\n")  # Ensure a new line after response
