# JSEC_College_LMS

JSEC_College_LMS is a web application for managing online courses and learning materials specifically designed for JSEC College.

## Table of Contents

- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Features](#features)
- [Screenshots](#screenshots)
- [Testing](#testing)
- [Future Enhancements](#future-enhancements)
- [Contributing](#contributing)
- [Credits](#credits)
- [License](#license)
- [Contact](#contact)

## Technologies Used

- Python 3.9
- Django 3.2.5
- PostgreSQL 13.3
- HTML, CSS, JavaScript

## Installation

1. Clone the repository:` 

git clone [https://github.com/NagiPragalathan/JSEC\_College\_LMS.git](https://github.com/NagiPragalathan/JSEC_College_LMS.git)

 `2. Install dependencies:` 

pip install -r requirements.txt


 `3. (Optional) Create and activate a virtual environment:` 

python3 -m venv venv source venv/bin/activate

 ``4. Create a PostgreSQL database and update the database settings in `settings.py`.

5. Run database migrations:`` 

python manage.py migrate

 `6. Load initial data:` 

python manage.py loaddata fixtures/\*.json


 `7. Start the server:` 

python manage.py runserver

 `## Usage

1. Open the application in a web browser: [http://localhost:8000/](http://localhost:8000/)

2. Login with the following credentials:
- create the super user using 'python manage.py runserver'
- Email: admin@example.com
- Password: password

3. Create, edit, or delete courses, modules, and learning materials.

4. Assign instructors and students to courses.

5. View course progress and completion status.

## Features

- User authentication and authorization
- Course management (create, edit, delete)
- Module management (create, edit, delete)
- Learning material management (create, edit, delete)
- Instructor and student management (create, edit, delete)
- Course enrollment (assign instructors and students)
- Course progress tracking and completion status

## Screenshots

Include screenshots of the user interface and key features.

## Testing

- Run automated tests:` 

python manage.py test

 `- Manually test the application and report any issues or bugs.

## Future Enhancements

- Add user profile pages.
- Implement a notification system.
- Improve the user interface and user experience.

## Contributing

1. Fork the repository.
2. Create a new branch:` 

git checkout -b feature-name

`3. Make changes and commit them:` 

git commit -m "Add new feature"


`4. Push to the branch:` 

git push origin feature-name

`5. Create a pull request.`

## Credits

- [Nagi Pragalathan](https://github.com/NagiPragalathan)
- [jkokilaCSEP](https://github.com/jkokilaCSEP)
- [glorysherin](https://github.com/glorysherin)
- [MohanKumar](https://github.com/MohanKumarMurugan)

## License

This project is licensed under the MIT License.

## Contact

For questions, feedback, or support, please contact Nagi Pragalathan.`
