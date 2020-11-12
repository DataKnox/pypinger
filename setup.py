from setuptools import setup

with open('README.md', 'r') as file:
    long_description = file.read()

setup(name='pypinger',
      version='2.0.2',
      description='Another way to ping in Python',
      url='https://github.com/DataKnox/pypinger',
      author='Knox Hutchinson',
      author_email='knox@knoxsdata.com',
      license='MIT',
      packages=['pypinger'],
      keywords=['ping', 'icmp', 'network'],
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Intended Audience :: System Administrators',
          'Natural Language :: English'
      ],
      long_description=long_description,
      long_description_content_type='text/markdown',
      entry_points={  # Optional
          'console_scripts': [
              'pyping=pypinger:pyping',
          ],
      },
      zip_safe=False)
