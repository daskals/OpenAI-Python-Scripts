#######################################################
#     Spyros Daskalakis                               #
#     Last Revision: 20/06/2024                       #
#     Python Version:  3.9                            #
#     Email: Daskalakispiros@gmail.com                #
#######################################################

import requests
import os
from datetime import datetime

# Retrieve the OpenAI API key from environment variables
api_key = os.environ["OPENAI_API_KEY"]

# Define the headers for the API requests, including the API key and content type
headers = {
    'Authorization': f'Bearer {api_key}',
    'Content-Type': 'application/json',
    'OpenAI-Beta': 'assistants=v2'
}


def create_vector_store(name):
    """
    Create a vector store with the given name if it does not already exist.

    Args:
    name (str): The name of the vector store to create.

    Returns:
    tuple: The ID and name of the created or existing vector store, or None if creation failed.
    """
    # Check if a vector store with the given name already exists
    response = requests.get('https://api.openai.com/v1/vector_stores', headers=headers)
    if response.status_code == 200:
        vector_stores = response.json()
        for store in vector_stores['data']:
            if store['name'] == name:
                print(f"Vector store '{name}' already exists. ID: {store['id']}")
                return store['id'], store['name']
    else:
        print(f"Failed to retrieve vector stores. Status code: {response.status_code}, Error: {response.text}")
        return None

    # If the vector store does not exist, create a new one
    create_payload = {
        "name": name
    }

    response = requests.post('https://api.openai.com/v1/vector_stores', headers=headers, json=create_payload)
    if response.status_code == 200:
        store = response.json()
        store_id = store.get('id')
        store_name = store.get('name')
        print(f"Vector store created successfully. ID: {store_id}, Name: {store_name}")
        return store_id, store_name
    else:
        print(f"Failed to create vector store. Status code: {response.status_code}, Error: {response.text}")
        return None


def list_vector_stores():
    """
    List all vector stores available in the OpenAI account.
    """
    response = requests.get('https://api.openai.com/v1/vector_stores', headers=headers)
    if response.status_code == 200:
        vector_stores = response.json()
        if not vector_stores['data']:
            print("Empty")
        else:
            print("Vector Stores:")
            for store in vector_stores['data']:
                print(f"ID: {store['id']}, Name: {store['name']}")
    else:
        print(f"Failed to retrieve vector stores. Status code: {response.status_code}, Error: {response.text}")


def delete_all_vector_stores():
    """
    Delete all vector stores in the OpenAI account.
    """
    response = requests.get('https://api.openai.com/v1/vector_stores', headers=headers)
    if response.status_code == 200:
        vector_stores = response.json()
        for store in vector_stores['data']:
            delete_response = requests.delete(f"https://api.openai.com/v1/vector_stores/{store['id']}", headers=headers)
            if delete_response.status_code == 200:
                print(f"Vector store '{store['name']}' deleted successfully.")
            else:
                print(
                    f"Failed to delete vector store '{store['name']}'. Status code: {delete_response.status_code}, Error: {delete_response.text}")
    else:
        print(
            f"Failed to retrieve vector stores for deletion. Status code: {response.status_code}, Error: {response.text}")


def delete_vector_store(store_id):
    """
    Delete a specific vector store by its ID.

    Args:
    store_id (str): The ID of the vector store to delete.
    """
    delete_response = requests.delete(f"https://api.openai.com/v1/vector_stores/{store_id}", headers=headers)
    if delete_response.status_code == 200:
        print(f"Vector store with ID '{store_id}' deleted successfully.")
    else:
        print(
            f"Failed to delete vector store with ID '{store_id}'. Status code: {delete_response.status_code}, Error: {delete_response.text}")


def print_vector_store_info(store_id):
    """
    Print detailed information about a specific vector store.

    Args:
    store_id (str): The ID of the vector store to retrieve information for.
    """
    response = requests.get(f'https://api.openai.com/v1/vector_stores/{store_id}', headers=headers)
    if response.status_code == 200:
        store_info = response.json()
        created_at = datetime.fromtimestamp(store_info.get('created_at', 0)).strftime('%Y-%m-%d %H:%M:%S')
        usage_mb = store_info.get('usage_bytes', 0) / (1024 * 1024)

        print(f"Vector Store ID: {store_info['id']}")
        print(f"Name: {store_info['name']}")
        print(f"Number of files: {store_info.get('num_files', 'N/A')}")
        print(f"Usage (MB): {usage_mb:.2f}")
        print(f"Created At: {created_at}")
        print(f"Status: {store_info.get('status', 'N/A')}")
        print(f"Last Error: {store_info.get('last_error', 'N/A')}")
    else:
        print(f"Failed to retrieve vector store info. Status code: {response.status_code}, Error: {response.text}")


def main():
    """
    Main function to create a vector store and print its information.
    """
    vector_store_name = "Green IoT Solutions"
    store_id, store_name = create_vector_store(vector_store_name)
    if store_id:
        print_vector_store_info(store_id)
        # Example usage of deleting a specific vector store
        delete_vector_store(store_id)

    # Uncomment the following lines to list or delete vector stores
    list_vector_stores()
    delete_all_vector_stores()


if __name__ == "__main__":
    main()
