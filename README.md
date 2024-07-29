# notebook-ed

A tool to convert `.py` files to `.ipynb` files and delete the original `.py` files. This tool makes it easy to convert Python scripts into Jupyter Notebooks for easy sharing and collaboration.

If you find `notebook-ed` useful, please consider giving it a star on GitHub! Your support helps me to continue developing and improving this tool.

![Python](https://img.shields.io/badge/python-v3.8+-blue.svg?logo=python)
[![PyPI version](https://img.shields.io/badge/pip%20install-notebook--ed%3D%3D0.1.3-blue)](https://pypi.org/project/notebook-ed/0.1.2/)
[![GitHub stars](https://img.shields.io/github/stars/w3cdpass/notebook-ed?style=social)](https://github.com/w3cdpass/notebook-ed/stargazers)

## Project Insights

`notebook-ed` is designed to streamline the process of converting Python scripts into Jupyter Notebooks. It is particularly useful for educators, data scientists, and developers who need to present their Python code in a more interactive format. 

### Features

- Converts `.py` files to `.ipynb` files
- Deletes the original `.py` files after conversion
- Processes directories to batch convert multiple files
- Simple command-line interface for ease of use

## How to Start with Source Code

To start using `notebook-ed`, follow these steps:

1. **Clone the Repository**

    ```sh
    git clone https://github.com/w3cdpass/notebook-ed.git
    cd notebook-ed
    ```

2. **Create a Virtual Environment**

    ```sh
    python -m venv notebook_ed_env
    ```

3. **Activate the Virtual Environment**

    - On Windows:
        ```sh
        notebook_ed_env\Scripts\activate
        ```
    - On macOS/Linux:
        ```sh
        source notebook_ed_env/bin/activate
        ```

4. **Install Dependencies**

    ```sh
    pip install -r requirements.txt
    ```

5. **Run the Script**

    ```sh
    notebook-ed -r <root_directory>  # To convert all .py files in a directory
    notebook-ed -f <file_path>       # To convert a single .py file
    ```

## How to Contribute

We welcome contributions to `notebook-ed`! If you have ideas for improvements or have found bugs, please follow these steps to contribute:

1. **Fork the Repository**

    Click the "Fork" button at the top right corner of this repository page.

2. **Clone Your Fork**

    ```sh
    git clone https://github.com/<your-username>/notebook-ed.git
    cd notebook-ed
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

## Contact

For any queries, feel free to contact me at [kupasva663@gmail.com](mailto:kupasva663@gmail.com).
