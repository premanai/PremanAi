from setuptools import setup, find_packages

setup(
    name='PremanAi',
    version='0.1.0',
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        'openai',
        'requests',
        'pillow',
        'moviepy',
        'pydub',
        'opencv-python',
        'python-docx',
        'reportlab',
        'python-dotenv',
    ],
    entry_points={
        'console_scripts': [
            'premanai=preman_core:main',
        ],
    },
    author='Preman Empire',
    description='PremanAi: Bot AI Gaya Preman, Galak Tapi Bantuin!',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/PremanAi/PremanAi',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
)
