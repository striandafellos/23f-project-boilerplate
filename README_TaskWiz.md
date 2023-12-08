This repository contains details for running 3 containers necessary to run our app. The containers include
- MySQL 
- Flask Application
- AppSmith Server

Code for database creation as well as the insertation of sample data is included in the db folder. 
Flask App contains python code for the API routes, sorted by entity.

To run the repository: 
- In a terminal or command prompt, navigate to the folder with the `docker-compose.yml` file.  
- Build the images with `docker compose build`
- Start the containers with `docker compose up`.  To run in detached mode, run `docker compose up -d`. 
To view the AppSmith UI:
- Enter url "localhost:8080" in browser. 
To view backend:
- Enter url "localhost:8001" in browser.
