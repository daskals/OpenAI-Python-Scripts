#######################################################
#     Spyros Daskalakis                               #
#     Last Revision: 20/06/2024                       #
#     Python Version:  3.9                            #
#     Email: Daskalakispiros@gmail.com                #
#######################################################

import base64
import requests
import os
import openai

# Retrieve the OpenAI API key from the environment variables
openai_api_key= os.getenv("OPENAI_API_KEY")

# Check if the API key is retrieved correctly
if not openai_api_key:
    raise ValueError("API key not found. Please set the 'OPENAI_API_KEY' environment variable.")

# Function to encode the image
def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')

# Path to your image
image_path = "images/resistor.png"

# Getting the base64 string
base64_image = encode_image(image_path)

headers = {
  "Content-Type": "application/json",
  "Authorization": f"Bearer {openai_api_key}"
}

payload = {
  "model": "gpt-4o",
  "messages": [
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "GPT, your task is to identify the resistor on the picture. Analyze any image and give me final "
                  "resistor value in kOhms."
        },
        {
          "type": "image_url",
          "image_url": {
            "url": f"data:image/jpeg;base64,{base64_image}"
          }
        }
      ]
    }
  ],
  "max_tokens": 300
}

response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)

print(response.json())

# Parsing the response to extract the list of ingredients and quantities
response_json = response.json()
ingredients = response_json.get('choices', [{}])[0].get('message', {}).get('content', 'No ingredients found')

# Print the list of ingredients and quantities
print("Resistor Value:")
print(ingredients)


