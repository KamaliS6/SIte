Kamali Smith   
ID Number: A20245083  
Summer 2025 Internet and Web Programming  
Final Project  
6/27/2025

**How to set up and run the application locally:**

* Create a virtual environment and activate it  
* Install files and dependencies  
* Run the application   
* Open in your browser

**File Structure:**  
/static  
  /css           \# Stylesheets  
  /js            \# JavaScript files (AJAX, flash handling)  
  /pdf           \# Resume file  
/templates  
  base.html      \# Common layout  
  index.html     \# Home page  
  resume.html    \# Resume preview and download  
  projects.html  \# Projects listing  
  contact.html   \# Contact form  
  comments.html  \# Display comments  
  login.html     \# Login form  
  register.html  \# Registration form  
  Aboutme.html \#hobbies outside of tech  
app.py           \# Main Flask app  
forms.py         \# WTForms classes  
database.py      \# SQLite DB functions  
requirements.txt  
README.md

**Design:**  
I choose to use a clean black-and-white base with minimal visual clutter for easy readability and navigation to keep things simple but efficient. Subtle accents of green, yellow, and black reflect Jamaican cultural pride while maintaining a professional look. 

**Challenges:**  
First time using Flask, so learning how to set up routes, use templates, manage sessions, and interact with a database was a major learning curve.Managing dependencies like Flask-WTF, CSRFProtect, and werkzeug required a lot of trial and error to make sure everything worked. I also did not have much Javascript experience so implementing dynamic features and AJAX was tough. W3Schools and the slides in class were helpful for HTML, CSS, and JavaScript and Flask concepts.