from setuptools import setup, find_packages
from typing import List

HYPHEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    try:
        with open(file_path, 'r') as file_obj:
            requirements = file_obj.read().splitlines()
            requirements = [req.strip() for req in requirements if req.strip()]
            if HYPHEN_E_DOT in requirements:
                requirements.remove(HYPHEN_E_DOT)
    except FileNotFoundError:
        print(f"File {file_path} not found.")
        requirements = []
    return requirements

setup(
    name='Ml Project',
    version='1.0.0',
    author="Zia ul Islam Mughal",
    author_email='ziamughal132@gmail.com',
    description="A Machine Learning project to predict customer churn in a telecommunications company",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/ZiaulIslamMughal/telecom_churn_prediction',
    packages=find_packages(),
    include_package_data=True,
    install_requires=get_requirements("requirements.txt"),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    python_requires='>=3.8',
)