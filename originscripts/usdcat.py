import sys
from pxr import Usd

def usdcat(input_path, output_path):
    # Open the USD stage
    stage = Usd.Stage.Open(input_path)
    if not stage:
        print(f"Could not open USD file: {input_path}")
        return

    # Export the stage to the output path
    stage.Export(output_path)
    print(f"Converted {input_path} to {output_path}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python usdcat_script.py <input_usd_file> <output_usda_file>")
    else:
        input_usd_file = sys.argv[1]
        output_usda_file = sys.argv[2]
        usdcat(input_usd_file, output_usda_file)