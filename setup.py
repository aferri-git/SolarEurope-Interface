# Enable `pip install` for your package

import os
from setuptools import find_packages
from setuptools import setup

with open("requirements_local.txt") as f:
    content = f.readlines()
requirements = [x.strip() for x in content if "git+" not in x]

setup(name='SolarEurope-interface',
      version=os.environ.get('VERSION'),
      description="SolarEurope Model (automate_model_lifecycle)",
      #license="",
      author="A. Ferri",
      #author_email="",
      #url="",
      install_requires=requirements,
      packages=find_packages(),
      test_suite="tests",
      # include_package_data: to install data from MANIFEST.in
      include_package_data=True,
      zip_safe=False)