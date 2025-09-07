from setuptools import find_packages, setup

setup(
    name= 'mcqgenerator',
    version= '0.0.1',
    author= 'Navneet Kumar Singh',
    author_email= 'navneet.sing@gmail.com',
    install_requires= ["OpenAi", "langChain", "streamlit", "python-dotenv", "PyPDF2"],
    package= find_packages()
)