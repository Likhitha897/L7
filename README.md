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

git clone <your-repo-url>
cd chocolate_house

2. Install Dependencies


pip install -r requirements.txt

3. Initialize the Database

python database.py
This command will create a chocolate_house.db file in the project directory, containing three tables: Flavors, Ingredients, and CustomerFeedback.

Running the Application
To start the application, use:

python app.py
Follow the on-screen instructions to add flavors, list flavors, and manage other data.

