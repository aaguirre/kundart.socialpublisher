from setuptools import setup, find_packages
import os

version = '1.1'

setup(name='kundart.socialpublisher',
      version=version,
      description="Publish your content to Twitter and Facebook easily",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='facebook twitter social media',
      author='Alvaro Aguirre',
      author_email='aaguirre@kundart.com',
      url='http://www.kundart.com',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['kundart'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'python_twitter',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
