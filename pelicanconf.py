#!/usr/bin/env python
# -*- coding: utf-8 -*- #

from __future__ import unicode_literals


########################### General Settings ###################################
AUTHOR = 'Katrina Sperry'
SITENAME = 'Katrina Sperry'
SITESUBTITLE = 'My journey from modeling clothes to modeling data.'
SITEURL = ''

PATH = 'content'
DELETE_OUTPUT_DIRECTORY = True

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = 'en'

USE_FOLDER_AS_CATEGORY = True
DEFAULT_DATE_FORMAT = '%a %d %B %Y'
DEFAULT_DATE = 'fs'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'))

# Social widget
SOCIAL = (('github', 'https://github.com/katrinasperry'),
          ('linkedin', 'https://www.linkedin.com/in/katrinasperry/'),
          ('twitter', 'https://twitter.com/KatrinaSperry'))

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# STATIC_PATHS = ['images', 'extra/CNAME']
# EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}
# Generate archive
#YEAR_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/index.html'

##################### Exterior Services ############################
#GOOGLE_ANALYTICS = "UA-54524020-1"


####################### Theme-Specific Settings #########################
THEME = './pelican-themes/hyde'

BIO = "Hi! I like data science and cats."
PROFILE_IMAGE = 'headshot.jpg'

SHOW_ARTICLE_CATEGORY = True

JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}

MARKUP = ('md', 'ipynb')


############################ Plugins ######################################
PLUGIN_PATHS = ['./plugins', './pelican-plugins']
PLUGINS = ['ipynb.markup', 'i18n_subsites']
JINJA_ENVIRONMENT = {
    'extensions': ['jinja2.ext.i18n'],
}

IGNORE_FILES = ['.ipynb_checkpoints']
