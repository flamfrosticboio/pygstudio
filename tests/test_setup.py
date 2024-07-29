import subprocess
from datetime import datetime
import pytest

@pytest.skip(reason="This test is a cli based test")
def main():
    subprocess.call('python -m pygstudio create "Test Pygstudio Project" -o ".temp"')