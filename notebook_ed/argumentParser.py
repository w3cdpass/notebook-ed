import argparse

def ArgumentParser():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description='Convert .py files to .ipynb and delete the original .py files.')
    parser.add_argument('-r', '--root_dir', type=str, help='The root directory of your project')
    parser.add_argument('-f', '--file', type=str, help='Convert a specific .py file to .ipynb')
    parser.add_argument('--report', action='store_true', help='Report an issue with this tool')
    args  =  parser.parse_args()
    return args, parser