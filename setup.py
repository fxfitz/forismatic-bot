from setuptools import find_packages, setup

setup(
    name='forismatic_bot',
    version='1.0.0',
    description='Forismatic Slack Bot',
    long_description='Forismatic Slack Bot',
    author='Fran Fitzpatrick',
    author_email='francis.x.fitzpatrick@gmail.com',
    license='Apache v2.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'forismatic-bot-post = forismatic_bot:post_slack',
        ]
    },
    install_requires=[
        'requests',
    ]
)
