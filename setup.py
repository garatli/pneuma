from setuptools import setup

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

## edit below variables as per your requirements -
REPO_NAME = "unstuck"
AUTHOR_USER_NAME = "garatlia"
SRC_REPO = "src"
LIST_OF_REQUIREMENTS = ['streamlit', 'streamlit_lottie', 'requests']


setup(
    name=SRC_REPO,
    version="0.0.1",
    author=AUTHOR_USER_NAME,
    description="NLP book recommender system",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=[SRC_REPO],
    license="MIT",
    python_requires=">=3.7",
    install_requires=LIST_OF_REQUIREMENTS
)
