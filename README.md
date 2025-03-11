# Django RestAPI Employee Management

## 🚀 Overview

This is a Django REST API for managing employees and companies, built using Django REST Framework (DRF). It provides a structured and scalable solution for handling employee records and company details with full CRUD operations.

## 🔥 Features

- ✅ RESTful API with Django REST Framework (DRF)
- ✅ CRUD operations for employees and companies
- ✅ Authentication & Permission handling
- ✅ Pagination & Filtering for large datasets
- ✅ Role-based access control
- ✅ API documentation using Swagger/OpenAPI

---

## 📌 Installation

### **1⃣ Clone the Repository**

```sh
https://github.com/aniketdoke35/Django_RestAPI_Employee_Company_Management.git
cd Django_RestAPI_Employee_Management
```

### **2⃣ Create and Activate a Virtual Environment**

```sh
python -m venv venv
source venv/bin/activate   # For macOS/Linux
venv\Scripts\activate      # For Windows
```

### **3⃣ Install Dependencies**

```sh
pip install -r requirements.txt
```

### **4⃣ Apply Migrations**

```sh
python manage.py makemigrations
python manage.py migrate
```

### **5⃣ Create a Superuser (For Admin Access)**

```sh
python manage.py createsuperuser
```

### **6⃣ Run the Development Server**

```sh
python manage.py runserver
```

The API will be available at:\
📞 **[http://127.0.0.1:8000/api/v1/](http://127.0.0.1:8000/api/v1/)**

---

## 📌 API Endpoints

### **🔹 Employee Endpoints**

| Method | Endpoint                  | Description               |
| ------ | ------------------------- | ------------------------- |
| GET    | `/api/v1/employees/`      | Get all employees         |
| POST   | `/api/v1/employees/`      | Create a new employee     |
| GET    | `/api/v1/employees/{id}/` | Retrieve employee details |
| PUT    | `/api/v1/employees/{id}/` | Update an employee        |
| DELETE | `/api/v1/employees/{id}/` | Delete an employee        |

### **🔹 Company Endpoints**

| Method | Endpoint                  | Description              |
| ------ | ------------------------- | ------------------------ |
| GET    | `/api/v1/companies/`      | Get all companies        |
| POST   | `/api/v1/companies/`      | Create a new company     |
| GET    | `/api/v1/companies/{id}/` | Retrieve company details |
| PUT    | `/api/v1/companies/{id}/` | Update a company         |
| DELETE | `/api/v1/companies/{id}/` | Delete a company         |

---

## 📌 Authentication & Permissions

This API uses Django authentication and role-based permissions. To access restricted endpoints:\
1⃣ **Login & Get Token:**

```sh
POST /api/token/
{
    "username": "admin",
    "password": "yourpassword"
}
```

2⃣ **Use Token in Requests:**\
Include the token in the headers of your API requests:

```sh
Authorization: Bearer your_access_token
```

---

## 📌 Technologies Used

- **Django** - Python web framework
- **Django REST Framework (DRF)** - API development
- **SQLite/PostgreSQL/MySQL** - Database
- **JWT Authentication** (if implemented)
- **Swagger/OpenAPI** - API documentation

---

## 📌 License

This project is open-source and available under the MIT License.

---

## 📌 Contributing

Contributions are welcome! Feel free to fork this repository, create a branch, and submit a pull request.

🙌 **Happy Coding!** 🚀

---

## 📌 Author

👨‍💻 **Aniket Doke**  
🌍 **Portfolio:** [aniketdoke35.netlify.app](https://aniketdoke35.netlify.app/)

