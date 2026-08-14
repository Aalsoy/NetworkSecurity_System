from setuptools import setup, find_packages
from typing import List

def get_requirements()->List[str]:
    """This function will return the list of requirements"""
    
    requirement_lst:List[str]=[]
    try:
        with open('requirements.txt','r') as file:
            lines = file.readlines()
            for line in lines:
                requirement=line.strip()
                if requirement and requirement!= '-e .':
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found. Please ensure it exists in the project directory.")
        
    return requirement_lst

setup(
    name="Network Security",
    version="0.0.1",
    author="Aditya Boken",
    email="aditya.boken1@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)
