from setuptools import find_packages, setup
from typing import List


hyphen = "-e ."

def get_requirements(file_path: str) -> List[str]:
    '''
    This function returns a list of required packages from a file.
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "").strip() for req in requirements]

        if hyphen in requirements:
            requirements.remove(hyphen)

    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='Bedanta',
    author_email='bedantaroy9@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirement.txt')
)