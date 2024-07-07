import os
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter.scrolledtext import ScrolledText
from pxr import Usd
import sys
import io

class ConsoleOutput(io.StringIO):
    def __init__(self, console_widget):
        super().__init__()
        self.console_widget = console_widget

    def write(self, s):
        self.console_widget.insert(tk.END, s)
        self.console_widget.see(tk.END)
        self.console_widget.update_idletasks()

def convert_usd_to_usda(input_path, output_path):
    stage = Usd.Stage.Open(input_path)
    if not stage:
        print(f"Could not open USD file: {input_path}")
        return
    stage.Export(output_path)
    print(f"Converted {input_path} to {output_path}")

def convert_usdc_to_usda(input_path, output_path):
    stage = Usd.Stage.Open(input_path)
    if not stage:
        print(f"Could not open USDC file: {input_path}")
        return
    stage.Export(output_path)
    print(f"Converted {input_path} to {output_path}")

def usda_to_usd(input_path, output_path):
    stage = Usd.Stage.Open(input_path)
    if not stage:
        print(f"Could not open USDA file: {input_path}")
        return
    stage.Export(output_path)
    print(f"Converted {input_path} to {output_path}")

def process_files(input_dir, output_dir, processed_files, conversion_function, extension_check, output_extension):
    print(f"Processing files in {input_dir}, output to {output_dir}")
    for file_name in os.listdir(input_dir):
        if file_name.endswith(extension_check) and file_name not in processed_files:
            input_path = os.path.join(input_dir, file_name)
            base_name = os.path.splitext(file_name)[0]
            output_path = os.path.join(output_dir, base_name + output_extension)
            print(f"Converting {input_path} to {output_path}")
            conversion_function(input_path, output_path)
            processed_files.add(file_name)
            print(f"Processed {file_name}")
        else:
            print(f"Skipping {file_name}, either it doesn't end with {extension_check} or it is already processed")

def main_processing():
    script_dir = os.path.dirname(os.path.realpath(__file__))
    input_dir = os.path.join(script_dir, 'input')
    output_dir = os.path.join(script_dir, 'output')
    usda_dir = os.path.join(output_dir, 'usda')
    usdCa_dir = os.path.join(output_dir, 'usdCa')

    if not os.path.exists(usda_dir):
        os.makedirs(usda_dir)
    
    if not os.path.exists(usdCa_dir):
        os.makedirs(usdCa_dir)

    processed_files_usda = set()
    processed_files_usdCa = set()

    process_files(input_dir, usda_dir, processed_files_usda, convert_usd_to_usda, '.usd', '.usda')
    process_files(input_dir, usdCa_dir, processed_files_usdCa, convert_usdc_to_usda, '.usdc', '.usda')

def main_conversion():
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

    processed_files_usda = set()
    processed_files_usdCa = set()

    print(f"Converting .usda to .usd in {usda_output_dir} to {fixed_usd_dir}")
    process_files(usda_output_dir, fixed_usd_dir, processed_files_usda, usda_to_usd, '.usda', '.usd')
    
    print(f"Converting .usda to .usd in {usdCa_output_dir} to {fixed_usdC_dir}")
    process_files(usdCa_output_dir, fixed_usdC_dir, processed_files_usdCa, usda_to_usd, '.usda', '.usd')

    # Check if the directory contains files
    if not os.listdir(usdCa_output_dir):
        print(f"No files found in {usdCa_output_dir}")
    else:
        print(f"Files found in {usdCa_output_dir}: {os.listdir(usdCa_output_dir)}")

class USDConverterApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("USD to USDA Converter")
        self.geometry("1000x800")

        self.text_widget = ScrolledText(self, wrap=tk.NONE)
        self.text_widget.pack(expand=1, fill=tk.BOTH)

        button_frame = tk.Frame(self)
        button_frame.pack(side=tk.TOP, fill=tk.X)

        self.open_button = tk.Button(button_frame, text="Open .usda File", command=self.open_file)
        self.open_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.save_button = tk.Button(button_frame, text="Save File", command=self.save_file)
        self.save_button.pack(side=tk.LEFT, padx=5, pady=5)

        center_frame = tk.Frame(button_frame)
        center_frame.pack(side=tk.LEFT, padx=5, pady=5, expand=True)

        self.process_button = tk.Button(center_frame, text="Convert To USD-A", command=main_processing)
        self.process_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.convert_button = tk.Button(center_frame, text="Re-Convert To USD", command=main_conversion)
        self.convert_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.wrap_button = tk.Button(button_frame, text="Toggle Word Wrap", command=self.toggle_word_wrap)
        self.wrap_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.console_output = ScrolledText(self, wrap=tk.WORD, height=10)
        self.console_output.pack(expand=0, fill=tk.X)
        self.console_output.insert(tk.END, "Console log...\n")

        self.clear_console_button = tk.Button(self, text="Clear Console Log", command=self.clear_console)
        self.clear_console_button.pack(side=tk.BOTTOM, padx=5, pady=5)

        sys.stdout = ConsoleOutput(self.console_output)
        sys.stderr = ConsoleOutput(self.console_output)

        self.word_wrap = False

    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("USDA files", "*.usda")])
        if file_path:
            with open(file_path, 'r') as file:
                content = file.read()
            self.text_widget.delete(1.0, tk.END)
            self.text_widget.insert(tk.END, content)
            self.current_file_path = file_path

    def save_file(self):
        if hasattr(self, 'current_file_path'):
            with open(self.current_file_path, 'w') as file:
                content = self.text_widget.get(1.0, tk.END)
                file.write(content)
            messagebox.showinfo("Save File", "File saved successfully!")
        else:
            messagebox.showwarning("Save File", "No file is currently open.")

    def toggle_word_wrap(self):
        self.word_wrap = not self.word_wrap
        if self.word_wrap:
            self.text_widget.config(wrap=tk.WORD)
        else:
            self.text_widget.config(wrap=tk.NONE)

    def clear_console(self):
        self.console_output.delete(1.0, tk.END)

if __name__ == "__main__":
    app = USDConverterApp()
    app.mainloop()
