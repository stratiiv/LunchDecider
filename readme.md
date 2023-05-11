# LunchDecider

LunchDecider is a web application that helps employees decide where to have lunch. It allows employees to vote for their preferred restaurants and view the voting results for the current day.

## Features

- User Registration: Employees can create an account and log in to the application.
- Restaurant Creation: Employees can add new restaurants to the system.
- Menu Creation: Employees can create menus for each restaurant, specifying the available items.
- Voting: Employees can vote for their preferred restaurant for the current day.
- Vote Results: The application displays the voting results for the current day, showing the restaurant with the highest number of votes.

## Technologies Used

- Python
- Django: Web framework used for backend development.
- Django REST framework: Toolkit for building RESTful APIs in Django.
- PostgreSQL: Relational database for storing application data.
- Docker: Containerization platform for easy deployment.
- Docker Compose: Tool for defining and running multi-container Docker applications.
- pytest: Testing framework for writing and executing tests.

## Getting Started

To run the LunchDecider application locally, follow these steps:

1. Clone the repository:
   `git clone https://github.com/stratiiv/LunchDecider.git`

2. Install Docker and Docker Compose if not already installed.

2. Build and run the Docker containers:
`'docker-compose up --build'`

4. Run migrations:
`docker-compose exec web python manage.py migrate`
5. Access the application in your web browser at http://localhost:8000

## Usage
* Create a user account to log in to the application.
* Add restaurants to the system through the "Add Restaurant" functionality.
* Create menus for each restaurant using the "Create Menu" feature.
* Vote for your preferred restaurant for the current day.
* View the voting results on the "Vote Results" page.
## Contributing
Contributions to the LunchDecider project are welcome! If you encounter any issues or have suggestions for improvements, please create a new issue or submit a pull request.