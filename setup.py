from setuptools import setup, find_packages
from setuptools.command.build_py import build_py as _build_py

with open('requirements.txt', 'r') as f:
    requirements = f.readlines()

setup(
    name='BiliScraper',
    version='0.0.1',
    description='哔哩哔哩视频刮削器',
    author='wuyaos',
    author_email='wufeifeng_hust@163.com',
    url='https://github.com/wuyaos',
    keywords=['scraper', "bilibili", "nfo"],
    python_requires=">=3.6",
    install_requires=requirements,
    packages=['biliscraper'],
    entry_points={
        'console_scripts': [  # 命令的入口
            'biliscraper=biliscraper.main:main',
        ]
    })
