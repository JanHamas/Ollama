import requests
import json
# ollama serve
# ollama run llama3.1:8b

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



query="""
Below is the 'About Me'.
For each job title, provide **percentage**:
1. **Match Percentage** – How well this job title matches my profile.
Return only the highest percentage (Match) for each job title,and your response must in a single line of numbers separated by spaces and keep in mind  without any explaination info. For example:
Here are the highest percentages
95 85 30 65...
About Me:
**Babar Rehman**  &#10;**Senior Full-Stack Developer**   &#10;&#10;With over 8 years of experience in software development, I am a Senior Full-Stack Developer adept at building secure, scalable, and high-performance web applications. My expertise spans a diverse range of technologies including .NET Core, C#, ASP.NET, React, Angular, TypeScript, Python (Django, FastAPI), and cloud platforms like AWS and Azure. I specialize in developing complex backend systems, designing robust database architectures, and delivering seamless user experiences through dynamic, responsive front-end applications.  &#10;&#10;I have a strong background in cloud services, DevOps practices (CI/CD, Docker, Kubernetes), microservices architecture, and database optimization (SQL, NoSQL). I excel at leading cross-functional teams, optimizing application performance, and mentoring junior developers. I have a track record of delivering projects ahead of schedule by leveraging modern frameworks, cutting-edge development techniques, and efficient workflows. With a deep understanding of system architecture, design patterns (DDD, SOA), and security best practices (OAuth, JWT), I continuously drive innovation to meet complex project requirements while ensuring maintainable, scalable solutions.  &#10;&#10;Whether designing cloud-based solutions or implementing secure data pipelines, I thrive in fast-paced environments where I can contribute to all stages of the development lifecycle, from initial planning to deployment and maintenance.
Titles are :
Full-Stack Web Developer | Expert in End-to-End Solutions

Full-Stack Developer | React, Node.js & Database Integration Specialist

Versatile Full-Stack Engineer | Front-End to Back-End Architect

Full-Stack Web Developer | Building Scalable Apps from Concept to Deployment

Full-Stack Developer | Modern Web Tech & Cross-Platform Solutions

"""
while True:
    # query = input("\nWhat's on your mind? : ")
    input("What's are you minds today? :")
    if query.lower() in ["exit", "quit"]:
        break  # Exit the loop if user types "exit" or "quit"
    
    model_response = ask_query(query)
    print("\n")  # Ensure a new line after response
