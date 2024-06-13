# T-Shirt Store CLI Application

## Project Description
The T-Shirt Store CLI Application is a command-line interface (CLI) e-commerce platform built using Python and SQLite. It allows users to browse, purchase, and rate T-shirts. Admin users can manage the store by adding, updating, and deleting T-shirts, as well as viewing all purchased and non-purchased T-shirts. The application follows object-oriented programming (OOP) principles and includes a robust database interaction layer using Python ORM methods.

## Table of Contents
- [Project Description](#project-description)
- [Project Objectives](#project-objectives)
- [Features](#features)
  - [User Features](#user-features)
  - [Admin Features](#admin-features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Dependencies](#dependencies)
- [Contributing](#contributing)
- [License](#license)

## Project Objectives
- Implement a Python CLI Application that meets specific requirements.
- Utilize Python ORM methods for database creation and modification.
- Include a data model with at least 2 model classes and 1 one-to-many relationship.
- Define property methods for adding appropriate constraints to each model class.
- Implement ORM methods (create, delete, get all, find by id) for each model class.
- Develop a CLI with menus for user interaction, input validation, and error handling.
- Adhere to OOP best practices, appropriate naming conventions, and project organization.

## Features
### User Features
- **Login:** Users can log in using their email and password.
- **View T-Shirts:** Users can view all available T-shirts with their prices.
- **Purchase T-Shirts:** Users can purchase T-shirts if their account balance is sufficient.
- **Rate T-Shirts:** Users can rate T-shirts they have purchased.

### Admin Features
- **Add T-Shirt:** Admins can add new T-shirts to the store.
- **Update T-Shirt:** Admins can update existing T-shirts.
- **Delete T-Shirt:** Admins can delete T-shirts from the store.
- **View All T-Shirts:** Admins can view all purchased and non-purchased T-shirts.

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/Felixmutuma/tshirt-store-cli.git
    cd tshirt-store-cli
    ```
2. Set up a virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```
3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4. Initialize the database:
    ```bash
    python -c "from data.database import initialize_db; initialize_db()"
    ```

## Usage
1. Run the application:
    ```bash
    python app.py
    ```
2. Follow the on-screen prompts to log in as a user or admin and perform the desired actions.

## Project Structure

ecommerce_app/
├── app.py
├── cli/
│ ├── init.py
│ ├── admin.py
│ ├── user.py
│ ├── auth.py
│ └── utils.py
├── models/
│ ├── init.py
│ ├── user.py
│ ├── admin.py
│ ├── account.py
│ └── tshirt.py
├── data/
│ ├── init.py
│ └── database.py
├── tests/
│ ├── init.py
│ └── test_app.py
├── requirements.txt
└── README.md


## Dependencies
- Python 3.x
- SQLite
- [Other dependencies listed in requirements.txt]

## Contributing
Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch: `git checkout -b feature-branch-name`.
3. Make your changes and commit them: `git commit -m 'Add new feature'`.
4. Push to the branch: `git push origin feature-branch-name`.
5. Submit a pull request.

