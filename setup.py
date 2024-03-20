from setuptools import find_packages, setup

# Read the contents of your README file
with open("README.md", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="ResumeCreatorator",
    version="0.1",
    packages=find_packages(exclude=["tests*", "docs"]),
    include_package_data=True,
    description="Django resume creation app from user data. Imports into `django-custom-user-base`.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/brucestull/resume-creatorator",
    author="Flynnt Knapp",
    author_email="FlynntKnapp@gmail.com",
    license="MIT",
    install_requires=[
        "Django>=5.0.3,<6.0",
    ],
    classifiers=[
        "Framework :: Django",
        # "Programming Language :: Python :: 3",
        # "Programming Language :: Python :: 3.8",
        # "Programming Language :: Python :: 3.9",
        # "Programming Language :: Python :: 3.10",
        # "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
