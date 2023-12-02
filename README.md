# PowerPulseGYM Website

PowerPulseGYM is a web application built with Django, designed for managing gym memberships, trainer information, and user profiles.

## Features

- User authentication (signup, login, logout)
- Membership enrollment
- Contact form for user inquiries
- User profiles
- Information about memberships, trainers, and the gym

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Arslanamin404/PowerPulseGYM.git
   ```

3. **Navigate to the project directory:**

   ```bash
   cd powerpulsegym
   ```
   
5. **Install the required dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

7. **Dont forget to setup your database (mysql/mysqlLite/oracle)**

8. **Apply migrations:**

   ```bash
   python manage.py migrate
   ```

10. **Create a superuser for admin access:**

   ```bash
   python manage.py createsuperuser
   ```
   
11. **Run the development server:**

    ```bash
    python manage.py runserver
    ```

The application will be accessible at http://localhost:8000/.


## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or create a pull request.


## License

This project is licensed under the [MIT License](PowerPulseGYM/LICENSE). Please see the [LICENSE](PowerPulseGYM/LICENSE) file for more details.


## Author

[Mohammad Arsalan Rather](mailto:arslanamin.org@gmail.com)
