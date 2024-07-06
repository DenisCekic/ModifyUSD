import os
from pxr import Usd

def convert_usd_to_usda(input_path, output_path):
    # Open the USD stage
    stage = Usd.Stage.Open(input_path)
    if not stage:
        print(f"Could not open USD file: {input_path}")
        return

    # Export the stage to the USDA file format
    stage.Export(output_path)
    print(f"Converted {input_path} to {output_path}")

def convert_usdc_to_usda(input_path, output_path):
    # Open the USDC stage
    stage = Usd.Stage.Open(input_path)
    if not stage:
        print(f"Could not open USDC file: {input_path}")
        return

    # Export the stage to the USDA file format
    stage.Export(output_path)
    print(f"Converted {input_path} to {output_path}")

def process_files(input_dir, output_dir, processed_files, conversion_function, extension_check):
    for file_name in os.listdir(input_dir):
        if file_name.endswith(extension_check) and file_name not in processed_files:
            input_path = os.path.join(input_dir, file_name)
            base_name = os.path.splitext(file_name)[0]  # Remove the file extension
            output_path = os.path.join(output_dir, base_name + '.usda')
            conversion_function(input_path, output_path)
            processed_files.add(file_name)

def main():
    script_dir = os.path.dirname(os.path.realpath(__file__))
    input_dir = os.path.join(script_dir, 'input')
    output_dir = os.path.join(script_dir, 'output')
    usda_dir = os.path.join(output_dir, 'usda')
    usdCa_dir = os.path.join(output_dir, 'usdCa')

    if not os.path.exists(usda_dir):
        os.makedirs(usda_dir)
    
    if not os.path.exists(usdCa_dir):
        os.makedirs(usdCa_dir)

    processed_files = set()

    # Process .usd to .usda and save to 'output/usda'
    process_files(input_dir, usda_dir, processed_files, convert_usd_to_usda, '.usd')

    # Process .usdc to .usda and save to 'output/usdCa'
    process_files(input_dir, usdCa_dir, processed_files, convert_usdc_to_usda, '.usdc')

if __name__ == "__main__":
    main()
