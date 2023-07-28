from huggingface_hub import hf_hub_download
import os
import shutil

# Define the desired filename
output_filename = "amandamodel.bin"

# Download the model
downloaded_model_path = hf_hub_download(
    repo_id="TheBloke/vicuna-7B-v1.3-GGML",
    filename="vicuna-7b-v1.3.ggmlv3.q4_0.bin",
)

# Create the new file path with the desired filename
new_model_path = os.path.join(os.path.dirname(downloaded_model_path), output_filename)

# Rename the downloaded model file
os.rename(downloaded_model_path, new_model_path)

# Move the file to the current directory
current_directory = os.getcwd()
destination_path = os.path.join(current_directory, output_filename)
shutil.move(new_model_path, destination_path)

print("Model downloaded and saved as:", destination_path)
