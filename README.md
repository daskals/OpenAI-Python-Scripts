
# OpenAI API Python Project

This project demonstrates the use of the OpenAI API with Python. It includes various scripts showcasing different capabilities of the OpenAI API, including text generation, image analysis, and more.

## Overview

The purpose of this project is to explore and utilize the OpenAI API to perform a variety of tasks using Python. Each script is designed to demonstrate a different functionality of the API.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Environment Variable Setup](#environment-variable-setup)
- [Scripts](#scripts)
  - [Assistant_GPT_4o_API_Endpoint.py](#Assistant_GPT_4o_API_Endpointpy)
  - [Assistant_GPT_4o_API_no_stream.py](#Assistant_GPT_4o_API_no_streampy)
  - [Assistant_GPT_4o_API_resistor_calculator.py](#Assistant_GPT_4o_API_resistor_calculatorpy)
  - [Assistant_GPT_4o_API_stream.py](#Assistant_GPT_4o_API_streampy)
  - [Assistant_GPT_4o_callories_estimator.py](#Assistant_GPT_4o_callories_estimatorpy)
  - [Assistant_GPT_4o_Component_finder.py](#Assistant_GPT_4o_Component_finderpy)
  - [Assistant_GPT_4o_image_identifier.py](#Assistant_GPT_4o_image_identifierpy)
  - [Vector_Store_and_files_Assistant.py](#Vector_Store_and_files_Assistantpy)
  - [Vector_store_API_EndPoint.py](#Vector_store_API_EndPointpy)
  - [Vector_store_and_files_API_Endpoint.py](#Vector_store_and_files_API_Endpointpy)

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/openai-api-python-project.git
    cd openai-api-python-project
    ```

2. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Environment Variable Setup

To use the OpenAI API, you need to set up an environment variable for your API key. This key is required for authentication when making requests to the OpenAI API.

### On Linux/MacOS

Open your terminal and run the following command:

```sh
export OPENAI_API_KEY='your-api-key'
```

To make this change permanent, add the above line to your `~/.bashrc` or `~/.zshrc` file.

### On Windows

Open Command Prompt or PowerShell and run the following command:

```sh
setx OPENAI_API_KEY "your-api-key"
```

Alternatively, you can set the environment variable through the System Properties:

1. Open the Start Search, type in "env", and select "Edit the system environment variables".
2. In the System Properties window, click on the "Environment Variables" button.
3. Click "New" to create a new environment variable.
4. Enter `OPENAI_API_KEY` as the name and your actual API key as the value.
5. Click OK to apply the changes.

## Usage

Each script in the project directory demonstrates a different use case for the OpenAI API. You can run each script individually to see how it interacts with the API.

## Scripts

### Assistant_GPT_4o_API_Endpoint.py

This script demonstrates a basic interaction with the OpenAI API. It sends a request to the API with a user query and prints the response.

### Assistant_GPT_4o_API_no_stream.py

This script creates an OpenAI assistant that can solve math equations. It demonstrates how to handle a complete interaction in a single API call without streaming responses.

### Assistant_GPT_4o_API_resistor_calculator.py

This script analyzes an image of a resistor and calculates its value. It showcases the use of image data with the OpenAI API to perform analysis and provide detailed results.

### Assistant_GPT_4o_API_stream.py

This script demonstrates the use of the streaming feature of the OpenAI API. It allows for real-time response handling and showcases how to implement an event handler to process streamed data.

### Assistant_GPT_4o_callories_estimator.py

This script estimates the calories in a plate of food based on an image. It first identifies the ingredients and quantities, and then calculates the calorie content of each ingredient and the total meal.

### Assistant_GPT_4o_Component_finder.py

This script analyzes an image of a PCB (Printed Circuit Board) and identifies the electronic components present. It demonstrates the ability of the OpenAI API to process and analyze image data to identify objects.

### Assistant_GPT_4o_image_identifier.py

This script identifies the contents of an image, such as food items on a plate. It encodes the image, sends it to the OpenAI API, and prints the identified items along with their descriptions.

### Vector_Store_and_files_Assistant.py
This script demonstrates how to create an assistant for analyzing invoice files using vector stores. It shows how to upload files, create vector stores, and handle file searches within the assistant.

### Vector_store_API_EndPoint.py
This script provides functions for managing vector stores, including creating, listing, and deleting vector stores. It also includes functionality for uploading files to vector stores.

### Vector_store_and_files_API_Endpoint.py
This script combines the functionality of managing vector stores and handling file uploads. It demonstrates how to create vector stores, upload files, and manage file batches within a vector store.

---

For any questions or support, feel free to contact me at Daskalakispiros@gmail.com.

Happy coding!
