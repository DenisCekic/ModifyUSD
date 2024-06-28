import sys
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

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python usda_to_usd.py <input_usda_file> <output_usd_file>")
    else:
        input_usda_file = sys.argv[1]
        output_usd_file = sys.argv[2]
        usda_to_usd(input_usda_file, output_usd_file)
