from setuptools import find_packages,setup
from typing import List

constant="-e ."
def get_requirements(file_path:str)->List[str]:
    '''
    This function will return list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]
        if constant in requirements:
            requirements.remove(constant)
    return requirements



setup(
    name="ML Projext",
    version="0.0.1",
    author="Yamini",
    author_email="yaminilearning1@gmail.com",
    packages=find_packages(),
    install_requireents=get_requirements("requirements.txt")
)

