#!/usr/bin/env python
import sys
from django.conf import settings, global_settings as default_settings
from django.core.management import execute_from_command_line
from os import path

if not settings.configured:
    module_root = path.dirname(path.realpath(__file__))

    settings.configure(
        DEBUG = False,  # will be False anyway by DjangoTestRunner.
        TEMPLATE_DEBUG = True,
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': ':memory:'
            }
        },
        TEMPLATE_LOADERS = (
            'django.template.loaders.app_directories.Loader',
        ),
        TEMPLATE_CONTEXT_PROCESSORS = default_settings.TEMPLATE_CONTEXT_PROCESSORS + (
            'django.core.context_processors.request',
        ),
        INSTALLED_APPS = (
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.sites',
            'django.contrib.admin',
            'django.contrib.sessions',
            'fluent_pages',
            'fluent_pages.tests.testapp',
            'mptt',
            'polymorphic',
            'polymorphic_tree',
        ),
        SITE_ID = 4,
        ROOT_URLCONF = 'fluent_pages.tests.testapp.urls',
        FLUENT_PAGES_TEMPLATE_DIR = path.join(module_root, 'fluent_pages', 'tests', 'testapp', 'templates'),
    )

def runtests():
    argv = sys.argv[:1] + ['test', 'fluent_pages'] + sys.argv[1:]
    execute_from_command_line(argv)

if __name__ == '__main__':
    runtests()
