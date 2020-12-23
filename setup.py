from PhishCanary import __version__
import os

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

project_dir = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(project_dir, 'README.md'),"r", encoding='utf-8') as f:
    long_description = f.read()

entry_points = {
    'console_scripts': [
        'phishcanary=PhishCanary.extractor:main',
    ],
}

setup(
    name="PhishCanary",
    version=__version__,
    author="Amirreza Niakanlahiji",
    author_email="aniak2@uis.edu",
    description=(
        "PhishCanary extracts potential phishing domains from a given TLD zone file."
    ),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/DissectMalware/PhishCanary",
    packages=["PhishCanary"],
    entry_points=entry_points,
    license='Apache License 2.0',
    python_requires='>=3.4',
    install_requires=[
        "dnspython",
        "tldextract",
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "Intended Audience :: Science/Research",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Security",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    package_data={
        'PhishCanary': ['configs\\trusted_nameservers.conf']},

)
