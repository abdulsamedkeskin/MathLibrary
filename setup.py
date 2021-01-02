from distutils.core import setup
from setuptools import setup,setuptools
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()



setup(
      name = 'MathLibrary',         
      packages = setuptools.find_packages(),   
      version = '15.0',
      license='MIT',      
      description = 'Math Library For Python',   
      author = 'Abdulsamet Keskin',                  
      author_email = 'erdemsametkeskin25@gmail.com',      
      url = 'https://github.com/abdulsamedkeskin/MathLibrary',   
      download_url = 'https://github.com/abdulsamedkeskin/MathLibrary/archive/V15.tar.gz',
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
      long_description=long_description,
      long_description_content_type='text/markdown'
)
