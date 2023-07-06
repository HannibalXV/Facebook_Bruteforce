



# Facebook_Bruteforce
This code uses the Selenium library in Python to automate the process of logging into Facebook. It takes an email and a file containing a list of passwords as inputs. The code iterates through each password, fills in the email and password fields on the Facebook login page, submits the form, and checks if the login is successful. It prints a message indicating whether the login was successful or not.

 # Usage:
To use this code, follow these steps:

Install the Selenium library if you haven't already. You can use the command pip install selenium to install it.

Download the appropriate webdriver for your browser and operating system. In this code, it is using the Chrome webdriver.

Provide the path to the Chrome webdriver executable by setting the driver_path variable in the code. Replace "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Google Chrome" with the actual path to the Chrome driver on your system.

Create a password file containing a list of passwords to try. Each password should be on a separate line in the file.

Modify the example usage at the end of the code by providing your Facebook email and the path to the password file. Replace "Phone_Number" with your Facebook email and "Password\Path\pass.txt" with the actual path to your password file.

Run the code, and it will automate the login process, attempting each password from the file and printing the results.
