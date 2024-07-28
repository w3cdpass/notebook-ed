import unittest
import os
from notebook_ed import delete_file, convert_py_to_ipynb, process_directory

class TestConverter(unittest.TestCase):

    def setUp(self):
        """Set up test environment."""
        self.test_py_file = 'test_script.py'
        self.test_ipynb_file = 'test_script.ipynb'
        with open(self.test_py_file, 'w') as f:
            f.write("print('Hello, world!')")

    def tearDown(self):
        """Clean up test environment."""
        if os.path.exists(self.test_py_file):
            os.remove(self.test_py_file)
        if os.path.exists(self.test_ipynb_file):
            os.remove(self.test_ipynb_file)

    def test_delete_file(self):
        """Test deleting a file."""
        self.assertTrue(os.path.exists(self.test_py_file))
        delete_file(self.test_py_file)
        self.assertFalse(os.path.exists(self.test_py_file))

    def test_convert_py_to_ipynb(self):
        """Test converting a .py file to a .ipynb file."""
        convert_py_to_ipynb(self.test_py_file)
        self.assertFalse(os.path.exists(self.test_py_file))
        self.assertTrue(os.path.exists(self.test_ipynb_file))

    def test_process_directory(self):
        """Test processing a directory."""
        os.makedirs('test_dir', exist_ok=True)
        test_py_file = os.path.join('test_dir', 'test_script.py')
        with open(test_py_file, 'w') as f:
            f.write("print('Hello, world!')")
        process_directory('test_dir')
        self.assertFalse(os.path.exists(test_py_file))
        self.assertTrue(os.path.exists(os.path.join('test_dir', 'test_script.ipynb')))
        os.remove(os.path.join('test_dir', 'test_script.ipynb'))
        os.rmdir('test_dir')

if __name__ == '__main__':
    unittest.main()
