from setuptools import setup, find_packages

setup(
    name='IA_personal_assistant',
    version='0.1',
    author='EPamanes',
    author_email='youremail@example.com',
    description='A personal assistant AI package.',
    packages=find_packages(),
    install_requires=[
        # Add your package dependencies here
        # 'numpy',
        # 'requests',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)