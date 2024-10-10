# **Capstone Website Project using Django**

This project is a website of a fake band which has a registration
feature and login feature before the pages are accessible.
This was an important step in learning to use Django effectively.
It also consolidated the use of git, dockers and sphinx for 
documentation. Please note that due to Git only being able to 
deploy static webpages that you must follow the installation 
process below in order to view the project.

## *Table of Content*
* Installation
* Usage

## **Installation** 

### **Clone repository**
The first step is to clone the repository to your device. To do this start your command prompt in the desired
directory and run 'git clone https://github.com/Ruhan-Cilliers/Capstone-task.git' to get the repository onto 
your local device. Follow the following steps depending on how you wish to deploy the program.

### **Deploying pages using your device:**
* Run your command prompt and run pip with 'requirements.txt' to install the necessary programs
* Run Python 'make migrations' in your CMD to ensure all the files are up to date
* Then run Python 'migrate' in your CMD to initialise the migrations
* Lastly type 'python run server' in your CMD to run the server from your console

### **Deploying the project using Docker:**
* Run your command prompt and run pip with 'requirements.txt' to ensure all the necessary programs are installed.
* Run docker build -t capstone-task and ensure your docker desktop app is open.
* After this type docker run -p 8000:8000 capstone-task to in your cmd to run the program on a website.
* Follow this link to view the program:
  http://localhost:8000

## **Usage**
This program is intended to be a demonstration of using Django. It includes a login page, a user registration page and various 
pages containing some info on the subject matter of the page. The recommended usage of this app is to run the server and 
use the site as if you were someone who wants to find info on a new band.
