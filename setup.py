from setuptools import setup,find_packages
from typing import List

def install_requirements(file:str)->List[str]:
    package_list = []
    with open(file) as f:
        package_list = f.readlines()
        F = [word.replace("\n","")for word in package_list]
        if "-e ." in package_list:
            package_list.remove("-e .")

    return package_list

setup(name='Delhi_House_Price_predictions',
      version='1.0',
      author='Gaurav',
      packages=find_packages(),
      install_requires=install_requirements('requirements.txt'),
    )

if __name__ == '__main__':
    a = install_requirements('requirements.txt')
    print(a)