import setuptools

with open('requirements.txt') as f:
    required = f.read().splitlines()

setuptools.setup(
    name='pdf_scrapping',
    version='1.0.0',
    author="Richard Raphael Banak",
    description="Tool to assist navigation using mouse and keyboard for automated actions when RPA techniques are not effective.",
    url="https://github.com/Richardbnk/pdf_scrapping",
    packages=['pdf_scrapping'],
    
    py_modules = ['PyPDF2'],
    
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    install_requires=[required],
)
