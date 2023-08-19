# Project Name

Ecommerce Using Django

## Prerequisites

List any prerequisites or dependencies that need to be installed before setting up the project. For example:

- Python (version 3.9.10)
- Django (version 4.2.4)
- Virtual environment

## Getting Started

Provide step-by-step instructions for setting up the project locally. Include the following:

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/your-project.git
   ```

2. **Navigate to the Project Directory:**

   ```bash
   cd your-project/
   ```

3. **Create a Virtual Environment (Optional but Recommended):**

   ```bash
   python -m venv venv
   ```

4. **Activate the Virtual Environment:**

   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

   - On macOS and Linux:

     ```bash
     source venv/bin/activate
     ```

5. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

6. **Run Database Migrations:**

   ```bash
   python manage.py migrate
   ```

7. **Create a Superuser (Admin Account):**

   ```bash
   python manage.py createsuperuser
   ```

8. **Run the Development Server:**

   ```bash
   python manage.py runserver
   ```

9. **Access the Project:**

   Open a web browser and go to [http://localhost:8000/](http://localhost:8000/) to access the project. You can access the admin interface at [http://localhost:8000/admin/](http://localhost:8000/admin/) using the superuser credentials.