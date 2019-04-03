
.. _software:

=============================================================
Software for the course
=============================================================

Python
------

Please use Python for computing in this class. If you don't know Python but are
used to Matlab, this 
`Numpy for Matlab Users
<https://docs.scipy.org/doc/numpy/user/numpy-for-matlab-users.html>`_
page might be very useful.  Even if you know Python and Numpy, this page has
some useful tips!

Some other resources:

- `AMath 583 notes <http://faculty.washington.edu/rjl/classes/am583s2014/notes/index.html#python>`_
  (from 2013) on Python ,
- `Python Tutorial <https://docs.python.org/2/tutorial/>`_,
- Many other tutorials can be found online.

To use Python effectively you will need `numpy <http://www.scipy.org/>`_ 
(which supports arrays and
many mathematical operations), `matplotlib <http://matplotlib.org/>`_
(matlab-style plotting).  The
`IPython shell <http://ipython.org/>`_ and/or 
`Jupyter notebooks <http://jupyter.org>`_
are highly recommended for interactive work, see below.  

The `Anaconda Python Distribution <https://www.anaconda.com/distribution/>`_
is one easy way to get everything you need.  If you install this, you can
also then use the `conda package installer
<https://docs.anaconda.com/anaconda/user-guide/tasks/install-packages/>`_ to install various
extensions easily.  
You might also want to check out `conda environments
<https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html>`_
as a way to compartmentalize versions of Python packages for different projects.

The notebooks for this class should be compatible with either Python 2.7 or 3.x.
The main difference that affects us is that in Python 3 `print` is a function
rather than a statement, e.g. ::

    print('x has the value %.6e' % x)

rather than::

    print 'x has the value %.6e' % x 

To get a code written using the print function to work in Python 2, you can
include this line at the top of the file::

    from __future__ import print_function

(with 2 underscores before and after `future`).
    

Jupyter notebooks
-----------------

See http://jupyter.org for more information and documentation. 

The notebook platform is rapidly being improved but as a result how things
behave often depend on what version you have installed.  If you installed
the Anaconda Python, you can insure you have jupyter and  are up to date 
via the bash commands::

    conda install jupyter
    conda update jupyter

Then in a bash shell you should be able to execute::

    jupyter notebook

to start the notebook server.  You can then navigate your browser
to the address shown when the notebook starts, e.g. ::

    http://localhost:8888/tree

If you want to easily run notebooks without installing any software, you
might try `CoCalc <https://cocalc.com/>`_ (previously known as SageMathCloud) or
`binder <http://mybinder.org>`_.  See :ref:`codes` for more information about
running the notebooks for this class.


