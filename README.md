# kml2dwg
Python KML to DWG cconverter


### 0. Clone the project

Clone the repository into your local machine.

```Powershell
# Search to the location to clone the repo
cd <"Root directory">

# Clone the repo
{"Root directory"} git clone "https://github.com/JFToro192/kml2dwg.git"
```

Alternatively, you should download the repository to the location you intend to work on.

### 1. Virtual environment setup

Recreate the virtual environment for installing the packages and dependencies to use the scripts.


>**Note**: The setup requires installing python, [`venv`](https://docs.python.org/3/library/venv.html) and [`pip`](https://pypi.org/project/pip/) in your system. (Python 3.10)

```Powershell
# Access the folder contaning the scripts
<"Root directory"> cd "./kml2dwg"

# Create the python virtual environment
<"Root directory/kml2dwg"> python -m venv env

# Activate the virtual environment (Windows Powershell)
<"Root directory/kml2dwg"> ./env/bin/Activate.ps1

# Install the requirements file in the virtual environment
(env)<"Root directory/kml2dwg">  
(env)<"Root directory/kml2dwg">  pip install -r requirements.txt
```
>**Note**: it is possible to setup the environment in windows by executing the `env-setup.bat` file.  