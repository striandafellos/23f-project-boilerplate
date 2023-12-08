This repository contains details for running 3 containers necessary to run our app. The containers include
- MySQL Instance
- Flask Application
- Local AppSmith Instance

Code for database creation as well as the insertion of sample data is included in the db folder. 
Flask App contains python code for the API routes, sorted by entity.

Our repository consists of:
- `db/TaskWiz` folder which contains all the MYSQL insert files that were produced from Mockaroo.
- `flask-app/src` folder which contains all the Python routes connections that define the GET, POST, PUT, and DELETE commands for each project entity.

To run the repository: 
- Start the Docker Engine.
- In a terminal or command prompt, navigate to the folder with the `docker-compose.yml` file.
- Build the images with `docker compose build`
- Start the containers with `docker compose up`.  To run in detached mode, run `docker compose up -d`. 

To use AppSmith locally:
- Enter url "localhost:8080" in browser.
- Input user information to login to AppSmith.
- The application UI can be found at [this repository](https://github.com/striandafellos/23f-Appsmith).

To view backend:
- Enter url "localhost:8001" in browser.
- Append each route which you would like to view to the end of the url.
    - For example, to view all tasks, the full url would be `localhost:8001/t/tasks`

**Link to presentation video:**
https://youtu.be/f4WszhiMmLo

