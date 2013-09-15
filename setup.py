from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='pytablefy',
      version=version,
      description="A python SVG table library",
      long_description="""\
A python SVG table library""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='python table SVG PNG',
      author='Fayiz Musthafa',
      author_email='fayizk1@gmail.com',
      url='https://github.com/fayizk1/pytablefy',
      license='MIT/X11 license',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=True,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
