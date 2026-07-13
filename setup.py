from setuptools import find_packages,setup
from typing import List
const='-e .'
def get_req(path:str)->List[str]:
    '''
    THIS FUNCTION WILL RETURN THE LIST OF REQUIREMENTS
    '''
    req=[]
    with open(path) as file_obj:
        req=file_obj.readlines()
        req=[r.replace("\n","") for r in req ]
        if const in req:
            req.remove(const)

    return req       

setup(
    name="mlproject",
    version='0.0.1',
    author='Divyansh Vishal',
    author_email='divyansh.tiwary@gmail.com',
    packages=find_packages(),
    install_requires=get_req('requirements.txt')
)