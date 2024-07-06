import sys
from pxr import Usdviewq

def usdview(input_path):
    app = Usdviewq.UsdviewApp(launchArgs=[input_path])
    app.Run()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python usd_viewer.py <input_usd_file>")
    else:
        input_usd_file = sys.argv[1]
        usdview(input_usd_file)
