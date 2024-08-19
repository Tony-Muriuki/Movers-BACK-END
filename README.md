# Movers App

Overview
Movers App is a Flask-based web application designed to manage moving-related activities. It includes functionalities for user management, inventory tracking, move scheduling, mover services, and messaging between users. This app leverages Flask with SQLAlchemy for ORM, Flask-Migrate for database migrations, Flask-JWT-Extended for secure authentication, and Flask-CORS for handling cross-origin requests.

# Features

User Management: Register and manage users with different roles and approval statuses.
Inventory Management: Track and manage household items by user.
Move Management: Schedule and track moving activities with status updates.
Mover Management: Manage moving companies, their pricing, and availability.
Messaging System: Enable communication between users about their moves.

# Installation

To set up the Movers App on your local machine, follow these steps:

Clone the Repository

git clone https://github.com/Tony-Muriuki/Movers-BACK-END.git

cd movers-app

# Set Up a Virtual Environment

python -m venv venv
source venv/bin/activate # On Windows use venv\Scripts\activate

# Install Dependencies

pip install -r requirements.txt

# Configure Environment Variables

Create a .env file in the root directory with the following content:
FLASK_APP=routes.py
FLASK_ENV=development
DATABASE_URL=sqlite:///'sqlite:///movers.db'
JWT_SECRET_KEY=your_jwt_secret_key

Usage
Run Database Migrations

Initialize and upgrade the database schema with:

flask db upgrade

Start the Application

# Launch the Flask development server with:

flask run
By default, the application will be accessible at http://127.0.0.1:5555/.

Configuration
The application configuration is managed through the Config class in config.py.

# Contributing

Contributions to the Movers App are welcome! Please follow these steps:

Fork the repository.
Create a new branch for your feature or fix.
Make your changes and test them.
Submit a pull request with a clear description of your changes.

# License

This project is licensed under the MIT License. See the LICENSE file for details.

Contact
For any questions or inquiries, please contact kamandetonymuriuki@gmail.com.
