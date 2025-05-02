from setuptools import setup, find_packages

setup(
    name="thony_keyboards",
    packages=find_packages(),
    install_requires=[
        'fastapi',
        'uvicorn',
        'sqlalchemy'
    ]
)