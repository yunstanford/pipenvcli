"""
Add Task Example
"""

import subprocess


def distribute():
    """ distribute the package """
    subprocess.call([
        "python", "setup.py",
        "sdist", "bdist_wheel", "--universal", "upload"
    ])


def build_doc():
	""" Build Documentation """
	print("Build Documentation..")
