# create new libraries for project
# create a folder
# convert to python package and create __init__.py file 
# framawork: some packages are together for a purpose. collection of libraries.

from setuptools import find_packages, setup # searcging main directory for
from typing import List 

def get_requirements()->List[str]:
    '''This function will return list of requirements.
    '''
    requirement_list:List[str] = []

    ''' Write a code to read requirements.txt file and append each requirements in requirement_list variable'''
    return requirement_list

# we have one packages: sensor 
setup( #python setup.py install 
    name='sensor',
    version='0.0.1',
    author='Abdül',
    author_email='abdulmeral@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements() # ["pymongo==4.2.0"]
)