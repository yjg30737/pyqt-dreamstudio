from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

setup(
    name='pyqt-dreamstudio',
    version='0.0.11',
    author='Jung Gyu Yoon',
    author_email='yjg30737@gmail.com',
    license='MIT',
    packages=find_packages(),
    package_data={'pyqt_dreamstudio': ['logo.png'], 'pyqt_dreamstudio.ico': ['history.svg', 'setting.svg']},
    description='Using DreamStudio API in Python desktop application',
    url='https://github.com/yjg30737/pyqt-dreamstudio.git',
    long_description_content_type='text/markdown',
    long_description=long_description,
    install_requires=[
        'PyQt5>=5.14',
        'PySide6',
        'qtpy',
        'stability_sdk'
    ]
)