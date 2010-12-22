.. Confluence documentation master file, created by
   sphinx-quickstart on Thu Apr 30 10:59:32 2009.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

============
confluencerpclib
============

confluencerpclib is a Python_ library for Atlassian_ Confluence_ Wiki. 

Quick Start
***********

.. code-block:: python
	
	>>> from confluencerpclib import Confluence
	>>> c = Confluence('http://localhost:8080/confluence/rpc', 'username', 'password')
	>>> print c.get_server_info()
	Atlassian Confluence 3.0.2

Contents
********

.. toctree::
	:maxdepth: 2
	
	api

Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

.. _Python: http://python.org/
.. _Atlassian: http://atlassian.com/
.. _Confluence: http://www.atlassian.com/software/confluence/
