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

