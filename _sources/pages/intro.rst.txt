
Installing tdmc
----------------

The is the install process for Linux (Ubuntu). It will probably work on macOS
as well. For Windows, you can try installing with Windows subsystem for Linux
(wsl).

- First, `install miniconda <https://www.anaconda.com/docs/getting-started/miniconda/install#quickstart-install-instructions>`_.  
- Set up a virtual ``python3`` envirnoment (follow the instructions from the miniconda page).  Activate your environment

.. code-block:: console

   source /hour/path/to/miniconda/bin/activate


- Clone or download the ``tdmc`` repository. Go to the cloned directory and
  run 

.. code-block:: console

   bash install.sh

To verify that the package is installed properly, check if you can import it
with python (``import tmdc``) and try running the example scripts in the 
examples directory.
