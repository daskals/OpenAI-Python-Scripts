import requests
import os
from datetime import datetime
from openai import OpenAI

# Replace 'your_api_key_here' with your actual OpenAI API key
api_key = os.environ["OPENAI_API_KEY"]

headers = {
    'Authorization': f'Bearer {api_key}',
    'Content-Type': 'application/json',
    'OpenAI-Beta': 'assistants=v2'
}
client = OpenAI()

def create_vector_store(name):
    # Check if the vector store with the given name already exists
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

    # If not exists, create a new vector store
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


def print_vector_store_info(store_id):
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


def upload_files_to_vector_store(store_id, file_paths):
    # Ensure the file_paths list has 3 files or fewer
    if len(file_paths) > 3:
        print("Error: This function can only upload up to 3 files at a time.")
        return

    file_ids = []
    for file_path in file_paths:
        file_info = upload_file(file_path)
        if file_info:
            file_ids.append(file_info['id'])
        else:
            print(f"Failed to upload file: {file_path}")
            return

    batch_payload = {
        "file_ids": file_ids
    }

    response = requests.post(
        f'https://api.openai.com/v1/vector_stores/{store_id}/file_batches',
        headers=headers,
        json=batch_payload
    )

    if response.status_code == 200:
        batch_info = response.json()
        print("Files uploaded successfully to the vector store.")
        print(f"Batch ID: {batch_info['id']}")
        print(f"Status: {batch_info['status']}")
    else:
        print(f"Failed to create file batch. Status code: {response.status_code}, Error: {response.text}")




def upload_file(file_path):
    url = 'https://api.openai.com/v1/files'
    headers = {
        'Authorization': f'Bearer {api_key}',
    }
    files = {
        'file': (file_path, open(file_path, 'rb')),
        'purpose': (None, 'assistants'),
    }

    response = requests.post(url, headers=headers, files=files)

    if response.status_code == 200:
        file_info = response.json()
        print(f"File uploaded successfully. ID: {file_info['id']}, Filename: {file_info['filename']}")
        return file_info
    else:
        print(f"Failed to upload file. Status code: {response.status_code}, Error: {response.text}")
        return None


def list_files():
    url = 'https://api.openai.com/v1/files'
    headers = {
        'Authorization': f'Bearer {api_key}',
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        files = response.json()['data']
        if not files:
            print("No files found.")
        else:
            print("Files:")
            for file in files:
                print(f"ID: {file['id']}, Filename: {file['filename']}")
        return files
    else:
        print(f"Failed to list files. Status code: {response.status_code}, Error: {response.text}")
        return None


def delete_file(file_id):
    url = f'https://api.openai.com/v1/files/{file_id}'
    headers = {
        'Authorization': f'Bearer {api_key}',
    }

    response = requests.delete(url, headers=headers)

    if response.status_code == 200:
        print(f"File ID: {file_id} deleted successfully.")
    else:
        print(f"Failed to delete file. Status code: {response.status_code}, Error: {response.text}")


def delete_all_files():
    files = list_files()
    if files:
        for file in files:
            delete_file(file['id'])


def main():
    vector_store_name = "Green IoT Solutions"
    store_id, store_name = create_vector_store(vector_store_name)

    if store_id:

        file_path = "./Invoice_files/Invoice_1.pdf"  # Replace with your actual file path
        upload_file(file_path)
        list_files()
        delete_all_files()
        list_files()

        print_vector_store_info(store_id)
        # Example files list, replace with actual file objects
        file_paths = ['./Invoice_files/Invoice_1.pdf', './Invoice_files/Invoice_2.pdf']
        upload_files_to_vector_store(store_id, file_paths)
    # Uncomment the following lines to list or delete vector stores
    list_vector_stores()
    delete_all_vector_stores()


if __name__ == "__main__":
    main()
