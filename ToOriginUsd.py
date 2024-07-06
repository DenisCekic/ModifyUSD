import os
from pxr import Usd

def usda_to_usd(input_path, output_path):
    # Open the USDA stage
    stage = Usd.Stage.Open(input_path)
    if not stage:
        print(f"Could not open USDA file: {input_path}")
        return

    # Export the stage to the USD file format
    stage.Export(output_path)
    print(f"Converted {input_path} to {output_path}")

def process_files(input_dir, output_dir, processed_files):
    for file_name in os.listdir(input_dir):
        if file_name.endswith('.usda') and file_name not in processed_files:
            input_path = os.path.join(input_dir, file_name)
            output_path = os.path.join(output_dir, file_name[:-1])  # Remove the 'a' at the end
            usda_to_usd(input_path, output_path)
            processed_files.add(file_name)

def main():
    script_dir = os.path.dirname(os.path.realpath(__file__))
    output_dir = os.path.join(script_dir, 'output')
    fixed_dir = os.path.join(script_dir, 'fixed')
    usda_output_dir = os.path.join(output_dir, 'usda')
    usdCa_output_dir = os.path.join(output_dir, 'usdCa')
    fixed_usd_dir = os.path.join(fixed_dir, 'usd')
    fixed_usdC_dir = os.path.join(fixed_dir, 'usdC')

    if not os.path.exists(fixed_usd_dir):
        os.makedirs(fixed_usd_dir)
    
    if not os.path.exists(fixed_usdC_dir):
        os.makedirs(fixed_usdC_dir)

    processed_files = set()

    # Process .usda files in 'output/usda' and save to 'fixed/usd'
    process_files(usda_output_dir, fixed_usd_dir, processed_files)

    # Process .usda files in 'output/usdCa' and save to 'fixed/usdC'
    process_files(usdCa_output_dir, fixed_usdC_dir, processed_files)

if __name__ == "__main__":
    main()
