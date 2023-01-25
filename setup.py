"""
Packaging for Deeper Insights coding test.
"""

from setuptools import setup, find_packages

setup(
    name="deepintest",
    version="0.0.0",
    description="Deeper Insights's coding test",
    author="Nourdine Bah",
    author_email="nourdinebah@gmail.com",
    packages=find_packages(),
    include_package_data=True,
    install_requires=["click"],
    entry_points={"console_scripts": ["solution = deepintest.scripts.solution:main"]},
)
