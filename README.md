# ramanujans-way
Steps to set up the project on your local machine:  
1) Make a new folder.  
2) Initialize an empty git repository inside the folder by running the command "git init" in your terminal.  
3) Clone the repository using "git clone https://github.com/VersionNITT/ramanujans-way.git".  
4) Move into the folder, set up a new virtual enviroment and activate it.  
   4.1) For making a new virtual enviroment, paste "python3 -m venv venv" and run it.  
   4.2) For activating it:  
        Windows:  
        i) Set-ExecutionPolicy Unrestricted -scope process  
        ii) .\venv\Scripts\activate  
        Mac OS/Linux:  
        i) source venv/bin/activate  
5) Install all the dependencies using "pip install -r requirements.txt".  
6) Set up the database by typing "flask create_db" in the terminal.  
7) To run the app enter "flask run".  