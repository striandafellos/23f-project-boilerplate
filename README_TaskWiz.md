This repository contains details for running 3 containers necessary to run our app. The containers include
- MySQL 
- Flask Application
- AppSmith Server

Code for database creation as well as the insertation of sample data is included in the db folder. 
Flask App contains python code for the API routes, sorted by entity.

Our repository consists of:
- TaskWiz folder which contains all the MYSQL insert files that was produced from Mockaroo.
- flask-app/src folder which contains all the Python routes connections that define the GET, POST, PUT, and DELETE commands for each project entity.

To run the repository: 
- In a terminal or command prompt, navigate to the folder with the `docker-compose.yml` file.  
- Build the images with `docker compose build`
- Start the containers with `docker compose up`.  To run in detached mode, run `docker compose up -d`. 
To view the AppSmith UI:
- Enter url "localhost:8080" in browser. 
To view backend:
- Enter url "localhost:8001" in browser.

**Link to presentation video:**
https://youtu.be/f4WszhiMmLo

