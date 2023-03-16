from setuptools import setup, find_packages

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='alyxdash',
    version='0.1',
    author='onesixx',
    author_email='onesixx@sk.com',
    description='A Python package for dashboard',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/onesixx/alyxdash',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    install_requires=[
        'numpy>=1.19.2',
        'pandas>=1.1.2',
        'matplotlib>=3.3.2',
    ],
)
