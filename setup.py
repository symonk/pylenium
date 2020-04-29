from setuptools import setup, find_packages

with open("README.md") as f:
    long_description = f.read()
setup(
    name="pytest-pylenium",
    description="selenium wrapper for pytest to aid with system testing",
    license="Apache Software License 2.0",
    author="Simon Kerr",
    url="https://github.com/symonk/pytest-pylenium",
    version="0.0.1",
    author_email="jackofspaces@gmail.com",
    maintainer="Simon Kerr",
    maintainer_email="jackofspaces@gmail.com",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    entry_points={"pytest11": ["pylenium = pylenium.plugin"]},
    setup_requires=["setuptools_scm"],
    zip_safe=False,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Framework :: Pytest",
        "Topic :: Software Development :: Testing",
        "Topic :: Software Development :: Quality Assurance",
        "Programming Language :: Python :: 3.7",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: Apache Software License",
    ],
)
