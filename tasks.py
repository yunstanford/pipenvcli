"""
Add Task Example
"""

import subprocess


def distribute(build):
    """ distribute the package """
    subprocess.call([
        "python", "setup.py",
        "sdist", "bdist_wheel", "--universal", "upload"
    ])
