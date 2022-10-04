# Billing


Create a local folder django
C:\Users\shrishail\django>py -3 -m venv .venv

C:\Users\shrishail\django>
C:\Users\shrishail\django>.venv\scripts\activate

(.venv) C:\Users\shrishail\django>code ..

Open the project folder in VS Code by running code ., or by running VS Code and using the File > Open Folder command.
select the folder django 

In VS Code, open the Command Palette (View > Command Palette or (Ctrl+Shift+P)). Then select the Python: Select Interpreter command:

The command presents a list of available interpreters that VS Code can locate automatically (your list will vary; if you don't see the desired interpreter, see Configuring Python environments). 
From the list, select the virtual environment in your project folder that starts with ./.venv or .\.venv:

Run Terminal: Create New Terminal (Ctrl+Shift+`) from the Command Palette, which creates a terminal and automatically activates the virtual environment by running its activation script.

This should show 

Windows PowerShell
Copyright (C) Microsoft Corporation. All rights reserved.

Try the new cross-platform PowerShell https://aka.ms/pscore6

PS C:\Users\shrishail\django> & c:/Users/shrishail/django/.venv/Scripts/Activate.ps1
(.venv) PS C:\Users\shrishail\django> 



PS C:\Users\shrishail\django> & c:/Users/shrishail/django/.venv/Scripts/Activate.ps1
(.venv) PS C:\Users\shrishail\django> python -m pip install --upgrade pip
Requirement already satisfied: pip in c:\users\shrishail\django\.venv\lib\site-packages (21.2.4)
Collecting pip
  Using cached pip-21.3.1-py3-none-any.whl (1.7 MB)
Installing collected packages: pip
  Attempting uninstall: pip
    Found existing installation: pip 21.2.4
    Uninstalling pip-21.2.4:
      Successfully uninstalled pip-21.2.4
Successfully installed pip-21.3.1



(.venv) PS C:\Users\shrishail\django> python -m pip install django
Collecting django
  Using cached Django-4.0-py3-none-any.whl (8.0 MB)
Collecting sqlparse>=0.2.2
  Using cached sqlparse-0.4.2-py3-none-any.whl (42 kB)
Collecting asgiref<4,>=3.4.1
  Using cached asgiref-3.4.1-py3-none-any.whl (25 kB)
Collecting tzdata
  Using cached tzdata-2021.5-py2.py3-none-any.whl (339 kB)
Installing collected packages: tzdata, sqlparse, asgiref, django
Successfully installed asgiref-3.4.1 django-4.0 sqlparse-0.4.2 tzdata-2021.5

pip install django-utils-six # if utils six isnt installed

run server
python .\manage.py runserver



Admin Password
admin1
vitvittest
