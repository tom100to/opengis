from setuptools import setup, find_packages

dependencies = [
  "numpy>=1.19.5",
  "gdal",
]

setup(
    name="opengis",
    version="3.0.7",
    description="An open source GIS tool.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Zijie Wang",
    author_email="773598627@qq.com",
    packages=find_packages(),
    install_requires=dependencies,
    python_requires = ">=3.9",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    keywords="GIS",
    project_urls={
        'Source':"https://github.com/caaszj/opengis",
        'Tracker':"https://github.com/caaszj/opengis/issues"
        }
)