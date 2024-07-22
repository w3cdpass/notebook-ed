# py2nb

A tool to convert `.py` files to `.ipynb` files and delete the original `.py` files. This tool makes it easy to convert Python scripts into Jupyter Notebooks for easy sharing and collaboration.

![Python](https://img.shields.io/badge/python-v3.8+-blue.svg?logo=python)
![Pip Install](https://img.shields.io/badge/pip%20install-py2nb-green)

## Project Insights

`py2nb` is designed to streamline the process of converting Python scripts into Jupyter Notebooks. It is particularly useful for educators, data scientists, and developers who need to present their Python code in a more interactive format. 

### Features

- Converts `.py` files to `.ipynb` files
- Deletes the original `.py` files after conversion
- Processes directories to batch convert multiple files
- Simple command-line interface for ease of use

## How to Start with Source Code

To start using `py2nb`, follow these steps:

1. **Clone the Repository**

    ```sh
    git clone https://github.com/yourusername/py2nb.git
    cd py2nb
    ```

2. **Create a Virtual Environment**

    ```sh
    python -m venv py2nb_env
    ```

3. **Activate the Virtual Environment**

    - On Windows:
        ```sh
        py2nb_env\Scripts\activate
        ```
    - On macOS/Linux:
        ```sh
        source py2nb_env/bin/activate
        ```

4. **Install Dependencies**

    ```sh
    pip install -r requirements.txt
    ```

5. **Run the Script**

    ```sh
    python -m py2nb -r <root_directory>  # To convert all .py files in a directory
    python -m py2nb -f <file_path>       # To convert a single .py file
    ```

## How to Contribute

We welcome contributions to `py2nb`! If you have ideas for improvements or have found bugs, please follow these steps to contribute:

1. **Fork the Repository**

    Click the "Fork" button at the top right corner of this repository page.

2. **Clone Your Fork**

    ```sh
    git clone https://github.com/w3cdpass/py2nb.git
    cd py2nb
    ```

3. **Create a New Branch**

    ```sh
    git checkout -b your-branch-name
    ```

4. **Make Your Changes**

    Make your changes to the codebase and ensure that all tests pass.

5. **Commit Your Changes**

    ```sh
    git add .
    git commit -m "Description of your changes"
    ```

6. **Push to Your Fork**

    ```sh
    git push origin your-branch-name
    ```

7. **Create a Pull Request**

    Go to the original repository and create a pull request with a description of your changes.