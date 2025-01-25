from azure.storage.blob import BlobServiceClient, ContainerClient
import os, sys


username = "ninad"


# Define the connection string and container name
connection_string = "DefaultEndpointsProtocol=https;AccountName=dspcoderproblem;AccountKey=zsNAztjSrZKiMLq9lAmAL1qYC3BODBJjvxW06gE5U9Wt2P+rodzQWkxrPHTLi2flqZP5H+sfXim9+AStx7/JAg==;EndpointSuffix=core.windows.net"

# Create a BlobServiceClient
blob_service_client = BlobServiceClient.from_connection_string(connection_string)

def push_to_container(folder_name, local_path, container_name="usercode-bucket"):
    """
    Uploads files from a local directory to an Azure Blob Storage container.
    
    :param container_name: Name of the Azure Blob container.
    :param folder_name: The folder path in the container where files will be uploaded.
    :param local_path: The local directory containing the files to upload.
    """
    container_client = blob_service_client.get_container_client(container_name)
    
    for root, dirs, files in os.walk(local_path):
        for file in files:
            if ".DS_Store" in file or ".git" in file or ".a" in file or ".o" in file or ".pyc" in file or ".out" in file or not ".md" in file:
                continue
            local_file_path = os.path.join(root, file)
            relative_path = os.path.relpath(local_file_path, local_path)
            blob_path = os.path.join(folder_name, relative_path).replace("\\", "/")  # Ensure compatibility with blob paths
            
            print(f"Uploading {local_file_path} to {blob_path} in {container_name}...")
            
            # Get a blob client
            blob_client = container_client.get_blob_client(blob_path)
            
            # Upload the file
            with open(local_file_path, "rb") as data:
                blob_client.upload_blob(data, overwrite=True)
            
            print(f"Uploaded: {local_file_path} to {blob_path}")

    print("Upload complete.")

def upload_all_folders(base_path, username, container_name="problem-bucket"):
    """
    Iterates over all folders in the base path and uploads each folder's contents to the blob container.
    
    :param base_path: The root path containing subfolders to upload.
    :param username: The username, used in folder naming on the blob container.
    :param container_name: Name of the Azure Blob container.
    """
    for folder_name in os.listdir(base_path):
        if folder_name == "10101_reverse_linked_list":    
            local_folder_path = os.path.join(base_path, folder_name)
            if os.path.isdir(local_folder_path):  # Check if it's a directory
                blob_folder_name = folder_name
                print(f"Processing folder: {local_folder_path} -> Blob path: {blob_folder_name}")
                push_to_container(folder_name=blob_folder_name, local_path=local_folder_path, container_name=container_name)

###############
# driver code #
###############

# Define the base path where all user folders are stored
base_path = f"/Users/ninad/dspcoder/automation/"

# Upload all folders under the user's localSave directory
upload_all_folders(base_path=base_path, username=username)