from setuptools import setup, find_packages

setup(
        name="contour_plotting",
        version="0.1.0",
        description="Contour plotting utilities using matplotlib and corner",
        author="Padma Venkatraman",
        author_email="vpadma@berkeley.edu",
        packages=find_packages(),
        install_requires=[
            "numpy",
            "matplotlib",
            "corner",
        ],
        python_requires=">=3.7",
    )