from setuptools import setup, find_packages

setup(
    name='sensible-text-test-runner',
    version='0.3.0',
    description='Selectable test on failure',
    author='David Sanders',
    author_email='dsanders@rapilabs.com',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
    ],
    install_requires=[
        'Django',
    ],
)
