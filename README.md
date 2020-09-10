# Dash app simple example and template

This repository provide a very simple example of a dash app, and a template to 
use to build some new visualisation.

## How to setup the environment
### Pyenv

In order to launch the project you need to setup your environement.

First you need to install pyenv, to use the right version of python. To do so
follow the steps explained in the
[official git repository](https://github.com/pyenv/pyenv/).

Then you need to install and activate the right version of python with the
following commands when you are in the root directory:

`pyenv install $(cat .python-version)`

`pyenv local $(cat .python-version)`

You can now check that you are using the right version of python with the command:

`python --version`

### Pipenv

Then you need to use pipenv to install all the required packages. Install pipenv
follopwing the step described in the 
[official git repository](https://github.com/pypa/pipenv).

To install all the packages with the good version from the file `Pipefile.lock`,
 simply run the following command:

`pipenv install` 

Now you need to activate the environement with all the packages installed. To do
so simply use the command:

`pipenv shell`

Now all the packages are available.

## Launch the app

To launch the app, go in the root folder and use the command:

`python index.py`

The very simple dashboard is then available at the following url:
`http://127.0.0.1:8050`.
