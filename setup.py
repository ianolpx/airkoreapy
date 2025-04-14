from setuptools import setup

setup(
    name="airkoreapy",
    version="0.0.1",
    description="",
    author="JB Park",
    author_email="ianolpx@gmail.com",
    url="https://github.com/ianolpx/airkoreapy",
    # packages=find_packages(),
    py_modules=["airkoreapy"],
    install_requires=[
        "requests",
        "tqdm",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)