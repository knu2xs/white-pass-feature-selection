from setuptools import find_packages, setup

with open('README.md', 'r') as readme:
    long_description = readme.read()

setup(
    name='white_pass_feature_selection',
    package_dir={"": "src"},
    packages=find_packages('src'),
    version='0.0.0',
    description='SelectKBest and any other ideas I get for feature selection workflow.',
    long_description=long_description,
    author='Joel McCune',
    license='Apache 2.0',
)
