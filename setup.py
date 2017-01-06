from setuptools import setup, find_packages

setup(
    name="page_object",
    version="0.1.1",
    description="Python implementation of the PageObject pattern",
    author="Onshift Inc.",
    author_email="dev@onshift.com",
    url="https://github.com/OnShift/page_object",
    license="MIT",
    keywords=['page_object', 'selenium', 'webdriver'],
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=[
        'pyvirtualdisplay==0.2',
        'selenium==3.0.2'
    ]
)
