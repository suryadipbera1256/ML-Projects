from setuptools import find_packages,setup
from typing import List


HYPEN_E_DOT='-e .'
def get_requirement(file_path:str)->List[str]:
    '''
    this function will return the List of requirements
    '''
    file_Path = r"C:\Users\Arnash Das\OneDrive\Desktop\ML-Projects\requirement.txt"
    requirement=[]
    with open(file_Path) as file_obj:
        requirement=file_obj.readlines()
        requirement=[req.replace("\n"," ") for req in requirement]

        if HYPEN_E_DOT in requirement:
            requirement.remove(HYPEN_E_DOT)

    return requirement        


setup(

name='ML-PROJECTS',
version='0.1',
author='suryadip',
author_email='suryadip230@gmail.com',
packages= find_packages(),
install_requires=[get_requirement("requirement.txt")]

)