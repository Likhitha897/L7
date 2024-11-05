Chocolate House Management Application
This application manages seasonal flavors, ingredient inventory, and customer feedback (including flavor suggestions and allergy concerns) for a fictional chocolate house. The app uses SQLite as its database.

Features
Manage seasonal flavor offerings.
Track ingredient inventory.
Collect customer flavor suggestions and allergy concerns.
Requirements
Python 3.7 or higher
SQLite (comes installed with Python)
Optional: Docker (for containerization)

Setup Instructions

1. Clone the Repository

cd chocolate_house

2. Install Dependencies
First, make sure you have Python 3 and pip installed. Then install the necessary packages:


pip install -r requirements.txt

3. Initialize the Database
Run the following command to create and initialize the SQLite database with the required tables:

python database.py
This command will create a chocolate_house.db file in the project directory, containing three tables: Flavors, Ingredients, and CustomerFeedback.

Running the Application
To start the application, use:


python app.py
Follow the on-screen instructions to add flavors, list flavors, and manage other data.

Example Usage
Add Flavor: Enter a seasonal flavor name and season (e.g., Winter, Summer).
List Flavors: View all flavors currently in the database.
Docker Instructions
If you'd like to run the application in a Docker container, follow these steps.

1. Build the Docker Image

docker build -t chocolate-house .
2. Run the Docker Container

docker run -it chocolate-house
This command will start the application in an isolated environment.



