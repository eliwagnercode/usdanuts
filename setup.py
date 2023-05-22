from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.0.5'
DESCRIPTION = 'Calls USDA FoodData Central API for food nutrient data and parses responses.'

# Setting up
setup(
    name="usdanuts",
    version=VERSION,
    author="eliwagnercode (Eli Wagner)",
    author_email="<eliwagnercode@gmail.com>",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=['nutrition', 'nutritional', 'nutrient', 'food', 'foods', 'pantry', 'diet', 'diets', 'dietary', 'eat', 'eats', 'eating'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
