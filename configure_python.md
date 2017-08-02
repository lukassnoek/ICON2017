# How to set-up Python for this hackathon

There are many ways to install Python, but we recommend installing Python and Python-packages through the [Anaconda](https://www.continuum.io/) distribution, which has installers for both Windows and Mac (and Linux). Note that Mac (and Linux) probably already have Python installed, but we *still* recommend installing Anaconda to avoid any package/dependency issues that we may come across later.

### Download Anaconda
Anyway, go to the [Anaconda](https://www.continuum.io/downloads) website and click on the download button corresponding to your operating system. Then, choose the **Python 3.6 version** of the installer (and choose between the 64 or 32 bit version; probably 64-bit). For *Windows*, after downloading the `.exe`, just follow the installation instructions.
For *Mac*, you can choose between the graphical installer or the command-line installer; choose whatever you like best.  

During the install, the Anaconda installer is going to ask for a few configurations, like where to install Anaconda and such. Importantly, when the installer asks:
*"Do you wish the installer to prepend the Anaconda3 install location to PATH in your /home/<user>/.bashrc?"*, answer **yes**. This will make sure that our notebook
uses the right version of Python.

### Install packages
If you installed Anaconda through the command line, close and reopen a terminal, which makes sure that the `$PATH` variable is reloaded and your OS finds the correct (Anaconda) version of Python. Now, we need to install the packages necessary for the tutorials. These packages encompass different functionality that we need to load, manipulate, and analyze MRI-images. We will use the following:  

* **numpy**: the standard package for working with **num**eric data in **Py**thon (e.g., manipulating n-dimensional arrays like MRI-images!);
* **scipy**: provides some functionality for statistics (like the t-test);
* **nibabel**: the *de facto* package for loading in MRI data;
* **scikit-learn**: the extremely versatile (and most popular) machine learning package in Python;
* **matplotlib**: the most-often used plotting package in Python;
* **skbold**: our own machine-learning-for-fMRI package (an optional section on [skbold](https://skbold.readthedocs.io) is included in the workshop)

To install these packages, we're going to use `pip`, Python's package installer (which is shipped by default with Anaconda). The command `pip` works in a terminal/command line, so Mac/Linux users should simply open a terminal window. Windows users can open a command prompt either by opening the `cmd` utility (search for "cmd" in your programs) or by using the *Anaconda command prompt* (a Linux-style terminal emulator; search for "Anaconda" in your programs).

Once you've opened a terminal, navigate to the directory with materials, and run:
use the following command to install all the packages at once:

    $ pip install -r requirements.txt

Alternatively (if it for some reason doesn't work), you can install the packages one by one by running:

    $ pip install <package name>

So, to install *nibabel*, just type: `pip install nibabel`. **Note**: scikit-learn can be installed by doing: `pip install sklearn`.

If you want to check whether all packages are installed correctly, you can run the `verify_package_installs.py` script located in the materials folder (run `python verify_package_installs.py` in a terminal). You might get a "DeprecationWarning", but you can ignore that!

**[Back to main page](README.md)**
