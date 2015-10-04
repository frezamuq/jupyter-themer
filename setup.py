from setuptools import setup, find_packages

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='jupyter-themer',
    version='0.1.0',
    license='MIT',
    description='Custom CSS themer for jupyter notebooks',
    long_description=long_description,
    author='Leon Chen',
    author_email='lchen3@gmail.com',
    url='https://github.com/transcranial/jupyter-themer',
    packages=find_packages(exclude=['*test*']),
    package_data={'': ['LICENSE']},
    entry_points = {
        'console_scripts' : [
            'jupyter-themer = jupythemer:run'
        ]
    },
    install_requires=[])
