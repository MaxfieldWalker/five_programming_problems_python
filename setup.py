from setuptools import setup, find_packages
import sys

sys.path.append('./src')
sys.path.append('./tests')

setup(
    name='Five programming problems',
    version='0.0.1',
    packages=find_packages(),
    test_suite='q1_test.suite'
)
