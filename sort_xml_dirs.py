import os
import shutil
# Define the source directory containing all the folders
source_dir = '/Users/brendanbrady/Downloads/AutoSlideGenDataset/dataset'
# Define the destination directories for the first and second XML files
first_xml_dir = '/Users/brendanbrady/Documents/GitHub/CS4120final/papers'
second_xml_dir = '/Users/brendanbrady/Documents/GitHub/CS4120final/slides'
# Create destination directories if they don’t exist
os.makedirs(first_xml_dir, exist_ok=True)
os.makedirs(second_xml_dir, exist_ok=True)
# Iterate through each folder in the source directory
for folder_name in os.listdir(source_dir):
    folder_path = os.path.join(source_dir, folder_name)
    # Check if the item in the source directory is a folder
    if os.path.isdir(folder_path):
        # List all files in the current folder
        files = os.listdir(folder_path)
        # Filter out XML files
        xml_files = [file for file in files if file.endswith('.xml')]
        # Make sure there are exactly two XML files in the folder
        if len(xml_files) == 2:
            # Move the first XML file to the first_xml_dir
            first = xml_files[0]
            second = xml_files[1]
            if first.startswith('slide'):
                first = xml_files[1]
                second = xml_files[0]
            first_xml_file = os.path.join(folder_path, first)
            shutil.move(first_xml_file, os.path.join(first_xml_dir, folder_name + first))
            # Move the second XML file to the second_xml_dir
            second_xml_file = os.path.join(folder_path, second)
            shutil.move(second_xml_file, os.path.join(second_xml_dir, folder_name + second))
            print(f"Moved XML files from {folder_name} folder.")
print("Process completed.")