import setuptools

with open('requirements.txt') as f:
    required = f.read().splitlines()

setuptools.setup(
    name='PDF_Scraper',
    version='1.0.0',
    author="Richard Raphael Banak",
    description="Library for scrapping and RPA in PDF files.",
    url="https://github.com/Richardbnk/PDF_Scraper",
    packages=['pdf_scraper'],
    
    py_modules = ['PyPDF2'],
    
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    install_requires=[required],
)
