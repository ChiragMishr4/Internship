# Flask PDF to JPEG Converter

In this project I used the Flask web framework to create my app. Upon launching the app, if the user isn't already logged in, they are treated with a login/sign-up page. Upon creating an account using the sign up page, the user has to log into their account to use the converter. I am storing the login details of all the users in a database using SQL Alchemy.

Once the user has selected the pdf file to upload, the pdf file get written to a MongoDB database using GridFS. I am using GridFS as it is better when it comes to handeling large files. Incase the user uploads a large file, the service speed won't be affected. The file also gets read from the MongoDB database and then each page in the pdf gets converted to a jpeg file and gets saved in a folder on the server. Then, using the shutil library, I convert that folder into a zip file and serve it on the server as a static file.

Upon clicking the "Convert Another PDF" button, all the old files that got saved on the server gets deleted and this process repeats itself when the next PDF is converted.



# Project Review

This project taught me alot about the python language and how it operates itself. I understood and learnt the concept of virtual enviornments and how useful they are. I also can say with confidence now that I am fluent when it comes to coding in Python and using Flask to make web apps. I also understood the difference between front-end dev, back-end dev and full stack dev. This has taught me the importance of UI/UX. This project was a great learning opportunity and I am greatful to have a chance to work on this project and with different databases and libraries. 