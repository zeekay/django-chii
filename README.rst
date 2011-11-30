===================================
Extra modules and web app for chii.
===================================

``django-chii`` provides a couple of extra modules for `chii <https://bitbucket.org/zeekay/chii/>`_.
It adds the following functionality to chii:

- A searchable quotes database.
- Link tracking.

The modules can be interacted with by messaging the bot, or through the web interface. You can check out
an installation of django-chii `here <http://smth.us>`_.

============
Installation
============

I recommend using ``virtualenv`` and ``pip``. You can install the requirements using ``pip``::

    pip install -r requirements.txt

You'll want to create a ``local_settings.py`` file and customize the project. Finally run ``syncdb``
as you normally would::

    python manage.py syncdb

Symlink the ``django_chii`` module so that it can be imported and add ``django_chii`` to the
list of modules in your ``bot.config`` and specify the full path to ``django-chii``:

::

    modules:
    - django_chii
    django_chii: /path/to/django-chii

Contact
=======

You can message me through github/bitbucket or catch me on ``irc.freenode.net``
and ``irc.esper.net`` as zk/zeekay.
