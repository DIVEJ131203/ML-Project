from setuptools import find_packages, setup
from typing import List

# Constant for the editable install string
HYPHEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    '''
    This function will return a list of requirements from the file.
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        # Remove newline characters and filter out the editable install string
        requirements = [req.replace("\n", "") for req in requirements if req.replace("\n", "") != HYPHEN_E_DOT]
    
    return requirements

setup(
    name='mlproject',
    version='0.0.1', 
    author="divej",
    author_email="divejahuja@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)