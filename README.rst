===================================
Extra modules and web app for chii.
===================================

``django-chii`` provides a number of extra modules for `chii <https://bitbucket.org/zeekay/chii/>`_, a simple irc bot.
It includes a web interface as well.

============
Installation
============

Setup django project as you would normally, ``pip install -r requirements.txt``, ``./manage.py syncdb``.
You don't need to setup the django project wherever you have chii, you can just symlink the ``django_chii`` so
that chii can import it.

Add ``django-chii`` to your ``bot.config``:

::

    modules:
    - django_chii
    django_chii: /path/to/django/project

Contact
=======

You can message me through github/bitbucket or catch me on ``irc.freenode.net``
and ``irc.esper.net`` as zk/zeekay.
