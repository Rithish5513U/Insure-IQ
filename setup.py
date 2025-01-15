from setuptools import find_packages, setup

def get_requirements(file_path):
    
    with open(file_path) as requirements_obj:
        requirements = requirements_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
        
        if "-e ." in requirements:
            requirements.remove("-e .")
            
        return requirements
    
setup(
    name="Medical-Cost-Prediction",
    version="0.0.1",
    autor="Rithish S",
    author_email="rithish.satish@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)