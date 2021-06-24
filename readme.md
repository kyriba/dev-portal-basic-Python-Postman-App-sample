# basic-Python-Postman-App
## Requirements
Building the API client library requires:
1.  Python 3.0 or higher [Installation][1]
   
   [1]: https://www.python.org/downloads/


## Installation
To copy the API client to your computer copy link of the repository, open Command Prompt, go to the location where project will be copied and execute git clone command:
```shell
git clone https://github.com/OlhaLevko/basic-Python-Postman-App.git
```
Open the project folder via command prompt, for example:
```shell
cd basic-Python-Postman-App
```
Select the desired Collection in Postman, authenticate through "Get token." request and run the request that you want to provide in the Application.
If the request works, copy code from Postman:

![code.png](code.png)

In "Code snippet", proceed to the dropdown list with different programming languages, where "cURL" is set by default, and choose "Python - http.client" from the list. There, copy the snippet without the last line to clipboard:

![copy.png](copy.png)

Open the .../app.py file and input your piece of code:

![input.png](input.png)


Run the project in Terminal in the root folder of cloned app:
```shell
python app.py
```
If everything was done accordingly with provided steps, you will get the result printed in the command prompt.