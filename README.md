# Wander QA Automation Project

# **Project Overview**
Wander is a web app created for [**Igrowker**](https://igrowker.com/) to connect travelers with locals offering unique, personalized experiences.

**Quality Assurance Contribution.**
As a member of the QA team, I am developing an automation framework tailored for this project, using [**Selenium Base**](https://seleniumbase.io/) (python-based testing library, to simplify web application test automation)

For this project, I am automating the following key processes:

1. **User Registration Automation**
	The automation for the user registration process includes the following scenarios:

	- Happy Path: Ensure the user can successfully complete the registration with valid data (username, email, password, etc.).

2. **User Login Automation**
	The automation for the user login process includes the following scenarios:

	- Valid Login: Ensure that a registered user can log in successfully with valid credentials.
	- Invalid Data: Test various cases with invalid data (e.g., invalid name, invalid password, empty fields).

	[ ] Not included in automation: Login Attempt with Unregistered Account

User Register Automation example:
![wander.gif](:/1de47302f5b04795a922b5ca88152736)

# **Project Structure**
```
wander
└─── pages
	│   login_page.py
	│   register_page.py

└─── report

└─── tests
	│   __init__.py
	|   test_login.py
	|   test_register.py
   
└─── .env
  
└─── requirements.text

```
- **pages**
  - `login_page.py`: Contains all the UI elements needed for the login page test.
  - `register_page.py`: Contains all the UI elements needed for the register page test.
- **report**
A directory is automatically created when running the command to generate the HTML report
  
- **tests**

	- `__init__.py`:  needed to initialize objects of a class (also called a constructor)
  - `test_login.py`: Contains only the login test script.
  - `test_register.py`: Contains only the register test script.

- `.env`: File added to the `.gitignore`. This file contains sensitive data (e.g., passwords).

- `requirements.tx`t: file containing all the requirements used in this project

# **Prerequisites**
You need to create or have access to the `.env` file, this file contains names, emails, passwords and other sensitive data.

# **Setting up the project environment**
1. Clone the Repository to your local machine
  `https://github.com/ZulemaArteaga/Wander.git`
2. Navigate to your folder
`cd/path/to/this/folder`
4. Create new environment
`conda create --name wander_env python=3.12.2`
5. Activate your environment
`conda activate wander_env`
 Note: when switching to another python projet
deactivate env : `deactivate`
7. Install seleniumbase
`pip install seleniumbase`
8. Insall all the necesary Python packages
	`pip install -r requirements.txt`

# **Runing tests commands**
 - To run all tests in the project
   `pytest`

- To run single test
`pytest tests/test_login.py`
`pytest tests/test_register.py `
# **Runing all tests and generate html report**
 - `pytest --html=report/report.html `# wander_igrowker_project
