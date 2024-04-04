from setuptools import find_packages, setup

package_name = 'my_controller'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='athena',
    maintainer_email='athena@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "trial_controller= my_controller.trial_controller:main",
            "trial_controller_diff= my_controller.trial_controller_diff:main",
            "trial_controller_opti= my_controller.trial_controller_opti:main",
            "trial_controller_backup_original= my_controller.trial_controller_backup_original:main",
            "trial_controller_backup= my_controller.trial_controller_backup:main",
            "evaluation_node=my_controller.evaluation_node:main",
            "simplenode=my_controller.simplenode:main",
            "evaluation_node_odom=my_controller.evaluation_node_odom:main",
            "evaluation_node_slam=my_controller.evaluation_node_slam:main",
            "optitrack_node=my_controller.optitrack_node:main"
        ],
    },
)
