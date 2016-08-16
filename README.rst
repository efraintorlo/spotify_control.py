###############
README
###############
:Author:   chinot7
:Date:   2016-08-16
:Version: 0.1
:Tags:  spotify, python

Control and get info from ``Spotify`` client

Install
#########

::

   python setup.py develop --user

Configuration
#############

In ``~/.bashrc`` or ``~/.zshrc`` include:

::

   export PATH=~/.local/bin:$PATH


Usage
#####

By default ``stupify.py`` prints the **artist-title** if ``Spotify`` is playing

::
    stupify.py

You can extract `artist`, `title` or `album` with:

::

    stupify.py -o artist
    stupify.py -o title
    stupify.py -o album


Version 0.1
###########

1. Get `Spotipy` info
