import os
import nbformat
from nbformat import v4
import logging
import time
import sys
from colorama import init, Fore


# Initialize colorama
init()

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(message)s')

file_count = 0

def delete_file(file_path):
    """Delete a file if it exists."""
    try:
        if os.path.exists(file_path):
            os.remove(file_path)
            global file_count
            file_count += 1
            show_animation(file_count)
    except Exception as e:
        logging.error(f'Failed to delete {file_path}: {e}')

def convert_py_to_ipynb(py_file_path):
    """Convert a .py file to a .ipynb file."""
    ipynb_file_path = os.path.splitext(py_file_path)[0] + '.ipynb'
    try:
        if os.path.exists(ipynb_file_path):
            logging.info(f'{Fore.RED}INFO - file already exists with {ipynb_file_path}{Fore.RESET}')
            return
        
        with open(py_file_path, 'r', encoding='utf-8') as py_file:
            code = py_file.read()
        
        notebook = v4.new_notebook()
        notebook.cells.append(v4.new_code_cell(code))
        
        with open(ipynb_file_path, 'w', encoding='utf-8') as ipynb_file:
            nbformat.write(notebook, ipynb_file)
        
        delete_file(py_file_path)
        show_success_animation(ipynb_file_path)
    except Exception as e:
        logging.error(f'{Fore.RED}ERROR - Failed to convert {py_file_path} to {ipynb_file_path}: {e}{Fore.RESET}')

def process_directory(root_dir):
    from .ignoreFIles import ignoreFile
    """Process all .py files in a directory, converting them to .ipynb and deleting the .py files."""
    ignore_dirs = ignoreFile
    for subdir, _, files in os.walk(root_dir):
        if any(ignored in subdir for ignored in ignore_dirs):
            continue
        for file in files:
            if file.endswith('.py'):
                py_file_path = os.path.join(subdir, file)
                if file == '__init__.py':
                    delete_file(os.path.splitext(py_file_path)[0] + '.ipynb')
                else:
                    convert_py_to_ipynb(py_file_path)

def convert_single_file(file_path):
    """Convert a single .py file to .ipynb."""
    if file_path.endswith('.py'):
        convert_py_to_ipynb(file_path)
    else:
        logging.error(f'{Fore.RED}INFO - only convert .py to .ipynb not other: {file_path}{Fore.RESET}')

def report_issue():
    """Print instructions for reporting an issue."""
    print("To report an issue, please visit: https://github.com/w3cdpass/notebook-ed/issues")

def show_animation(count):
    """Show ASCII animation while converting."""
    frames = [
        f"{Fore.GREEN}•{Fore.RED}•{Fore.GREEN}  •",
        # f"{Fore.GREEN}• {Fore.GREEN}•{Fore.GREEN} •",
        f"{Fore.GREEN}• {Fore.RED}•{Fore.GREEN} •",
        f"{Fore.GREEN}•{Fore.GREEN} •{Fore.GREEN} •",
        f"{Fore.GREEN}•  {Fore.RED}•{Fore.GREEN}•",
        f"{Fore.GREEN}•{Fore.RED} •{Fore.GREEN} •",
    ]
    for frame in frames:
        sys.stdout.write(f"\r{frame}  Converting ({count})")
        sys.stdout.flush()
        time.sleep(0.04)

def show_success_animation(file_path):
    """Show success message with animation."""
    sys.stdout.write(f"\r{Fore.GREEN}[•] Conversion complete: {file_path}{Fore.RESET}")
    sys.stdout.flush()

def main():
    
    from .argumentParser import ArgumentParser
    args, parser = ArgumentParser()

    if args.report:
        report_issue()
    elif args.file:
        show_animation(file_count)
        convert_single_file(args.file)
        print(f"\nRoot directory: {args.file}")
    elif not args.root_dir:
        parser.print_help()
    elif not os.path.exists(args.root_dir):
        logging.error(f'{Fore.RED}INFO - The provided directory or file does not exist: {args.root_dir}{Fore.RESET}')
    elif os.path.isfile(args.root_dir):
        show_animation(file_count)
        convert_single_file(args.root_dir)
        print(f"\nRoot directory: {args.root_dir}")
    else:
        show_animation(file_count)
        process_directory(args.root_dir)
        print(f"\nRoot directory: {args.root_dir}")

if __name__ == '__main__':
    main()
