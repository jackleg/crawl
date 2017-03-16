#!/usr/bin/env python

from distutils.core import setup

setup(name='crawl',
      version='0.3',
      description='crawl and parse front.',
      scripts = ['crawl'],
      data_files = [ ('crawl_config', ['crawl.cfg']) ],
     )
