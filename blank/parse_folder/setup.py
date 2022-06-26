from setuptools import setup, find_namespace_packages

setup(
    name='parse_folder',
    version='0.1.0',
    description='Project Parse folder',
    author='Olesia Popilovska',
    author_email='olesia.usagi@gmail.com',
    license='MIT',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=find_namespace_packages(),
    entry_points={'console_scripts': [
        'parse_folder=parse_folder.main:start']}
)
