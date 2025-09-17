# download and install it from this page: https://pypi.org/project/pip/
# Download a Package
'''
Downloading a package is very easy.
Open the command line interface and tell PIP to download the package you want.
Navigate your command line to the location of Python's script directory, and type the following:
Example: 
Download a package named "camelcase":
C:\Users\Your Name\AppData\Local\Programs\Python\Python36-32\Scripts>pip install camelcase
'''
# Check PIP version:
# C:\Users\Your Name\AppData\Local\Programs\Python\Python36-32\Scripts>pip --version 
# Example: Import and use "camelcase":
import camelcase
camel = camelcase.CamelCase()
text = "hello world"
print(camel.hump(text)) 

# more packages: https://pypi.org/

#remove package:  C:\Users\Your Name\AppData\Local\Programs\Python\Python36-32\Scripts>pip uninstall camelcase
#output:
'''Uninstalling camelcase-02.1:
  Would remove:
    c:\users\Your Name\appdata\local\programs\python\python36-32\lib\site-packages\camelcase-0.2-py3.6.egg-info
    c:\users\Your Name\appdata\local\programs\python\python36-32\lib\site-packages\camelcase\*
Proceed (y/n)?'''

#list command to 2 C the packages installed:
# C:\Users\Your Name\AppData\Local\Programs\Python\Python36-32\Scripts>pip list
# update pip: python.exe -m pip install --upgrade pip
