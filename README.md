# Card Game Simulataion
Insert Description Here

# Virtual Environment
For testing and running the application use the python virtual environment. Please do not push the venv directory or the pycache.
It is essential that everyone uses the venv, so that we are all working with the same dependancies, and so that whenever anyone uses a new package, we are all able to know which one it is and can update our venv. 

To create a virtual environment, run this command in the top level directory of the project:
```shell
python3 -m venv venv
```
Whenever you wish to activate the venv, run this command (again, you need to be in the top directory)
```shell
source venv/bin/activate
```

You will have to create the venv each time you begin working on a new branch. You will also have to install all of the required packages. This can be done using the requirements.txt file. After activating the venv, simply run this:
```shell
pip install -r requirements.txt
```

If you decide a new package is required for whatever you are implementing, please remember to update the requirement.txt file. This can be done with this following command:
```shell
pip freeze > requirements.txt
```
