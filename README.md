## AI Query Script

This Python script allows users to interact with a local AI model (LLaMA 3.1:8B) via an API running on `http://127.0.0.1:11434/api/generate`. The script takes user input, sends it to the API, and streams the response in real-time.
1, First donwload ollama for running model local
2, Second download model using this cmd :ollama run model name example :ollama run llama3.1:8b

---

## Prerequisites

Ensure you have the following installed:
- Python 3.x
- Required Python libraries:
  - `requests`
  - `json`

To install the required libraries, run:
```bash
pip install requests
```

Additionally, make sure the local API server is running at `http://127.0.0.1:11434` before executing the script.
# run local api server : ollama serve 
# for terminal interaction :ollama run llama3.1:8b

---

## How to Use

1. Run the script using:
   ```bash
   python script.py
   ```
2. Enter your queries when prompted.
3. To exit, type `exit` or `quit`.

Example interaction:
```
What's are you minds today? : How does machine learning work?
[Real-time response from the AI]

What's are you minds today? : exit
```

---

## Code Explanation

- **`ask_query(prompt)`**: Sends the user input (`prompt`) to the AI API and streams the response in real-time.
- **Error Handling**: If the API request fails, an error message is displayed.
- **Loop Mechanism**: The script runs continuously until the user types `exit` or `quit`.

---

## Notes
- The script currently assumes the local AI server is up and running.
- Modify the `url` variable if your API endpoint differs.
- The `stream=True` parameter allows for real-time response streaming.

---

## License
This script is provided under the MIT License. Feel free to modify and use it as needed.

