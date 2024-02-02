from setuptools import setup, find_packages

setup(
    name="NativeAmericanLanguageApp",
    version="1.0.0",
    author="Gregory Dixon",
    author_email="nashobastudios@gmail.com",
    description="An application for learning Native American languages with a GUI built using Tkinter.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/LurkyLunk/NativeLanguageApp.git",
    packages=find_packages(),
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    entry_points={
        "gui_scripts": [
            "native_app.py",
        ],
    },
    include_package_data=True,
    zip_safe=False,
)
