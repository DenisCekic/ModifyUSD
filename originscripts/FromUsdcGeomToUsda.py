import os
import sys
from pxr import Usd

def usdc_to_usda(input_path, output_path):
    # Open the USDC stage
    stage = Usd.Stage.Open(input_path)
    if not stage:
        print(f"Could not open USDC file: {input_path}")
        return

    # Export the stage to the USDA file format
    stage.Export(output_path)
    print(f"Converted {input_path} to {output_path}")

def get_processed_files():
    processed_files_path = 'processed_usdc_files.txt'
    if not os.path.exists(processed_files_path):
        return set()
    with open(processed_files_path, 'r') as file:
        return set(line.strip() for line in file)

def save_processed_file(file_name):
    with open('processed_usdc_files.txt', 'a') as file:
        file.write(file_name + '\n')

def main():
    script_dir = os.path.dirname(os.path.realpath(__file__))
    input_dir = os.path.join(script_dir, 'input')
    output_dir = os.path.join(script_dir, 'output')

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    processed_files = get_processed_files()

    for file_name in os.listdir(input_dir):
        if file_name.endswith('.usdc') and file_name not in processed_files:
            input_path = os.path.join(input_dir, file_name)
            output_path = os.path.join(output_dir, file_name[:-1] + 'a')  # Change the extension to .usda
            usdc_to_usda(input_path, output_path)
            save_processed_file(file_name)

if __name__ == "__main__":
    main()
