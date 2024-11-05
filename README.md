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
bash
Copy code
git clone <your-repo-url>
cd chocolate_house

2. Install Dependencies
First, make sure you have Python 3 and pip installed. Then install the necessary packages:

bash
pip install -r requirements.txt

3. Initialize the Database
Run the following command to create and initialize the SQLite database with the required tables:

bash
python database.py
This command will create a chocolate_house.db file in the project directory, containing three tables: Flavors, Ingredients, and CustomerFeedback.

Running the Application
To start the application, use:

bash
Copy code
python app.py
Follow the on-screen instructions to add flavors, list flavors, and manage other data.

Example Usage
Add Flavor: Enter a seasonal flavor name and season (e.g., Winter, Summer).
List Flavors: View all flavors currently in the database.
Docker Instructions
If you'd like to run the application in a Docker container, follow these steps.

1. Build the Docker Image
bash
Copy code
docker build -t chocolate-house .
2. Run the Docker Container
bash
Copy code
docker run -it chocolate-house
This command will start the application in an isolated environment.

Edge Case Handling
This application considers the following edge cases:

No Data in Tables: If there are no flavors or ingredients, the application will indicate that the tables are empty rather than crashing.
Invalid Input: The application sanitizes inputs to prevent SQL injection and other malicious entries.
Database Errors: If the database fails to initialize or connect, the application will output a friendly error message.
Code Structure
plaintext
Copy code
chocolate_house/
├── app.py                     # Main application logic
├── database.py                # Database initialization and management
├── models.py                  # CRUD functions
├── Dockerfile                 # Docker setup for the app
├── requirements.txt           # Dependencies
└── README.md                  # Documentation (this file)
app.py: Contains the main application logic.
database.py: Initializes and manages the SQLite database.
models.py: Handles CRUD (Create, Read, Update, Delete) operations.
Dockerfile: Used to build and run the application in Docker.
requirements.txt: Lists dependencies required by the application.
Testing the Application
Verify Database Initialization: After running database.py, check that chocolate_house.db has the necessary tables.
Functional Testing: Test each feature (adding flavors, listing flavors, etc.) to ensure correct behavior.
Edge Case Testing: Validate how the app handles no data, invalid inputs, and database errors.
Sample Commands for Testing
Initialize Database:

bash
Copy code
python database.py
Run Application:

bash
Copy code
python app.py
Docker Commands:

bash
Copy code
docker build -t chocolate-house .
docker run -it chocolate-house
