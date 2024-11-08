from setuptools import setup

package_name = 'outdoor_simulation'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/' + package_name + '/launch', ['launch/outdoor_launch.py']),
        ('share/' + package_name + '/worlds', ['worlds/cs460pp2.wbt']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Jeongbin Son',
    maintainer_email='json10@crimson.ua.edu',
    description='A ROS2 package for CS460 Project Part 2',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            
        ],
    },
)
