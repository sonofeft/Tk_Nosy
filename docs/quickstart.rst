
.. quickstart

QuickStart
=========

Verify tkinter
--------------

**In Theory** tkinter is included with all standard Python distributions.
(In practice, it might not be included.)
It's almost certainly there on a Windows machine, however,
on Linux you might have to try::

    sudo apt-get update
    sudo apt-get install python-tk
    sudo apt-get install python3-tk
    
In order to get tkinter/Tkinter for python 2 & 3.

You can test the installation from a terminal window with::

    >>> import Tkinter       # python2
    >>> Tkinter._test()      # python2
    
    >>> import tkinter       # python3
    >>> tkinter._test()      # python3

This should pop up a small test window.

Install
-------

The easiest way to install tk_nosy is::

    pip install tk_nosy
    
        OR on Linux
    sudo pip install tk_nosy
        OR perhaps
    pip install --user tk_nosy

In case of error, see :ref:`internal_pip_error`

.. _internal_source_install:

Installation From Source
------------------------

Much less common, but if installing from source, then
the best way to install tk_nosy is to use pip after navigating to the directory holding tk_nosy source code::

    cd full/path/to/tk_nosy
    pip install -e .
    
        OR on Linux
    sudo pip install -e .
        OR perhaps
    pip install --user -e .
    
This will execute the local ``setup.py`` file and insure that the pip-specific commands in ``setup.py`` are run.

Running tk_nosy
---------------

After installing with pip, there will be a launch command line program called **tk_nosy** or, on Windows, **tk_nosy.exe**. From a terminal or command prompt window simply type::

    tk_nosy

and the tk_nosy window should pop up. If not, then there may be an issue with your system path.
The path for the tk_nosy executable might be something like::

    /usr/local/bin/tk_nosy             (if installed with sudo pip install -e .)
         or 
    /home/<user>/.local/bin/tk_nosy    (if installed with pip install -e .)
         or 
    C:\Python27\Scripts\tk_nosy.exe    (on Windows)

Make sure your system path includes the above path to **tk_nosy**.


After launching tk_nosy, you can use the ``Change Dir`` command to select the directory to watch.
If you use the command line to navigate to the directory being developed and simply type::

    cd <path to my project>
    tk_nosy
    
No ``Change Dir`` navigation will be required.
Achieve the same effect from anywhere, by typing::
      
    tk_nosy <path to my project>
    
If tk_nosy detects a project in the local directory, it will launch nosetests, show results and start watching python files for changes.  If there is no project detected, it will ask for a directory to watch.

It is possible to run tk_nosy directly from source without installing it. Simply navigate to the source files and type::

    python main_gui.py
      or
    python main_gui.py <name of directory to watch>


.. _internal_pip_error:

pip Error Messages
------------------

If you get an error message that ``pip`` is not found, see `https://pip.pypa.io/en/latest/installing.html`_ for full description of pip installation.

I've sometimes had issues with pip failing on Linux with a message like::


    InsecurePlatformWarning
            or    
    Cannot fetch index base URL https://pypi.python.org/simple/

Certain Python platforms (specifically, versions of Python earlier than 2.7.9) have the InsecurePlatformWarning. If you encounter this warning, it is strongly recommended you upgrade to a newer Python version, or that you use pyOpenSSL as described in the OpenSSL / PyOpenSSL section.    

Also ``pip`` may be mis-configured and point to the wrong PyPI repository.
You need to fix this global problem with ``pip`` just to make python usable on your system.


If you give up on upgrading python or fixing ``pip``, 
you might also try downloading the tk_nosy source package 
(and all dependency source packages)
from PyPI and installing from source as shown above at :ref:`internal_source_install`


