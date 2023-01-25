User Documentation
==================


.. toctree::
  :maxdepth: 3


Argument & Options
------------------

The ``solution`` script takes the path a file as an argument and has only one option:


^^^^^^^^^^^^^^
``--max-size``
^^^^^^^^^^^^^^
    Maximum file size in bytes


It is run this way::


  $ solution <PATH_OF_THE_FILE>


How to install and run the solution
-----------------------------------


We assume that you have `unzip` and `python3` already installed on your system.
We also assume that `black`, `pylint` and `pytest` python packages are installed.


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Extract the content of the `zip` archive
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


First, extract the content of the `zip` archive by running::


  $ unzip MachineLearningSoftwareEngineer_nourdine_bah.zip


This should create a folder called `deepintest` in your current directory.


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Create package archive and generate documentation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Change directory to go to the `deepintest` folder and build the package by running::


  $ cd deepintest
  $ make build


The archive should be now visible in the `dist` directory::


  $ ls dist
  deepintest-0.0.0-py3-none-any.whl  deepintest-0.0.0.tar.gz


If you have `sphinx` and `sphinx-rtd-theme` installed, you can generated the documentation by running::


  $ make doc


The generated documentation should be in `deepintest/docs/build/html`.
You can now leave the `deepintest` directory and go back to where you were::


  $ cd ../


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Create a `virtualenv` environment
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


If you don't have `virtualenv` already on your system, please install it by running::

  $ pip install virtualenv


Then, create a virtual environment called `venv` and source it by running::


  $ virtualenv venv
  $ . venv/bin/activate


You are now in the virtual environment.


^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Install the solution package
^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Now, install the solution package by running::


  (venv) $ pip install deepintest/dist/deepintest-0.0.0.tar.gz


The solution is now installed.
You can display information about the script by running::


  (venv) $ solution --help


^^^^^^^^^^^^^^^^
Run the solution
^^^^^^^^^^^^^^^^


To run the solution on a file you can run::


    (venv) $ solution <PATH_OF_THE_FILE>


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Leave the virtual environment
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


When you are done, you can leave the virtual environment by running::


  (venv) $ deactivate


