from setuptools import setup

setup(name='pt_pivotal_tools',
      version='0.15',
      description='Collection of pivotal command line tools',
      url='http://github.com/nikolawannabe/pivotal_tools',
      author='Jonathan Tushman, Case Talbot',
      author_email='sharon.talbot@gmail.com',
      license='MIT',
      packages=['pivotal_tools'],
      install_requires=[
          'requests',
          'docopt',
          'termcolor',
          'dicttoxml'
      ],
      entry_points={
          'console_scripts': ['pt_pivotal_tools = pivotal_tools:main']
      },
      zip_safe=False)
