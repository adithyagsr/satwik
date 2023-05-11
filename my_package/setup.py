from setuptools import setup

package_name = 'my_package'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='satwik',
    maintainer_email='satwik@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "Test_node = my_package.sample:main",
            "pub = my_package.pub:main",
            "sub = my_package.subscriber:main",
            "control = my_package.turtle_controller:main",
            "dum = my_package.dummy:main",
            "three = my_package.node_program:main",
            "subb = my_package.my_subscriber",
            "pubb = my_package.my_publisher",
            "circle = my_package.circle_turtle:main",
            "triangle = my_package.triangle_turtle:main",
             "sqr = my_package.square:main",
             "spr = my_package.spiral:main"
        ],
    
    },
)
