from setuptools import setup, find_packages

setup(
    name='premanai',
    version='0.1',
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        'openai',
        'requests',
        'Pillow',
        'moviepy',
        'pydub',
        'opencv-python',
        'python-docx',
        'reportlab'
    ],
    entry_points={
        'console_scripts': [
            'premanai=preman_core:main',
        ],
    },
)
