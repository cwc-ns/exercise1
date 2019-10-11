# exercise1:
Exercise 1 is designed to understand the very basic of python coding. We developed this application with **python 3** along with the **flask** microframework. So you just required to have *python 3*, *pip* and *flask*. 

At first, download the ***exercise1*** application as a zip file from [here](https://github.com/cwc-ns/exercise1). Now open your Terminal/Command Prompt and run the following command.

    cd exercise1

# installing python and pip:
- If you have *python 3* (by running `python --version` or `python3 --version`) on your pc, please skip this section. 
- If you are new to python and you do not have *python 3* on your pc, then install python by following 
  * **Linux User:** Run the following command on your Terminal window
      
        sudo apt-get install python3-dev python3-pip
      
  * **Mac and Windows:** [this guideline](https://www.youtube.com/watch?v=YYXdXT2l-Gg)

# version checking:
Check your python and pip (python package installer).
- *python:* 

      python --version
      or 
      python3 --version
      
- *pip:*

      pip --version
      or 
      pip3 --version
      
# requirements:
If you have **python 3** and **pip** on your local pc, then it's time to install **flask** -- with 

    pip install flask
    or 
    pip3 install flask
    
or,

    pip install -r requirements.txt
    or
    pip3 install -r requirements.txt

You could check **flask** *version* with --

    pip show flask
    or
    pip3 show flask
    
Now your pc is ready to run the application.

# running application:
Run the following command to run the application on your terminal.

    python app.py
    or
    python3 app.py

Hope you will get something like --

    * Serving Flask app "app" (lazy loading)
    * Environment: production
      WARNING: Do not use the development server in a production environment.
      Use a production WSGI server instead.
    * Debug mode: off
    * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

This means your application is running with *http* protocol at *127.0.0.1* IP on port *5000*. 

# monitoring: 
Open a browser on your development pc and try to browse the following url --

    http://127.0.0.1:5000/
    or
    http://localhost:5000/
    
# tasks?
Your tasks are ...

(1) You will not be able to get access this applicationn from outside the development pc. So, make a way to get access this application from some other devices (a mobile phone, some other laptop) which are connected to the same access point or router thorugh the IP of the development pc. You can get IP address of the development pc as --

    ifconfig
    or 
    ip addr
    or
    ipconfig

(2) Here is this application, we didn't hangle error for a requesting page, therefore you will get some error like -- 

    Not Found
    The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again.
    
Make a custom (404) error page containing a link for the landing page (the index page) of this application.
