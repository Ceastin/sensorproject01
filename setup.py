from setuptools import find_packages,setup
from typing import List
HYPHEN_E_DOT='-e.'
def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path, 'r') as f:
        requirements = f.readlines()
        requirements=[req.replace("\n","") for req in requirements]
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements


setup(
    name='Fault detection',
    version='0.0.1',
    author='sahil',
    author_mail='ceastinstark@gmail.com',
    install_requirements=get_requirements('requirements.txt'),
    packages=find_packages()
)