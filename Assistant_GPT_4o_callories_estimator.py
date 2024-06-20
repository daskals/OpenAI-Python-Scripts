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
openai_api_key = os.getenv("OPENAI_API_KEY")

# Check if the API key is retrieved correctly
if not openai_api_key:
    raise ValueError("API key not found. Please set the 'OPENAI_API_KEY' environment variable.")

# Function to encode the image to base64 format
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

# Path to the image to be analyzed
image_path = "images/food_plate.jpg"

# Encode the image to base64 format
base64_image = encode_image(image_path)

# Set the headers for the API request
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {openai_api_key}"
}

# Prepare the payload for the first API request to identify ingredients and quantities
payload = {
    "model": "gpt-4o",
    "messages": [
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "GPT, your task is to identify the content of the plate of food with precision. Analyze any image of the plate and detect all the different ingredients. Respond strictly with the list of the content and the quantities (do an estimation in grams)."
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

# Send the first POST request to the OpenAI API
response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)

# Parse the response to extract the list of ingredients and quantities
response_json = response.json()
ingredients = response_json.get('choices', [{}])[0].get('message', {}).get('content', 'No ingredients found')

# Print the identified ingredients and quantities
print("Identified Ingredients and Quantities:")
print(ingredients)

# Prepare the payload for the second API request to estimate calories
second_payload = {
    "model": "gpt-4o",
    "messages": [
        {
            "role": "user",
            "content": f"Based on this list of ingredients and quantities, estimate the calories for each ingredient and the total calories for the plate: {ingredients}. Respond strictly with the list of the calories and total calories of the plate"
        }
    ],
    "max_tokens": 300
}

# Send the second POST request to the OpenAI API for calorie estimation
second_response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=second_payload)

# Parse the response to extract the calorie estimations
second_response_json = second_response.json()
calorie_estimations = second_response_json.get('choices', [{}])[0].get('message', {}).get('content', 'Calorie estimation not found')

# Print the calorie estimations
print("\nCalorie Estimations:")
print(calorie_estimations)
