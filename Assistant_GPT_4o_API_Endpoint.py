#######################################################
#     Spyros Daskalakis                               #
#     Last Revision: 20/06/2024                       #
#     Python Version:  3.9                            #
#     Email: Daskalakispiros@gmail.com                #
#######################################################

# Import necessary libraries
import requests
import os


# Retrieve the OpenAI API key from the environment variables
openai_api_key = os.environ.get("OPENAI_API_KEY"),

# Print the API key to verify its retrieval (optional, consider security)
print(openai_api_key[0])

# URL for the OpenAI API
URL = "https://api.openai.com/v1/chat/completions"

# Headers for the API request including the Content-Type and Authorization with API key
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {openai_api_key[0]}"
}

# Payload for the API request with details like model, messages, and parameters for the response
payload = {
    "model": "gpt-4o",
    "messages": [{"role": "user", "content": "What is the first computer in the world?"}],
    "temperature": 1.0,
    "top_p": 1.0,
    "n": 1,
    "stream": False,
    "presence_penalty": 0,
    "frequency_penalty": 0,
}

# Send the POST request to the API
response = requests.post(URL, headers=headers, json=payload, stream=False)

# Convert the response to JSON format
response_json = response.json()

# Pretty print the JSON response for readability
# print(json.dumps(response_json, indent=4))

# Extracting the content from the response
content = response_json['choices'][0]['message']['content'] if 'choices' in response_json and len(response_json['choices']) > 0 else "No content found"

# Print the extracted content
print(content)