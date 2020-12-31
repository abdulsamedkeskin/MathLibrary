from distutils.core import setup
import setuptools
from setuptools import setup
from os import path

readme = path.abspath(path.dirname(__file__))
with open(path.join(readme, 'Readme.md'), encoding='utf-8') as f:
    readme_description = f.read()

setup(
  name = 'MathLibrary',         
  packages = setuptools.find_packages(),   
  version = '7.0',
  long_description=readme_description,
  long_description_content_type='text/markdown',
  license='MIT',      
  description = 'Math Library For Python',   
  author = 'Abdulsamet Keskin',                  
  author_email = 'erdemsametkeskin25@gmail.com',      
  url = 'https://github.com/abdulsamedkeskin/MathLibrary',   
  download_url = 'https://github.com/abdulsamedkeskin/MathLibrary/archive/V7.tar.gz',
  keywords = ['MathLibrary'],
  classifiers=[
    'Development Status :: 3 - Alpha',      
    'Intended Audience :: Developers',      
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   
    'Programming Language :: Python :: 3',      
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
