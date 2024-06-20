#######################################################
#     Spyros Daskalakis                               #
#     Last Revision: 11/01/2024                       #
#     Python Version:  3.9                            #
#     Email: Daskalakispiros@gmail.com                #
#######################################################

# Documentation: https://platform.openai.com/docs/guides/text-generation
# Import necessary libraries
import requests
import os
import base64

# Retrieve the OpenAI API key from the environment variables
openai_api_key = os.environ.get("OPENAI_API_KEY")

# URL for the OpenAI API
URL = "https://api.openai.com/v1/chat/completions"


# Function to encode the image in base64 format
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')


# Path to your image
image_path = "images/pcb.jpg"
# Getting the base64 encoded string of the image
base64_image = encode_image(image_path)

# Headers for the API request including the Content-Type and Authorization with API key
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {openai_api_key}"
}

# Modify the payload for electronic component identification
payload = {
    "model": "gpt-4-vision-preview",
    "messages": [
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "GPT, your task is to analyze the provided image and identify any electronic components. "
                            "Please list each identifiable component with estimated names"
                },
                {
                    "type": "image_url",
                    "image_url": f"data:image/jpeg;base64,{base64_image}"
                }
            ]
        }
    ],
    "max_tokens": 300
}

# Sending the POST request to the OpenAI API to identify electronic components
response = requests.post(URL, headers=headers, json=payload)

# Parsing the response to extract the list of electronic components
response_json = response.json()
components = response_json.get('choices', [{}])[0].get('message', {}).get('content', 'No components found')

# Print the list of identified electronic components
print("Identified Electronic Components:")
print(components)
