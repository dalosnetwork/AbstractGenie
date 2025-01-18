from setuptools import setup, find_packages

setup(
    name="abstract_genie",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "fastapi",
        "uvicorn",
        "sqlalchemy",
        "web3",
        "py-solc-x"
    ],
    entry_points={
        "console_scripts": [
            "abstract_genie=abstract_genie.main:app"
        ]
    },
    description="ERC-4337 Account Abstraction library for Ethereum",
    author="Ali Bertay SOLAK",
    author_email="alibertay@gmail.com",
    url="https://github.com/alibertay/AbstractGenie",
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.9",
)
