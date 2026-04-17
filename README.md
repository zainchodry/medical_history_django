# MediVault - Medical History Management System

A comprehensive Django-based web application for managing medical records, appointments, prescriptions, and patient information in a healthcare setting.

## 🚀 Features

### User Management

- **Role-based Authentication**: Separate interfaces for doctors and patients
- **Secure Login System**: Email-based authentication with role-specific access
- **User Profiles**: Comprehensive profile management for all users

### Patient Management

- **Patient Records**: Complete patient information management
- **Medical History**: Detailed patient medical history tracking
- **Profile Management**: Patients can view and update their own information

### Appointment System

- **Appointment Booking**: Patients can schedule appointments online
- **Doctor Assignment**: Automatic assignment to available doctors
- **Conflict Prevention**: Prevents double-booking of time slots
- **Appointment Management**: View, update, and cancel appointments

### Medical Records

- **Record Management**: Comprehensive medical record keeping
- **Doctor Access**: Doctors can create and manage patient records
- **Patient Privacy**: Secure access controls for sensitive information

### Prescription Management

- **Prescription Creation**: Doctors can create prescriptions
- **Prescription Tracking**: Complete prescription history
- **Medication Details**: Detailed medication information and instructions

## 🛠️ Technology Stack

- **Backend**: Django 5.2.13
- **Database**: SQLite (development) / PostgreSQL (production recommended)
- **Frontend**: HTML5, CSS3, JavaScript
- **UI Framework**: Custom responsive design with modern CSS
- **Calendar Integration**: Flatpickr for date/time selection
- **Authentication**: Django's built-in authentication system

## 📋 Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- Virtual environment (recommended)

## 🔧 Installation

1. **Clone the repository**

   ```bash
   git clone <repository-url>
   cd medical_history_django
   ```

2. **Create and activate virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run database migrations**

   ```bash
   python manage.py migrate
   ```

5. **Create superuser (optional)**

   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**

   ```bash
   python manage.py runserver
   ```

7. **Access the application**
   - Open your browser and go to `http://127.0.0.1:8000`
   - Admin panel: `http://127.0.0.1:8000/admin`

## 📁 Project Structure

```
medical_history_django/
├── accounts/              # User authentication and profiles
├── appointments/          # Appointment booking and management
├── medical_records/       # Medical record management
├── patients/             # Patient information management
├── prescriptions/        # Prescription management
├── medical_history/      # Main Django project settings
├── static/               # Static files (CSS, JS, images)
├── templates/            # HTML templates
├── db.sqlite3           # SQLite database (development)
├── manage.py            # Django management script
├── requirements.txt     # Python dependencies
└── README.md           # Project documentation
```

## 🔐 User Roles & Permissions

### Doctor

- View and manage all patients
- Create and update medical records
- Create prescriptions
- View and manage appointments
- Access admin panel

### Patient

- View personal profile and medical history
- Book appointments
- View prescriptions
- Update personal information

## 🌟 Key Features Explained

### Appointment Booking

- Patients can book appointments with an intuitive calendar interface
- Automatic doctor assignment
- Conflict detection prevents double-booking
- Real-time validation

### Medical Records

- Comprehensive patient history tracking
- Secure access controls
- Doctor-only record creation and updates
- Patient privacy protection

### Prescription Management

- Detailed prescription creation
- Medication tracking
- Dosage and instruction management
- Prescription history

## 🔒 Security Features

- **Role-based access control**
- **CSRF protection** on all forms
- **Secure authentication** with email-based login
- **Data validation** on all user inputs
- **SQL injection prevention** through Django ORM

## 🚀 Deployment

### Production Checklist

- [ ] Set `DEBUG = False` in settings.py
- [ ] Configure `ALLOWED_HOSTS`
- [ ] Set secure `SECRET_KEY`
- [ ] Use PostgreSQL database
- [ ] Configure static files serving
- [ ] Set up proper logging
- [ ] Enable HTTPS
- [ ] Configure email settings

### Environment Variables

Create a `.env` file in the project root:

```env
SECRET_KEY=your-secret-key-here
DEBUG=False
ALLOWED_HOSTS=your-domain.com
DATABASE_URL=postgresql://user:password@localhost/dbname
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
```

## 🧪 Testing

Run the test suite:

```bash
python manage.py test
```

## 📊 Database Schema

The application uses the following main models:

- **User**: Extended Django user model with roles
- **Profile**: User profile information
- **Patient**: Patient-specific information
- **Appointment**: Appointment scheduling
- **MedicalRecord**: Medical history records
- **Prescription**: Medication prescriptions

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🆘 Support

For support and questions:

- Create an issue in the repository
- Contact the development team
- Check the documentation

## 🔄 Version History

### v1.0.0

- Initial release
- Basic user authentication
- Patient, appointment, and prescription management
- Medical records system
- Responsive UI design

---

**MediVault** - Secure, efficient, and user-friendly medical record management system.
