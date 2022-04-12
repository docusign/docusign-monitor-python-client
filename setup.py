# coding: utf-8

"""
    Monitor API

    An API for an integrator to access the features of DocuSign Monitor  # noqa: E501

    OpenAPI spec version: v2.0
    Contact: devcenter@docusign.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from setuptools import setup, find_packages, Command, os  # noqa: H301	

NAME = "docusign-monitor"
VERSION = "1.1.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.8.0", "certifi >= 14.05.14", "python-dateutil >= 2.5.3", "setuptools >= 21.0.0", "PyJWT>=1.7.1,<2", "cryptography>=2.5", "nose>=1.3.7"]

class CleanCommand(Command):
    """Custom clean command to tidy up the project root."""
    user_options = []
    def initialize_options(self):
        pass
    def finalize_options(self):
        pass
    def run(self):
        os.system('rm -vrf ./build ./dist ./*.pyc ./*.tgz ./*.egg-info')

this_directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()
    

setup(
    name=NAME,
    version=VERSION,
    description="Monitor API",
    author_email="devcenter@docusign.com",
    url="",
    keywords=["Swagger", "Monitor API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    cmdclass={
        'clean': CleanCommand,
    },
    long_description=long_description,
    long_description_content_type='text/markdown'
)
