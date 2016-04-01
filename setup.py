#! /usr/bin/env python

if __name__ == "__main__":
    from setuptools import setup
    setup(name="mousestyles",
          packages=["mousestyles", "mousestyles.data", "mousestyles.data.tests"],
          package_data={'mousestyles.data': ['*.npy', '*/*/*.npy']})

