# Documentation

<style>
    h1 {
        border-bottom: 2px solid #3498db;
        padding-bottom: 10px;
        margin-bottom: 20px;
        font-size: 30px !important;
    }

    h2 {
        border-bottom: 1px solid #3498db;
        padding-bottom: 5px;
        margin-bottom: 15px;
        font-size :25px !important;
    }
    
    h3 {
        font-size:20px !important;
    }

    h4{
        font-size:15px !important;    
    }

    /* Styling for paragraphs */
    p {
        margin-bottom: 15px;
        font-size:15px !important;
    }

    /* Styling for lists */
    ul, ol {
        margin: 15px 0;
        padding-left: 20px;
    }

    ul li, ol li {
        margin-bottom: 10px;
        font-size:15px !important;
    }

    a:hover {
        text-decoration: underline;
    }

    /* Styling for code blocks */
    pre, code {
        border: 1px solid #ddd;
        font-size: 15px; !important;
    }

    /* Table of contents styling */
    #toc {
        margin-bottom: 20px;
        padding: 10px;
        border: 2px solid #ccc;
        border-radius: 5px;
        background-color: #cccccc;
        font-size: 12px!important;
    }

    summary {
        margin-bottom: 20px;
        padding: 10px;
        border: 2px solid #ccc;
        border-radius: 5px;
        background-color: #cccccc;
        font-size: 18px;
        font-weight: bold;
        cursor: pointer;
        padding: 5px;
        color: #2980b9;
    }

    #toc[open] summary {
        color: #2980b9;
    }

    summary:hover {
        color: #2980b9;
    }

    div.toc {
        margin-top: 10px;
        margin-left: 15px;
    }

    .toc a {
        text-decoration: none;
        color: #34495e;
        font-size: 14px;
    }

    .toc a:hover {
        text-decoration: underline;
        color: #2980b9;
    }

    .toc ul {
        list-style-type: none;
        padding-left: 20px;
    }

    .toc ul li {
        margin: 5px 0;
    }
</style>

<details id="toc">
<summary>Click to expand and see the contents of the documentation </summary>

<div class="toc">

# Contents

- [Flask Application Setup](#flask-application-setup)
    - [Flask Application Initialization](#flask-application-initialization-)
    - [Blueprint Registration](#blueprint-registration)
    - [Schema Registration](#schema-registration)
    - [Execution](#execution)

- [Docker Setup for Digital Hospital Application](#docker-setup-for-digital-hospital-application)
    - [Dockerfile](#dockerfile-)
    - [Docker Compose](#docker-compose)
        - [Services](#services)
        - [Volumes](#volumes)
    - [Running the Application](#running-the-application)

- [MongoDB Setup Script](#mongodb-setup-script)
    - [Database Connection](#database-connection)
    - [Collection Creation](#collection-creation)
    - [Initial Data Insertion](#initial-data-insertion)

- [Source Code Documentation](#-source-code-documentation)
    - [Entities Overview](#ds-hospital---entities-overview)
        - [Appointment Entity](#appointment-entity)
        - [Doctor Entity](#doctor-entity)
        - [Patient Entity](#patient-entity)
        - [User Entity](#user-entity)
        - [ResponseEntity Class](#responseentity-class)
        - [ResponseEntityBuilder Class](#responseentitybuilder-class)
        - [Specialization Enum](#specialization-enum)
        - [Data Transfer Objects (DTOs)](#ds-hospital---data-transfer-objects-dtos)
        - [Accept DTOs](#accept-dtos)
            - [ChangeAppointmentCostDto](#changeappointmentcostdto)
            - [ChangePasswordDto](#changepassworddto)
            - [SearchAppointmentDto](#searchappointmentdto)
        - [Send DTOs](#send-dtos)
            - [DoctorAppointmentDto](#doctorappointmentdto)
            - [DoctorDto](#doctordto)
            - [PatientAppointmentDto](#patientappointmentdto)
            - [PatientDetailedAppointmentDto](#patientdetailedappointmentdto)
            - [PatientDto](#patientdto)
            - [UserDto](#userdto)
    - [Controllers Overview](#ds-hospital---controllers-overview)
        - [Admin Controller](#admin-controller)
        - [Doctor Controller](#doctor-controller)
        - [Patient Controller](#patient-controller)
    - [Services Overview](#ds-hospital---services)
        - [AdminService](#adminservice)
        - [AppointmentService](#appointmentservice)
        - [DoctorService](#doctorservice)
        - [PatientService](#patientservice)
    - [Repositories Overview](#ds-hospital---repositories)
        - [AdminRepository](#adminrepository)
        - [PatientRepository](#patientrepository)
        - [DoctorRepository](#doctorrepository)
    - [Utils Overview](#ds-hospital---utils)
        - [AppointmentScheduler](#appointmentscheduler)
        - [DateTimeUtils](#datetimeutils)
        - [HTTP](#http)
        - [MongoDBConnection](#mongodbconnection)
        - [JWT](#jwt)
        - [ServiceException](#serviceexception)
        - [DatabaseException](#databaseexception)
        - [SchemaException](#schemaexception)
        - [Config](#config)
        - [Decorators](#decorators)

- [Example API Requests and Responses](#example-api-requests-and-responses)
    - [Admin REST API](#admin-api)
        - [[POST] Login](#login-3)
        - [[GET] Logout](#logout-3)
        - [[POST] Create Doctor](#create-doctor-1)
        - [[PUT] Update Doctor Password](#update-doctor-password-1)
        - [[DELETE] Delete Doctor](#delete-doctor-1)
        - [[DELETE] Delete Patient](#delete-patient-1)

    - [Doctor REST API](#admin-api)
        - [[POST] Login](#login-4)
        - [[GET] Logout](#logout-4)
        - [[PUT] Update Password](#update-password-1)
        - [[PUT] Update Appointment Cost](#update-appointment-cost-1)
        - [[GET] Fetch Appointments](#fetch-appointments-2)

    - [Patient REST API](#patient-api)
        - [[POST] Login](#login-5)
        - [[GET] Logout](#logout-5)
        - [[POST] Register](#register-1)
        - [[POST] Book Appointment](#book-appointment-1)
        - [[GET] Fetch Appointments](#fetch-appointments-3)
        - [[GET] Fetch Appointment's Details](#fetch-appointments-details)
        - [[DELETE] Cancel Appointment](#cancel-appointment-1)
- [Swagger Documentation](#swagger-documentation)
- [Unit Testing Documentation](#unit-testing)
- [Jenkins CI/CD](#jenkins-cicd)
- [SonarQube Code Analysis](#sonarqube-code-analysis)
- [Jenkins - SonarQube Documentation](#jenkins-pipelines-and-sonarqube-code-analysis)

</div>
</details>

---

# Flask Application Setup

### Technologies Used

- **Backend** Framework: Utilized Python and Flask as the backend framework for building RESTful APIs.
- **Database**: MongoDB was chosen as the database to store application data.
- **JWT (JSON Web Tokens)**: Employed JWT for secure authentication and authorization mechanisms.
- **Deployment**: Deployed the application using Docker for containerization.
- **Version Control**: Managed version control using Git and hosted the repository on GitHub for collaborative
  development.
- **Testing**: Implemented unit testing with frameworks like pytest and unittest for ensuring code quality and
  reliability.
- **Documentation**: Documented the project using Markdown for clear and structured documentation.
- **API Documentation**: Documented the API Endpoints using Swagger for clear and interactive documentation, and also
  dedicated a section in the Markdown documentation.
- **Optional**:
    - **Continuous Integration/Continuous Deployment (CI/CD)**: Set up CI/CD pipelines using Jenkins to automate the
      build and deployment process. There is a guide on how to.
    - **Code Quality and Coverage**: Set up Sonarqube server for code quality and coverage testing using docker. There
      is a guide on how to.

## Key Components

### Flask Application Initialization

**[app.py](app.py)**

- Initializes a Flask application instance.
- Configures the application for debugging and sets the host to `0.0.0.0` to make it accessible externally.

### Blueprint Registration

Registers the following blueprints with their respective URL prefixes:

- `AdminController` with the URL prefix `/admin`.
- `DoctorController` with the URL prefix `/doctor`.
- `PatientController` with the URL prefix `/patient`.

### Schema Registration

- Adds a custom validation schema named `is_specialization` to the `schema_registry`.

## Execution

- The application runs in debug mode, allowing for easier development and troubleshooting.

---

# Docker Setup for Digital Hospital Application

This Docker setup allows you to run the Digital Hospital application in a containerized environment. It uses Docker
Compose to manage multiple services.

## Key Components

### Dockerfile

**[DockerFile](Dockerfile)**

- **Base Image**: Uses `python:3.6` as the base image.
- **Dependencies**: Copies `requirements.txt` to the `/app` directory and installs the required Python packages.
- **Working Directory**: Sets the working directory to `/app`.
- **Application Code**: Copies the entire application code to the `/app` directory.

---

### Docker Compose

**[Docker Compose](docker-compose.yml)**

Docker Compose is used to manage the application and its dependencies.

#### Services

1. **web**:
    - **Build Context**: Builds the image from the Dockerfile in the current directory.
    - **Container Name**: Names the container `flask`.
    - **Command**: Runs `app.py` using Python.
    - **Ports**: Maps port `5000` of the container to port `5000` on the host.
    - **Volumes**: Mounts the current directory to `/app` inside the container, allowing live code changes.
    - **Depends On**: Ensures the `mongodb` service is started before the `web` service.

2. **mongodb**:
    - **Image**: Uses the latest `mongo` image.
    - **Restart Policy**: Always restarts the container if it stops.
    - **Container Name**: Names the container `mongodb`.
    - **Environment Variables**: Sets the initial database to `DigitalHospital`.
    - **Ports**: Maps port `27017` of the container to port `27017` on the host.
    - **Volumes**:
        - Mounts the `./mongo-data` directory to `/data/db` inside the container for persistent storage.
        - Mounts the `./mongo-init.js` file to `/docker-entrypoint-initdb.d/mongo-init.js` to initialize the database.

#### Volumes

- **mongo-data**: A named volume used to persist MongoDB data.

---

### Running the Application

To build and run the application using Docker Compose, use the following command:

```sh
docker-compose up --build
```

---

# MongoDB Setup Script

**[Init DB](mongo-init.js)**

This script initializes the MongoDB database for the Digital Hospital application. It creates the necessary collections
and inserts initial data.

## Key Components

### Database Connection

- Connects to the MongoDB instance running on `localhost` at port `27017`.
- The database used is `DigitalHospital`.

### Collection Creation

The following collections are created:

- `admin`: Stores administrative user information.
- `doctors`: Stores information about doctors.
- `patients`: Stores patient information.
- `appointments`: Stores appointment details.

### Initial Data Insertion

Inserts initial data into the `admin` collection:

- Adds an administrative user with the username `admin` and password `@dm1n`.

---

<details>
<summary>Source Code Documentation</summary>
<div>

# Source Code Documentation

# DS Hospital - Entities Overview

This repository contains Python entities that represent different aspects of the application's domain model. Each entity
encapsulates data and functionality related to specific entities like appointments, doctors, patients, and users.

## Appointment Entity

**[Appointment Entity](src/entities/Appointment.py)**

The `Appointment` entity represents an appointment between a doctor and a patient.

### Attributes

- `_id`: Identifier of the appointment.
- `cid`: Generated ID for the appointment.
- `doctor_username`: Username of the doctor.
- `patient_username`: Username of the patient.
- `patient_name`: First name of the patient.
- `patient_surname`: Last name of the patient.
- `doctor_name`: First name of the doctor.
- `doctor_surname`: Last name of the doctor.
- `appointment_date`: Date of the appointment.
- `appointment_time`: Time of the appointment.
- `reason`: Reason for the appointment.
- `cost`: Cost of the appointment.
- `specialization`: Specialization of the doctor.

### Methods

#### combined(doctor, patient, search)

- **Description**: Combines data from `DoctorDto`, `PatientDto`, and `SearchAppointmentDto` to create a
  new `Appointment` instance.
- **Parameters**:
    - `doctor`: Instance of `DoctorDto`.
    - `patient`: Instance of `PatientDto`.
    - `search`: Instance of `SearchAppointmentDto`.
- **Returns**: New `Appointment` instance.

#### to_dict()

- **Description**: Converts the `Appointment` object to a dictionary.
- **Returns**: Dictionary representation of the `Appointment`.

---

## Doctor Entity

**[Doctor Entity](src/entities/Doctor.py)**

The `Doctor` entity represents a doctor in the system.

### Attributes

- `username`: Username of the doctor.
- `password`: Password of the doctor.
- `email`: Email address of the doctor.
- `first_name`: First name of the doctor.
- `last_name`: Last name of the doctor.
- `specialization`: Specialization of the doctor.
- `appointment_cost`: Cost of appointments for the doctor.

### Methods

#### to_db()

- **Description**: Converts the `Doctor` object to a format suitable for database storage.
- **Returns**: Dictionary representation of the `Doctor` for database insertion.

#### to_register()

- **Description**: Converts the `Doctor` object to a format suitable for registration purposes.
- **Returns**: Dictionary representation of the `Doctor` for registration.

---

## Patient Entity

**[Patient Entity](src/entities/Patient.py)**

The `Patient` entity represents a patient in the system.

### Attributes

- `username`: Username of the patient.
- `password`: Password of the patient.
- `email`: Email address of the patient.
- `first_name`: First name of the patient.
- `last_name`: Last name of the patient.
- `amka`: AMKA (Social Security Number) of the patient.
- `date_of_birth`: Date of birth of the patient.

### Methods

#### to_db()

- **Description**: Converts the `Patient` object to a format suitable for database storage.
- **Returns**: Dictionary representation of the `Patient` for database insertion.

#### to_register()

- **Description**: Converts the `Patient` object to a format suitable for registration purposes.
- **Returns**: Dictionary representation of the `Patient` for registration.

#### validate()

- **Description**: Validates the registration data of the `Patient`.
- **Returns**: Result of the validation.

---

## User Entity

**[User Entity](src/entities/User.py)**

The `User` entity represents a user for authentication purposes.

### Attributes

- `username`: Username of the user.
- `password`: Password of the user.

### Methods

#### to_dict()

- **Description**: Converts the `User` object to a dictionary.
- **Returns**: Dictionary representation of the `User`.

#### validate()

- **Description**: Validates the login data of the `User`.
- **Returns**: Result of the validation.

---

## ResponseEntity Class

**[ResponseEntity Entity](src/entities/ResponseEntity.py)**

The `ResponseEntity` class helps construct HTTP responses in a structured manner.

### Methods

#### builder()

- **Description**: Returns a new `ResponseEntityBuilder` instance to build a response.

---

## ResponseEntityBuilder Class

**[ResponseEntity Entity](src/entities/ResponseEntity.py)**

The `ResponseEntityBuilder` class facilitates the construction of `ResponseEntity` objects.

### Methods

#### with_status(status)

- **Description**: Sets the status of the response.

#### with_data(data)

- **Description**: Sets the data of the response.

#### with_content_type(content_type)

- **Description**: Sets the content type of the response.

#### build()

- **Description**: Constructs the `ResponseEntity` object with configured data and status.

---

## Specialization Enum

**[Specialization Entity](src/entities/Specialization.py)**

The `Specialization` enum defines various medical specializations.

### Enum Values

- `RADIOLOGIST`
- `HEMATOLOGIST`
- `ALLERGIST`
- `PATHOLOGIST`
- `CARDIOLOGIST`

Each enum value corresponds to a specific medical specialization.

---

---

# DS Hospital - Data Transfer Objects (DTOs)

This repository contains Python DTOs used for transferring data between different layers of the application. DTOs
encapsulate data related to specific operations or responses.

## Accept DTOs

### ChangeAppointmentCostDto

**[ChangeAppointmentCost Dto](src/transfer/accept/ChangeAppointmentCostDto.py)**

Represents data for changing appointment cost.

#### Attributes

- `username`: Username of the entity.
- `old_cost`: Old cost of the appointment.
- `new_cost`: New cost of the appointment.

#### Methods

##### to_dict()

Converts the DTO object to a dictionary.

---

### ChangePasswordDto

**[ChangePassword Dto](src/transfer/accept/ChangePasswordDto.py)**

Represents data for changing passwords.

#### Attributes

- `username`: Username of the entity.
- `old_password`: Old password.
- `new_password`: New password.

#### Methods

##### to_dict()

Converts the DTO object to a dictionary.

---

### SearchAppointmentDto

**[SearchAppointment Dto](src/transfer/accept/SearchAppointmentDto.py)**

Represents data for searching appointments.

#### Attributes

- `reason`: Reason for the appointment.
- `specialization`: Specialization required.
- `appointment_date`: Date of the appointment.
- `appointment_time`: Time of the appointment.

#### Methods

##### to_dict()

Converts the DTO object to a dictionary.

## Send DTOs

### DoctorAppointmentDto

**[DoctorAppointment Dto](src/transfer/send/DoctorAppointmentDto.py)**

Represents data sent for doctor appointments.

#### Attributes

- `patient_name`: Patient's first name.
- `patient_surname`: Patient's last name.
- `appointment_date`: Date of the appointment.
- `appointment_time`: Time of the appointment.
- `reason`: Reason for the appointment.

#### Methods

##### to_dict()

Converts the DTO object to a dictionary.

---

### DoctorDto

Represents data sent for doctors.

#### Attributes

- `cid`: ID of the doctor.
- `username`: Username of the doctor.
- `email`: Email address of the doctor.
- `first_name`: First name of the doctor.
- `last_name`: Last name of the doctor.
- `specialization`: Specialization of the doctor.
- `appointment_cost`: Cost of appointments for the doctor.

#### Methods

##### to_dict()

Converts the DTO object to a dictionary.

---

### PatientAppointmentDto

**[PatientDoctorAppointment Dto](src/transfer/send/PatientAppointmentDto.py)**

Represents data sent for patient appointments.

#### Attributes

- `doctor_name`: Doctor's first name.
- `doctor_surname`: Doctor's last name.
- `appointment_date`: Date of the appointment.
- `appointment_time`: Time of the appointment.

#### Methods

##### to_dict()

Converts the DTO object to a dictionary.

---

### PatientDetailedAppointmentDto

**[PatientDetailedAppointment Dto](src/transfer/send/PatientDetailedAppointmentDto.py)**

Represents detailed data sent for patient appointments.

#### Attributes

- `doctor_name`: Doctor's first name.
- `doctor_surname`: Doctor's last name.
- `appointment_date`: Date of the appointment.
- `appointment_time`: Time of the appointment.
- `specialization`: Specialization of the doctor.
- `cost`: Cost of the appointment.
- `reason`: Reason for the appointment.

#### Methods

##### to_dict()

Converts the DTO object to a dictionary.

---

### PatientDto

**[Patient Dto](src/transfer/send/PatientDto.py)**

Represents data sent for patients.

#### Attributes

- `cid`: ID of the patient.
- `username`: Username of the patient.
- `email`: Email address of the patient.
- `first_name`: First name of the patient.
- `last_name`: Last name of the patient.
- `amka`: AMKA (Social Security Number) of the patient.
- `date_of_birth`: Date of birth of the patient.

#### Methods

##### to_dict()

Converts the DTO object to a dictionary.

---

### UserDto

Represents data sent for users.

#### Attributes

- `username`: Username of the user.
- `token`: Token associated with the user.

#### Methods

##### to_dict()

Converts the DTO object to a dictionary.


---

---

# DS Hospital - Controllers Overview

This repository contains Flask controllers that handle different user roles and operations within the application. Each
controller defines routes and endpoints for specific functionalities related to administrators, doctors, and patients.

## Admin Controller

**[Admin Controller](src/controllers/AdminController.py)**

The `AdminController.py` file implements Flask routes specifically designed for administrative tasks within the
application.

### Endpoints and Functionalities

#### Login

- **Route**: `/login`
- **Method**: POST
- **Description**: Allows administrators to authenticate themselves.
- **Decorators**: `handle_exceptions`
- **Secret Key**: `Config.ADMIN_SECRET_KEY`

#### Logout

- **Route**: `/logout`
- **Method**: GET
- **Description**: Logs out administrators and removes their session token.
- **Decorators**: `remove_token`
- **Secret Key**: `Config.ADMIN_SECRET_KEY`

#### Create Doctor

- **Route**: `/create_doctor`
- **Method**: POST
- **Description**: Creates a new doctor profile.
- **Decorators**: `token_required`
- **Secret Key**: `Config.ADMIN_SECRET_KEY`

#### Update Doctor Password

- **Route**: `/update_doctor_password`
- **Method**: PUT
- **Description**: Updates the password for a doctor profile.
- **Decorators**: `token_required`
- **Secret Key**: `Config.ADMIN_SECRET_KEY`

#### Delete Doctor

- **Route**: `/delete_doctor/<username>`
- **Method**: DELETE
- **Description**: Deletes a specific doctor profile.
- **Decorators**: `token_required`
- **Secret Key**: `Config.ADMIN_SECRET_KEY`

#### Delete Patient

- **Route**: `/delete_patient/<username>`
- **Method**: DELETE
- **Description**: Deletes a specific patient profile.
- **Decorators**: `token_required`
- **Secret Key**: `Config.ADMIN_SECRET_KEY`

---

## Doctor Controller

**[Doctor Controller](src/controllers/DoctorController.py)**

The `DoctorController.py` file defines Flask routes specifically for interactions involving doctors.

### Endpoints and Functionalities

#### Login

- **Route**: `/login`
- **Method**: POST
- **Description**: Allows doctors to log in to their accounts.
- **Secret Key**: `Config.DOCTOR_SECRET_KEY`

#### Logout

- **Route**: `/logout`
- **Method**: GET
- **Description**: Logs out doctors and removes their session token.
- **Decorators**: `remove_token`
- **Secret Key**: `Config.DOCTOR_SECRET_KEY`

#### Update Password

- **Route**: `/update_password`
- **Method**: PUT
- **Description**: Updates the password for a doctor account.
- **Decorators**: `token_required`
- **Secret Key**: `Config.DOCTOR_SECRET_KEY`

#### Update Appointment Cost

- **Route**: `/update_appointment_cost`
- **Method**: PUT
- **Description**: Updates the cost of appointments for a doctor.
- **Decorators**: `token_required`
- **Secret Key**: `Config.DOCTOR_SECRET_KEY`

#### Fetch Appointments

- **Route**: `/appointments`
- **Method**: GET
- **Description**: Retrieves a list of appointments for a doctor.
- **Decorators**: `token_required`
- **Secret Key**: `Config.DOCTOR_SECRET_KEY`

---

## Patient Controller

**[Patient Controller](src/controllers/PatientController.py)**

The `PatientController.py` file implements Flask routes focused on patient-related operations.

### Endpoints and Functionalities

#### Login

- **Route**: `/login`
- **Method**: POST
- **Description**: Allows patients to authenticate themselves.
- **Secret Key**: `Config.PATIENT_SECRET_KEY`

#### Register

- **Route**: `/register`
- **Method**: POST
- **Description**: Registers a new patient in the system.
- **Secret Key**: `Config.PATIENT_SECRET_KEY`

#### Logout

- **Route**: `/logout`
- **Method**: GET
- **Description**: Logs out patients and removes their session token.
- **Decorators**: `remove_token`
- **Secret Key**: `Config.PATIENT_SECRET_KEY`

#### Book Appointment

- **Route**: `/book_appointment`
- **Method**: POST
- **Description**: Allows patients to book appointments.
- **Decorators**: `token_required`
- **Secret Key**: `Config.PATIENT_SECRET_KEY`

#### Fetch Appointments

- **Route**: `/appointments`
- **Method**: GET
- **Description**: Retrieves a list of appointments for a patient.
- **Decorators**: `token_required`
- **Secret Key**: `Config.PATIENT_SECRET_KEY`

#### Appointment Details

- **Route**: `/appointment/<appointment_id>`
- **Method**: GET
- **Description**: Retrieves details of a specific appointment for a patient.
- **Decorators**: `token_required`
- **Secret Key**: `Config.PATIENT_SECRET_KEY`

#### Cancel Appointment

- **Route**: `/cancel_appointment/<appointment_id>`
- **Method**: DELETE
- **Description**: Cancels a specific appointment for a patient.
- **Decorators**: `token_required`
- **Secret Key**: `Config.PATIENT_SECRET_KEY`

---

---

---

# DS Hospital - Services

This repository contains Python services responsible for business logic and interactions with repositories. Services
orchestrate operations between entities, repositories, and DTOs.

## AdminService

**[Admin Service](src/services/AdminService.py)**

Handles administrative operations such as login, logout, doctor management, etc.

### Methods

#### login(auth_data: User)

Logs in an admin user.

- **Parameters:**
    - `auth_data`: User object containing username and password.

- **Returns:**
    - Dictionary containing user information and token upon successful login.

- **Raises:**
    - `ServiceException`: If login fails.

#### logout(token)

Logs out an admin user.

- **Parameters:**
    - `token`: Token to be invalidated.

- **Returns:**
    - Boolean indicating successful logout.

- **Raises:**
    - `ServiceException`: If logout fails.

#### delete_doctor(username)

Deletes a doctor from the system.

- **Parameters:**
    - `username`: Username of the doctor to delete.

- **Returns:**
    - Boolean indicating successful deletion.

- **Raises:**
    - `ServiceException`: If deletion fails.

#### update_doctor_password(data: ChangePasswordDto)

Updates the password of a doctor.

- **Parameters:**
    - `data`: ChangePasswordDto object containing username, old password, and new password.

- **Returns:**
    - Boolean indicating successful password update.

- **Raises:**
    - `ServiceException`: If password update fails.

#### create_doctor(data: Doctor)

Creates a new doctor in the system.

- **Parameters:**
    - `data`: Doctor object containing doctor details.

- **Returns:**
    - Dictionary containing the newly created doctor's information.

- **Raises:**
    - `ServiceException`: If creation fails due to existing doctor with the same username or email.

#### delete_patient(username)

Deletes a patient from the system.

- **Parameters:**
    - `username`: Username of the patient to delete.

- **Returns:**
    - Boolean indicating successful deletion.

- **Raises:**
    - `ServiceException`: If deletion fails.

## AppointmentService

**[Appointments Service](src/services/AppointmentsService.py)**

Manages operations related to appointments such as checking availability, booking appointments, fetching appointments,
etc.

### Methods

#### check_time(appointment_time)

Checks if the appointment time is within working hours.

- **Parameters:**
    - `appointment_time`: Time of the appointment.

- **Returns:**
    - Boolean indicating if the time is within working hours.

#### check_date(appointment_date)

Checks if the appointment date is within a valid range.

- **Parameters:**
    - `appointment_date`: Date of the appointment.

- **Returns:**
    - Boolean indicating if the date is valid.

#### check_availability(doctor_username, appointment_date)

Checks the availability of slots for a given doctor and appointment date.

- **Parameters:**
    - `doctor_username`: Username of the doctor.
    - `appointment_date`: Date of the appointment.

- **Returns:**
    - List of available appointment slots.

#### find_appointments(data: SearchAppointmentDto)

Finds available appointments based on search criteria.

- **Parameters:**
    - `data`: SearchAppointmentDto object containing search criteria.

- **Returns:**
    - DoctorDto object representing the doctor with available appointments, or None if no appointments are found.

#### return_appointments(free_appointments)

Converts free appointment slots to a list of strings.

- **Parameters:**
    - `free_appointments`: List of free appointment slots.

- **Returns:**
    - List of appointment slots as strings.

#### return_doctors(doctors)

Converts a list of doctor entities to a list of DoctorDto objects.

- **Parameters:**
    - `doctors`: List of doctor entities.

- **Returns:**
    - List of DoctorDto objects.

## DoctorService

**[Doctor Service](src/services/DoctorService.py)**

Handles operations specific to doctors such as login, logout, updating password, managing appointments, etc.

### Methods

#### login(auth_data: User)

Logs in a doctor.

- **Parameters:**
    - `auth_data`: User object containing username and password.

- **Returns:**
    - Dictionary containing login status message and token upon successful login.

- **Raises:**
    - `ServiceException`: If login fails.

#### logout(token)

Logs out a doctor.

- **Parameters:**
    - `token`: Token to be invalidated.

- **Returns:**
    - Dictionary indicating successful logout.

- **Raises:**
    - `ServiceException`: If logout fails.

#### update_password(current_user, data: ChangePasswordDto)

Updates the password of the logged-in doctor.

- **Parameters:**
    - `current_user`: Username of the logged-in doctor.
    - `data`: ChangePasswordDto object containing old password and new password.

- **Returns:**
    - Dictionary indicating successful password update.

- **Raises:**
    - `ServiceException`: If password update fails.

#### update_appointment_cost(current_user, data: ChangeAppointmentCostDto)

Updates the appointment cost for a doctor.

- **Parameters:**
    - `current_user`: Username of the logged-in doctor.
    - `data`: ChangeAppointmentCostDto object containing username, old cost, and new cost.

- **Returns:**
    - Dictionary indicating successful appointment cost update.

- **Raises:**
    - `ServiceException`: If appointment cost update fails.

#### fetch_appointments(current_user)

Fetches appointments of the logged-in doctor.

- **Parameters:**
    - `current_user`: Username of the logged-in doctor.

- **Returns:**
    - Dictionary containing fetched appointments.

#### get_as_appointments(appointments)

Converts a list of appointment entities to DoctorAppointmentDto objects.

- **Parameters:**
    - `appointments`: List of appointment entities.

- **Returns:**
    - List of DoctorAppointmentDto objects.

## PatientService

**[Patient Service](src/services/PatientService.py)**

Manages operations related to patients such as registration, login, appointment booking, fetching appointments, etc.

### Methods

#### register(data: Patient)

Registers a new patient in the system.

- **Parameters:**
    - `data`: Patient object containing patient details.

- **Returns:**
    - Dictionary containing patient information, and token upon successful registration.

- **Raises:**
    - `ServiceException`: If registration fails due to existing patient with the same username or email.

#### login(auth_data: User)

Logs in a patient.

- **Parameters:**
    - `auth_data`: User object containing username and password.

- **Returns:**
    - Dictionary containing username and token upon successful login.

- **Raises:**
    - `ServiceException`: If login fails.

#### logout(token)

Logs out a patient.

- **Parameters:**
    - `token`: Token to be invalidated.

- **Returns:**
    - Dictionary indicating successful logout.

- **Raises:**
    - `ServiceException`: If logout fails.

#### book_appointment(current_user, data: SearchAppointmentDto)

Books an appointment for a patient.

- **Parameters:**
    - `current_user`: Username of the logged-in patient.
    - `data`: SearchAppointmentDto object containing appointment details.

- **Returns:**
    - Dictionary containing appointment information upon successful booking.

- **Raises:**
    - `ServiceException`: If booking fails.

#### fetch_appointments(current_user)

Fetches appointments of the logged-in patient.

- **Parameters:**
    - `current_user`: Username of the logged-in patient.

- **Returns:**
    - Dictionary containing fetched appointments.

#### fetch_appointment_details(current_user, appointment_id)

Fetches details of a specific appointment for the logged-in patient.

- **Parameters:**
    - `current_user`: Username of the logged-in patient.
    - `appointment_id`: ID of the appointment to fetch details for.

- **Returns:**
    - Dictionary containing fetched appointment details.

#### cancel_appointment(current_user, appointment_id)

Cancels an appointment for the logged-in patient.

- **Parameters:**
    - `current_user`: Username of the logged-in patient.
    - `appointment_id`: ID of the appointment to cancel.

- **Returns:**
    - Dictionary indicating successful cancellation.

- **Raises:**
    - `ServiceException`: If cancellation fails.

---

# DS Hospital - Repositories

This repository contains Python classes responsible for database interactions using MongoDB. Repositories handle CRUD
operations for entities and ensure data persistence.

## AdminRepository

**[Admin Repository](src/repositories/AdminRepository.py)**

Handles database operations related to admin users.

### Methods

#### login(auth_data: User)

Logs in an admin user.

- **Parameters:**
    - `auth_data`: User object containing username and password.

- **Returns:**
    - Admin entity if login successful, None otherwise.

#### create_doctor(data)

Creates a new doctor in the database.

- **Parameters:**
    - `data`: Dictionary containing doctor details.

- **Returns:**
    - Doctor entity if creation successful, None otherwise.

#### delete_doctor(username)

Deletes a doctor from the database.

- **Parameters:**
    - `username`: Username of the doctor to delete.

- **Returns:**
    - Boolean indicating successful deletion.

#### update_doctor_password(data: ChangePasswordDto)

Updates the password of a doctor in the database.

- **Parameters:**
    - `data`: ChangePasswordDto object containing username, old password, and new password.

- **Returns:**
    - Boolean indicating successful password update.

#### delete_patient(username)

Deletes a patient from the database.

- **Parameters:**
    - `username`: Username of the patient to delete.

- **Returns:**
    - Boolean indicating successful deletion.

#### doctor_exists(data: Doctor)

Checks if a doctor with the same username or email exists in the database.

- **Parameters:**
    - `data`: Doctor object containing doctor details.

- **Returns:**
    - Doctor entity if exists, None otherwise.

---

## PatientRepository

**[Patient Repository](src/repositories/PatientRepository.py)**

Handles database operations related to patients and appointments.

### Methods

#### register(data)

Registers a new patient in the database.

- **Parameters:**
    - `data`: Dictionary containing patient details.

- **Returns:**
    - Patient entity if registration successful, None otherwise.

#### login(auth_data: User)

Logs in a patient.

- **Parameters:**
    - `auth_data`: User object containing username and password.

- **Returns:**
    - Patient entity if login successful, None otherwise.

#### book_appointment(appointment)

Books a new appointment in the database.

- **Parameters:**
    - `appointment`: Dictionary containing appointment details.

- **Returns:**
    - Appointment entity if booking successful, None otherwise.

#### fetch_appointments(patient_username)

Fetches all appointments of a patient from the database.

- **Parameters:**
    - `patient_username`: Username of the patient.

- **Returns:**
    - List of appointment entities.

#### fetch_appointment_details(username, appointment_id)

Fetches details of a specific appointment for a patient.

- **Parameters:**
    - `username`: Username of the patient.
    - `appointment_id`: ID of the appointment.

- **Returns:**
    - Appointment entity if found, None otherwise.

#### cancel_appointment(current_user, appointment_id)

Cancels a patient's appointment from the database.

- **Parameters:**
    - `current_user`: Username of the patient.
    - `appointment_id`: ID of the appointment.

- **Returns:**
    - Boolean indicating successful cancellation.

#### find_by_username(username)

Finds a patient by their username in the database.

- **Parameters:**
    - `username`: Username of the patient.

- **Returns:**
    - Patient entity if found, None otherwise.

#### exists(data: Patient)

Checks if a patient with the same username or email exists in the database.

- **Parameters:**
    - `data`: Patient object containing patient details.

- **Returns:**
    - Patient entity if exists, None otherwise.

---

## DoctorRepository

**[Doctor Repository](src/repositories/DoctorRepository.py)**

Handles database operations related to doctors and appointments.

### Methods

#### login(auth_data: User)

Logs in a doctor.

- **Parameters:**
    - `auth_data`: User object containing username and password.

- **Returns:**
    - Doctor entity if login successful, None otherwise.

#### update_password(username, data: ChangePasswordDto)

Updates the password of a doctor in the database.

- **Parameters:**
    - `username`: Username of the doctor.
    - `data`: ChangePasswordDto object containing old password and new password.

- **Returns:**
    - Boolean indicating successful password update.

#### update_appointment_cost(username, data: ChangeAppointmentCostDto)

Updates the appointment cost for a doctor in the database.

- **Parameters:**
    - `username`: Username of the doctor.
    - `data`: ChangeAppointmentCostDto object containing old cost and new cost.

- **Returns:**
    - Boolean indicating successful appointment cost update.

#### fetch_appointments(doctor_username)

Fetches all appointments of a doctor from the database.

- **Parameters:**
    - `doctor_username`: Username of the doctor.

- **Returns:**
    - List of appointment entities.

#### fetch_appointments_by_date(doctor_username, appointment_date)

Fetches appointments of a doctor for a specific date from the database.

- **Parameters:**
    - `doctor_username`: Username of the doctor.
    - `appointment_date`: Date of the appointments.

- **Returns:**
    - List of appointment entities.

#### find_by_role(data: SearchAppointmentDto)

Finds doctors by their specialization in the database.

- **Parameters:**
    - `data`: SearchAppointmentDto object containing specialization.

- **Returns:**
    - List of doctor entities.

---

---

# DS Hospital - Utils

This repository contains utility classes and functions used across the project for various purposes like handling dates,
JWT tokens, HTTP status codes, database connections, and more.

## AppointmentScheduler

**[Appointment Scheduler](src/utils/AppointmentScheduler.py)**

Provides utilities related to appointment scheduling.

### Methods

#### is_within_working_hours(appointment_time)

Checks if the given appointment time is within the working hours.

- **Parameters:**
    - `appointment_time`: Time object representing the appointment time.

- **Returns:**
    - `True` if within working hours, otherwise `False`.

#### is_date_within_rang(appointment_date)

Checks if the given appointment date is within a valid range (future dates).

- **Parameters:**
    - `appointment_date`: Date string in the format '%Y-%m-%d'.

- **Returns:**
    - `True` if date is valid and in the future, otherwise `False`.

#### create_appointment_slots()

Creates time slots for appointments based on defined parameters.

- **Returns:**
    - List of time objects representing available appointment slots.

---

## DateTimeUtils

**[Date Utils](src/utils/DateUtils.py)**

Provides utility methods for parsing, converting, and formatting date and time objects.

### Methods

#### parse_date(date, date_format)

Parses a date string into a datetime.date object.

- **Parameters:**
    - `date`: Date string to parse.
    - `date_format`: Format of the date string.

- **Returns:**
    - `datetime.date` object parsed from the date string.

#### parse_time(time, time_format)

Parses a time string into a datetime.time object.

- **Parameters:**
    - `time`: Time string to parse.
    - `time_format`: Format of the time string.

- **Returns:**
    - `datetime.time` object parsed from the time string.

#### date_to_string(date, date_format)

Converts a datetime.date object into a formatted date string.

- **Parameters:**
    - `date`: `datetime.date` object to convert.
    - `date_format`: Desired format of the date string.

- **Returns:**
    - Formatted date string.

#### time_to_string(time, time_format)

Converts a datetime.time object into a formatted time string.

- **Parameters:**
    - `time`: `datetime.time` object to convert.
    - `time_format`: Desired format of the time string.

- **Returns:**
    - Formatted time string.

---

## HTTP

**[HTTP Utils](src/utils/Http.py)**

Enum class defining HTTP status codes for use in API responses.

### Status Codes

- `OK`: 200
- `CREATED`: 201
- `ACCEPTED`: 202
- `NO_CONTENT`: 204
- `BAD_REQUEST`: 400
- `UNAUTHORIZED`: 401
- `FORBIDDEN`: 403
- `NOT_FOUND`: 404
- `INTERNAL_SERVER_ERROR`: 500
- `NOT_IMPLEMENTED`: 501
- `BAD_GATEWAY`: 502
- `SERVICE_UNAVAILABLE`: 503

---

## MongoDBConnection

**[MongoDB Connection](src/utils/MongoDBConnection.py)**

Handles MongoDB database connection and configuration.

### Methods

#### connect()

Connects to the MongoDB database using predefined configuration.

- **Returns:**
    - MongoDB database object.

#### close()

Closes the MongoDB database connection.

---

## JWT

**[Token Factory](src/utils/TokenFactory.py)**

Provides utilities for handling JWT tokens, including generation, encoding, decoding, and validation.

### Methods

#### generate_admin_token(admin)

Generates a JWT token for an admin user.

- **Parameters:**
    - `admin`: User object representing the admin.

- **Returns:**
    - Generated JWT token.

#### generate_doctor_token(doctor)

Generates a JWT token for a doctor user.

- **Parameters:**
    - `doctor`: User object representing the doctor.

- **Returns:**
    - Generated JWT token.

#### generate_patient_token(patient)

Generates a JWT token for a patient user.

- **Parameters:**
    - `patient`: User object representing the patient.

- **Returns:**
    - Generated JWT token.

#### encode_token(username, secret_key)

Encodes a JWT token using the provided username and secret key.

- **Parameters:**
    - `username`: Username to encode into the token.
    - `secret_key`: Secret key used for encoding.

- **Returns:**
    - Encoded JWT token.

#### decode_token(token, secret_key)

Decodes a JWT token using the provided token and secret key.

- **Parameters:**
    - `token`: JWT token to decode.
    - `secret_key`: Secret key used for decoding.

- **Returns:**
    - Decoded token data.

#### get_username_from_token(token, secret_key)

Extracts the username from a JWT token using the provided token and secret key.

- **Parameters:**
    - `token`: JWT token to decode.
    - `secret_key`: Secret key used for decoding.

- **Returns:**
    - Username extracted from the token.

#### is_missing(token)

Checks if a JWT token is missing (None).

- **Parameters:**
    - `token`: JWT token to check.

- **Returns:**
    - `True` if token is missing, otherwise `False`.

#### is_blacklisted(token)

Checks if a JWT token is blacklisted (invalid).

- **Parameters:**
    - `token`: JWT token to check.

- **Returns:**
    - `True` if token is blacklisted, otherwise `False`.

---

## ServiceException

**[Service Exception](src/utils/ServiceException.py)**

Exception class for handling service-related errors.

---

## DatabaseException

**[Database Exception](src/utils/ServiceException.py)**

Exception class for handling database-related errors.

---

## SchemaException

**[Schema Exception](src/utils/ServiceException.py)**

Exception class for handling schema-related errors.

---

## Config

**[Environment Config](src/utils/EnvironmentConfig.py)**

Enum class defining configuration constants used throughout the project, including MongoDB settings and secret keys.

### Configuration Constants

- `ADMIN_SECRET_KEY`
- `DOCTOR_SECRET_KEY`
- `PATIENT_SECRET_KEY`
- `URI`
- `HOST`
- `PORT`
- `DB`
- `ADMIN_COLLECTION`
- `DOCTOR_COLLECTION`
- `PATIENT_COLLECTION`
- `APPOINTMENT_COLLECTION`

---

---

# Decorators

**[Decorators](src/utils/Decorators.py)**

This module contains decorators used for authentication, authorization, and exception handling in the project.

## Decorators

### `token_required(secret_key)`

A decorator to ensure that the request contains a valid JWT token.

#### Parameters

- `secret_key`: The secret key used to decode the JWT token.

#### Usage

- Apply this decorator to any route that requires user authentication.
- Extracts the JWT token from the request headers.
- Checks if the token is missing or blacklisted.
- Decodes the token and retrieves the current user's username.
- Returns a 403 response if the token is missing, expired, or invalid.

### `remove_token(secret_key)`

A decorator to handle token removal (logout functionality).

#### Parameters

- `secret_key`: The secret key used to decode the JWT token.

#### Usage

- Apply this decorator to any route that handles user logout.
- Extracts the JWT token from the request headers.
- Checks if the token is missing or blacklisted.
- Decodes the token and blacklists it.
- Returns a 403 response if the token is missing, expired, or invalid.

### `handle_exceptions(func)`

A decorator to handle exceptions and return appropriate responses.

#### Usage

- Apply this decorator to any route that requires exception handling.
- Wraps the function and catches `ServiceException` and other exceptions.
- Returns a response entity with the appropriate status code and error message.

</div>
</details>

<details>
<summary> API Documentation </summary>
<div>

# Example API Requests and Responses

---

### Explanation:

- Replace `<access_token>` with the actual JWT token for authorization where necessary which is included in the
  successful login responses.
- Adjust endpoint URLs, headers, request bodies, query parameters, and response structures based on the application's
  implementation.
- Use these examples as a guide to understand how clients interact with the API endpoints using JSON payloads and
  receive responses formatted in JSON.

This section provides comprehensive examples for basic operations handled by the Admin, Doctor, and Patient controllers
in the application.

---

## Admin API

### Login:

**Request**:

- **Endpoint**: `/api/admin/login`
- **Method**: `POST`
- **Headers**:
    - `Content-Type: application/json`

**Request Body**:

```json
{
  "username": "admin",
  "password": "@dm1n"
}
```

**Response**:

- **Status**: `HTTP/1.1 200 OK`
- **Headers**:
    - `Content-Type: application/json`

**Response Body**:

```json
{
  "status": "success",
  "data": {
    "username": "admin",
    "token": "<access_token>"
  },
  "date": "<date_of_login>"
}
```

### Logout

**Request**:

- **Endpoint**: `/api/admin/logout`
- **Method**: `GET`
- **Headers**:
    - `Authorization: Bearer <access_token>`

**Request Body**:

```

No Request Body is required
```

**Response**:

- **Status**: `HTTP/1.1 200 OK`
- **Headers**:
    - `Content-Type: application/json`

**Response Body**:

```json
{
  "status": "success",
  "data": {
    "Admin Logged Out": true
  },
  "date": "<date_of_logout>"
}
```

### Create Doctor:

**Request**:

- **Endpoint**: `/api/admin/create_doctor`
- **Method**: `POST`
- **Headers**:
    - `Content-Type: application/json`
    - `Authorization: Bearer <access_token>`

**Request Body**:

```json
{
  "username": "dr_smith",
  "password": "password123",
  "email": "dr.smith@example.com",
  "first_name": "John",
  "last_name": "Smith",
  "specialization": "Cardiologist",
  "appointment_cost": 150.0
}
```

**Response**:

- **Status**: `HTTP/1.1 200 OK`
- **Headers**:
    - `Content-Type: application/json`

**Response Body**:

```json
{
  "status": "success",
  "data": {
    "cid": "DOC_1842218",
    "username": "dr_smith",
    "email": "dr.smith@example.com",
    "first_name": "John",
    "last_name": "Smith",
    "specialization": "Cardiologist",
    "appointment_cost": 150.0
  },
  "date": "<datetime_of_creation>"
}
```

### Update Doctor Password:

**Request**:

- **Endpoint**: `/api/admin/update_doctor_password`
- **Method**: `PUT`
- **Headers**:
    - `Content-Type: application/json`
    - `Authorization: Bearer <access_token>`

**Request Body**:

```json
{
  "username": "dr_smith",
  "old_password": "password123",
  "new_password": "newpassword456"
}
```

**Response**:

- **Status**: `HTTP/1.1 200 OK`
- **Headers**:
    - `Content-Type: application/json`

**Response Body**:

```json

{
  "status": "success",
  "data": {
    "Password changed": true
  },
  "date": "<date_of_update>"
}
```

### Delete Doctor:

**Request**:

- **Endpoint**: `/api/admin/delete_doctor/<doctor_username>`
- **Method**: `DELETE`
- **Headers**:
    - `Authorization: Bearer <access_token>`

**Request URL Params**:

```
  <doctor_username>
```

**Response**:

- **Status**: `HTTP/1.1 200 OK`
- **Headers**:
    - `Authorization: Bearer <access_token>`

**Response Body**:

```json
{
  "status": "success",
  "data": {
    "Doctor deleted": true
  },
  "date": "<date_of_deletion>"
}
```

### Delete Patient:

**Request**:

- **Endpoint**: `/api/admin/delete_patient/<patient_username>`
- **Method**: `DELETE`
- **Headers**:
    - `Authorization: Bearer <access_token>`

**Request URL Params**:

```
  <patient_username>
```

**Response**:

- **Status**: `HTTP/1.1 200 OK`
- **Headers**:
    - `Content-Type: application/json`

**Response Body**:

```json
{
  "status": "success",
  "data": {
    "Patient deleted": true
  },
  "date": "<date_of_deletion>"
}
```

## Doctor API

### Login:

**Request**:

- **Endpoint**: `/api/doctor/login`
- **Method**: `POST`
- **Headers**:
    - `Content-Type: application/json`

**Request Body**:

```json
{
  "username": "dr_smith",
  "password": "password123"
}
```

**Response**:

- **Status**: `HTTP/1.1 200 OK`
- **Headers**:
    - `Content-Type: application/json`

**Response Body**:

```json
{
  "status": "success",
  "data": {
    "username": "dr_smith",
    "token": "<token_created>"
  },
  "date": "<date_of_login>"
}
```

### Logout

**Request**:

- **Endpoint**: `/api/doctor/logout`
- **Method**: `GET`
- **Headers**:
    - `Authorization: Bearer <access_token>`

**Request Body**:

```

No Request Body is required
```

**Response**:

- **Status**: `HTTP/1.1 200 OK`
- **Headers**:
    - `Content-Type: application/json`

**Response Body**:

```json
{
  "status": "success",
  "data": {
    "Doctor Logged Out": true
  },
  "date": "<date_of_logout>"
}
```

### Update Password:

**Request**:

- **Endpoint**: `/api/doctor/update_doctor_password`
- **Method**: `PUT`
- **Headers**:
    - `Content-Type: application/json`
    - `Authorization: Bearer <access_token>`

**Request Body**:

```json
{
  "username": "dr_smith",
  "old_password": "password123",
  "new_password": "newpassword456"
}
```

**Response**:

- **Status**: `HTTP/1.1 200 OK`
- **Headers**:
    - `Content-Type: application/json`

**Response Body**:

```json
{
  "status": "success",
  "data": {
    "Password Changed": true
  },
  "date": "<date_of_update>"
}
```

### Update Appointment Cost:

**Request**:

- **Endpoint**: `/api/doctor/update_appointment_cost`
- **Method**: `PUT`
- **Headers**:
    - `Content-Type: application/json`
    - `Authorization: Bearer <access_token>`

**Request Body**:

```json
{
  "username": "dr_smith",
  "old_cost": 150.0,
  "new_cost": 200.0
}
```

**Response**:

- **Status**: `HTTP/1.1 200 OK`
- **Headers**:
    - `Content-Type: application/json`

**Response Body**:

```json

{
  "status": "success",
  "data": {
    "Appointment cost updated": true
  },
  "date": "<date_of_update>"
}
```

### Fetch Appointments:

**Request**:

- **Endpoint**: `/api/admin/appointments/`
- **Method**: `GET`
- **Headers**:
    - `Authorization: Bearer <access_token>`

**Request Params**:

```
   No parameters are required. The access token is used to access the appointments.

```

**Response**:

- **Status**: `HTTP/1.1 200 OK`
- **Headers**:
    - `Authorization: Bearer <access_token>`

**Response Body**:

```json
{
  "status": "success",
  "data": [
    {
      "cid": "APT_4746881",
      "patient_name": "John",
      "patient_surname": "Doe",
      "appointment_time": "10:00",
      "appointment_date": "2024-07-01",
      "reason": "General Checkup"
    }
  ],
  "date": "<date_of_request>"
}
```

## Patient API

### Login:

**Request**:

- **Endpoint**: `/api/patient/login`
- **Method**: `POST`
- **Headers**:
    - `Content-Type: application/json`

**Request Body**:

```json
{
  "username": "john_doe",
  "password": "password123"
}
```

**Response**:

- **Status**: `HTTP/1.1 200 OK`
- **Headers**:
    - `Content-Type: application/json`

**Response Body**:

```json
{
  "status": "success",
  "data": {
    "username": "john_doe",
    "token": "<token_created>"
  },
  "date": "date_of_login"
}
```

### Logout

**Request**:

- **Endpoint**: `/api/patient/logout`
- **Method**: `GET`
- **Headers**:
    - `Authorization: Bearer <access_token>`

**Request Body**:

```

No Request Body is required
```

**Response**:

- **Status**: `HTTP/1.1 200 OK`
- **Headers**:
    - `Content-Type: application/json`

**Response Body**:

```json
{
  "status": "success",
  "data": {
    "Patient Logged Out": true
  },
  "date": "<date_of_logout>"
}
```

### Register:

**Request**:

- **Endpoint**: `/api/patient/register`
- **Method**: `POST`
- **Headers**:
    - `Content-Type: application/json`
    - `Authorization: Bearer <access_token>`

**Request Body**:

```json
{
  "username": "john_doe",
  "password": "password123",
  "email": "john.doe@example.com",
  "first_name": "John",
  "last_name": "Doe",
  "amka": "123456789",
  "date_of_birth": "1997-20-06"
}
```

**Response**:

- **Status**: `HTTP/1.1 200 OK`
- **Headers**:
    - `Content-Type: application/json`

**Response Body**:

```json
{
  "status": "success",
  "data": {
    "username": "john_doe",
    "token": "<token_created>"
  },
  "date": "<date_of_registration>"
}
```

### Book Appointment:

**Request**:

- **Endpoint**: `/api/patient/book_appointment`
- **Method**: `POST`
- **Headers**:
    - `Content-Type: application/json`
    - `Authorization: Bearer <access_token>`

**Request Body**:

```json
{
  "appointment_date": "2024-07-01",
  "appointment_time": "10:00",
  "reason": "General Checkup",
  "specialization": "Cardiologist"
}
```

**Response**:

- **Status**: `HTTP/1.1 200 OK`
- **Headers**:
    - `Content-Type: application/json`

**Response Body**:

```json

{
  "status": "success",
  "data": {
    "cid": "APT_4746881",
    "doctor_username": "dr_smith",
    "patient_username": "john_doe",
    "patient_name": "John",
    "patient_surname": "Doe",
    "doctor_name": "John",
    "doctor_surname": "Smith",
    "appointment_date": "2024-07-01",
    "appointment_time": "10:00",
    "reason": "General Checkup",
    "cost": 200.0,
    "specialization": "Cardiologist"
  },
  "date": "date_of_book"
}
```

### Fetch Appointments:

**Request**:

- **Endpoint**: `/api/patient/appointments`
- **Method**: `GET`
- **Headers**:
    - `Authorization: Bearer <access_token>`

**Request**:

```
   No parameters are required. The access token is used to access the appointments.
```

**Response**:

- **Status**: `HTTP/1.1 200 OK`
- **Headers**:
    - `Authorization: Bearer <access_token>`

**Response Body**:

```json
{
  "status": "success",
  "data": [
    {
      "cid": "APT_4746881",
      "doctor_name": "John",
      "doctor_surname": "Smith",
      "appointment_time": "10:00",
      "appointment_date": "2024-07-01"
    }
  ],
  "date": "<date_of_request>"
}
```

### Fetch Appointment's Details:

**Request**:

- **Endpoint**: `/api/patient/appointment/<appointment_id>`
- **Method**: `GET`
- **Headers**:
    - `Authorization: Bearer <access_token>`

**Request URL Params**:

```
   <appointment_id> (Is the system generated cid shown in the fetch appointments request)
```

**Response**:

- **Status**: `HTTP/1.1 200 OK`
- **Headers**:
    - `Authorization: Bearer <access_token>`

**Response Body**:

```json
{
  "status": "success",
  "data": {
    "cid": "APT_4746881",
    "doctor_name": "John",
    "doctor_surname": "Smith",
    "appointment_time": "10:00",
    "appointment_date": "2024-07-01",
    "specialization": "Cardiologist",
    "cost": 200.0,
    "reason": "General Checkup"
  },
  "date": "<date_of_request>"
}
```

### Cancel Appointment:

**Request**:

- **Endpoint**: `/api/patient/cancel_appointment/<appointment_id>`
- **Method**: `DELETE`
- **Headers**:
    - `Authorization: Bearer <access_token>`

**Request URL Params**:

```
   <appointment_id> (Is the system generated cid shown in the fetch appointments request)
```

**Response**:

- **Status**: `HTTP/1.1 200 OK`
- **Headers**:
    - `Authorization: Bearer <access_token>`

**Response Body**:

```json
{
  "status": "success",
  "data": {
    "Appointment canceled": true
  },
  "date": "<date_of_cancellation"
}
```

</div>
</details>


<details>
<summary> Swagger API Documentation </summary>
<div>

# Swagger Documentation

This project uses Swagger to provide interactive API documentation. Swagger is a powerful tool that helps you design,
build, document, and consume RESTful web services.

### What is Swagger?

Swagger is an open-source software framework that allows developers to design, build, document, and consume RESTful web
services. It simplifies API development by providing a user-friendly interface to interact with the API, test endpoints,
and view detailed information about the API's structure and functionality.

### Accessing Swagger UI

You can access the Swagger UI for the DS Hospital API at the following URL after building the project:

`http://<swagger-url>/api/swagger`

Replace `<your-server-address>` with the address where your server is running (e.g., `localhost:5000` if you are running
the server locally).

### What Can You Do with Swagger UI?

With the Swagger UI, you can:

1. **Explore API Endpoints**: View a list of all available API endpoints, organized by category.
2. **Read Documentation**: See detailed documentation for each endpoint, including descriptions, request methods,
   parameters, and response formats.
3. **Test API Endpoints**: Interactively test the API by making requests directly from the browser. You can provide
   request parameters, view the responses, and see the status codes.
4. **View Models**: Understand the structure of the data models used in the API, including the required and optional
   fields for each request body.

### Operations You Can Perform

The DS Hospital API provides various operations that can be performed by different user roles (Admin, Doctor, Patient).
Here are some examples:

- **Admin Operations**:
    - Create, update, and delete doctors and patients.

- **Doctor Operations**:
    - Login and logout.
    - Update password and appointment cost.
    - Fetch and manage appointments.

- **Patient Operations**:
    - Login, logout, and register.
    - Book and cancel appointments.
    - Fetch appointment details.

### Configuration

The Swagger UI is configured in the application as follows:

```python
from flask_swagger_ui import get_swaggerui_blueprint
from flask import Flask

app = Flask(__name__)

swagger_ui_blueprint = get_swaggerui_blueprint(
    '/api/swagger',
    '/static/swagger.json',
    config={
        'app_name': 'DS Hospital API'
    }
)

app.register_blueprint(swagger_ui_blueprint, url_prefix='/api/swagger')
```

### Swagger JSON

The Swagger UI uses a JSON file to generate the documentation. This JSON file contains all the information about the API
endpoints, parameters, and models. The file is located at:

`/static/swagger.json`

### Summary

Swagger UI enhances the developer experience by providing a comprehensive and interactive documentation tool. It makes
it easier to understand the API, test endpoints, and integrate the API with other applications.

Make sure to explore the Swagger UI to get familiar with all the capabilities of the DS Hospital API!
</div>
</details>




<details>
<summary> Unit Testing Documentation </summary>
<div>

# Unit Testing

## Unit Tests

### Overview

Unit testing is a software testing method where individual units or components of a software are tested in isolation
from the rest of the application. This helps ensure that each part of the application behaves as expected.

### Test-Driven Development (TDD)

Test-Driven Development (TDD) is a software development process where you write tests for your functions before writing
the actual code. The process typically follows these steps:

1. **Write a Test**: Write a unit test that defines a function or improvement.
2. **Run All Tests**: Run the tests and see if the new test fails. This is a confirmation that the test is working and
   that the feature isn’t already implemented.
3. **Write Code**: Write the minimal amount of code required to pass the test.
4. **Run Tests**: Run the tests again. If they pass, it means the code meets the test requirements.
5. **Refactor Code**: Refactor the new code to acceptable standards while ensuring that the tests still pass.
6. **Repeat**: Repeat the cycle for each new feature or improvement.

TDD helps ensure that the code is thoroughly tested and reduces the chances of bugs.

### Using Pytest

We use `pytest` and `unittest` as our testing frameworks. Pytest is a mature full-featured Python testing tool that
helps you write better programs.

### Running the Tests

To run the tests, you need to have `pytest` installed. You can install it using pip:

```bash
pip install pytest
```

Once installed, you can run the tests by navigating to the root directory of the project and executing:

```bash
pytest src/tests
```

### Test Coverage

Our unit tests cover various parts of the application to ensure each component functions correctly. The tests include:

#### Admin Operations Tests:

- Creating, updating, and deleting doctors and patients.

#### Doctor Operations Tests:

- Login and logout functionality.
- Updating password and appointment cost.
- Fetching and managing appointments.

#### Patient Operations Tests:

- Login, logout, and registration.
- Booking and canceling appointments.
- Fetching appointment details.

## Example Test Cases

Here are some examples of the unit test cases implemented using pytest:

```python
import unittest
from datetime import datetime

from src.utils.DateUtils import DateTimeUtils


class TestDateTimeUtils(unittest.TestCase):
    def test_parse_date(self):
        date_str = '2024-07-01'
        date_format = '%Y-%m-%d'
        parsed_date = DateTimeUtils.parse_date(date_str, date_format)

        self.assertEqual(parsed_date.year, 2024)
        self.assertEqual(parsed_date.month, 7)
        self.assertEqual(parsed_date.day, 1)

    def test_parse_time(self):
        time_str = '14:30:00'
        time_format = '%H:%M:%S'
        parsed_time = DateTimeUtils.parse_time(time_str, time_format)

        self.assertEqual(parsed_time.hour, 14)
        self.assertEqual(parsed_time.minute, 30)
        self.assertEqual(parsed_time.second, 0)

    def test_date_to_string(self):
        date = datetime(year=2024, month=7, day=1)
        date_format = '%Y-%m-%d'
        date_str = DateTimeUtils.date_to_string(date, date_format)

        self.assertEqual(date_str, '2024-07-01')

    def test_time_to_string(self):
        time = datetime.strptime('14:30:00', '%H:%M:%S').time()
        time_format = '%H:%M:%S'
        time_str = DateTimeUtils.time_to_string(time, time_format)

        self.assertEqual(time_str, '14:30:00')


if __name__ == '__main__':
    unittest.main()
```

## Importance of Unit Testing

Unit testing is crucial for ensuring the reliability and quality of your code. It helps you catch bugs early, simplifies
debugging, and provides documentation for your codebase. Implementing unit tests in conjunction with TDD can
significantly enhance the development process by ensuring that new features do not introduce new bugs.

By following these practices, we ensure that the DS Hospital API remains robust, maintainable, and bug-free.
</div>
</details>

<details>
<summary>Jenkins CI/CID</summary>
<div>

## Jenkins CI/CD

### Introduction

[Jenkins](https://www.jenkins.io/) is an open-source automation server that helps automate the parts of software
development related to building, testing, and deploying, facilitating continuous integration and continuous delivery (
CI/CD).

### Prerequisites

- Docker installed on your machine.
- Basic knowledge of Docker and CI/CD pipelines.

### Docker Compose for Jenkins

Here is a simple Docker Compose file to run Jenkins:

```yaml
version: '3.8'

services:
  jenkins:
    image: jenkins/jenkins:lts
    container_name: jenkins
    ports:
      - "8080:8080"
      - "50000:50000"
    volumes:
      - jenkins_home:/var/jenkins_home

volumes:
  jenkins_home:
  ```

### Installation Steps

#### Create a directory for Jenkins:

```bash
mkdir jenkins
cd jenkins
```

##### Create a docker-compose.yml file and add the above content.

### Run the Docker Compose:

```bash
docker-compose up -d
```

#### Access Jenkins:

Open your browser and go to http://localhost:8080.

#### Unlock Jenkins: Retrieve the initial admin password by running:

```bash
docker exec jenkins cat /var/jenkins_home/secrets/initialAdminPassword
```

Enter this password on the Jenkins setup page.

#### Install Suggested Plugins: Follow the on-screen instructions to install the suggested plugins.

</div>
</details>

<details>
<summary>SonarQube Code Analysis</summary>
<div>

## SonarQube Code Analysis

### Introduction

SonarQube is an open-source platform used for continuous inspection of code quality to perform automatic reviews with
static analysis of code to detect bugs, code smells, and security vulnerabilities.

### Prerequisites

Docker installed on your machine.
Basic knowledge of code quality and static analysis.

### Docker Compose for SonarQube

Here is a simple Docker Compose file to run SonarQube:

```yaml
version: '3.8'

services:
  sonarqube:
    image: sonarqube:latest
    container_name: sonarqube
    ports:
      - "9000:9000"
    environment:
      - SONARQUBE_JDBC_URL=jdbc:postgresql://sonarqube-db:5432/sonar
      - SONAR_JDBC_USERNAME=sonar
      - SONAR_JDBC_PASSWORD=sonar
    volumes:
      - sonarqube_data:/opt/sonarqube/data
      - sonarqube_logs:/opt/sonarqube/logs
      - sonarqube_extensions:/opt/sonarqube/extensions

volumes:
  sonarqube_data:
  sonarqube_logs:
  sonarqube_extensions:
```

### Installation Steps

#### Create a directory for SonarQube:

```bash
mkdir sonarqube
cd sonarqube
```

#### Create a docker-compose.yml file and add the above content.

#### Run the Docker Compose:

``` bash
docker-compose up -d
```

#### Access SonarQube:

Open your browser and go to http://localhost:9000.

#### Login with default credentials:

Username: admin, Password: admin.


</div>
</details>


<details>
<summary>Jenkins - SonarQube Documentation</summary>
<div>

## Jenkins Pipelines and SonarQube Code Analysis

### Custom Docker Compose File

This section describes how to set up Jenkins and SonarQube using a custom Docker Compose file and configure them to work
together.

#### Docker Compose File

```yaml
version: '3.8'

services:
  jenkins:
    build:
      context: .
      dockerfile: Dockerfile
    image: jenkins/jenkins:lts
    container_name: jenkins
    ports:
      - "50000:50000"
      - "8080:8080"

    networks:
      - jenkins_sonarqube_network

    volumes:
      - jenkins_home:/var/jenkins_home

  sonarqube:
    image: sonarqube:latest
    container_name: sonarqube
    ports:
      - "9000:9000"
    environment:
      - SONARQUBE_JDBC_URL=jdbc:postgresql://sonarqube-db:5432/sonar
      - SONAR_JDBC_USERNAME=sonar
      - SONAR_JDBC_PASSWORD=sonar
    networks:
      - jenkins_sonarqube_network

    volumes:
      - sonarqube_data:/opt/sonarqube/data
      - sonarqube_logs:/opt/sonarqube/logs
      - sonarqube_extensions:/opt/sonarqube/extensions

networks:
  jenkins_sonarqube_network:
    driver: bridge

volumes:
  jenkins_home:
  sonarqube_data:
  sonarqube_logs:
  sonarqube_extensions:
```

#### Dockerfile

```dockerfile
# Use the official Jenkins LTS image from Docker Hub
FROM jenkins/jenkins:lts

# Switch to root user for installation
USER root

# Install necessary tools and dependencies

# Update package lists and install Python 3 with pip
RUN apt-get update && apt-get install -y python3 python3-venv


# Switch back to Jenkins user
USER jenkins
```

## Jenkinsfile for CI/CD Pipeline

Below is an example of a Jenkinsfile to automate the CI/CD process, including running tests and SonarQube analysis.

```groovy
pipeline {
    agent any

    environment {
        SONAR_SCANNER_HOME = tool 'SonarQubeScanner'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scmGit(branches: [[name: 'master']],
                        extensions: [], userRemoteConfigs: [[credentialsId: 'SecretKey', url: 'https://github.com/GiorgosThf/DS-Hospital.git']])
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                     python3 -m venv venv
                    . venv/bin/activate
                    ./venv/bin/pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests with Coverage') {
            steps {
                script {
                    try {

                        sh '''
                    . venv/bin/activate
                    ./venv/bin/python3 -m pytest src/tests --alluredir allure-results --cov=src --cov-report=xml --cov-report=html
                '''
                    } catch (Exception e) {
                        // Mark the build as unstable if tests fail
                        currentBuild.result = 'UNSTABLE'
                    }
                }
            }
        }


        stage('SonarQube Analysis') {
            steps {
                script {
                    withSonarQubeEnv('SonarQubeServer') {
                        sh '''
                                ${SONAR_SCANNER_HOME}/bin/sonar-scanner
                                '''
                    }
                }

            }
        }
        stage('Generate Allure Report') {
            steps {
                allure([
                        includeProperties: false,
                        jdk              : '',
                        properties       : [],
                        reportBuildPolicy: 'ALWAYS',
                        results          : [[path: "DS-Hospital/allure-results"]]
                ])
            }
        }
    }
}

```

## Steps to Configure and Trigger Jenkins Job

#### Access Jenkins: Open your browser and go to http://localhost:8080.

**Generate SonarQube Token:**

1. Go to http://localhost:9000, login with admin/admin.
2. Go to My Account -> Security -> Generate Tokens.
3. Generate a new Token (Type: Global Analysis Token)
4. Use this token in Jenkins to connect with SonarQube. (Discussed later)

**Generate GitHub Token:**

1. Go to https://github.com/my-account.
2. Go to Settings -> Developer Settings -> Personal Access Tokens
3. Generate a new token.
4. Use this token in Jenkins to connect with GitHub when checking out the GitHub Repository. (Discussed later)

**Configure Jenkins Credentials:**

1. Got to Manage Jenkins -> Credentials.
2. Add new credential for GitHub of type username and password (Username : GitHub Username, Password: GitHub Token).
3. Add new credential for SonarQube Server of type secret text (Secret Text: The SonarQube Generated Token).

**Install Jenkins Plugins:**

1. Go to Manage Jenkins -> Plugins -> Available Plugins
2. Select [Allure Plugin](#https://plugins.jenkins.io/allure-jenkins-plugin).
3. Select [SonarQube Scanner Plugin](#https://plugins.jenkins.io/sonar).
4. Select [Pipeline Stage View Plugin](#https://plugins.jenkins.io/pipeline-stage-view).
5. Install all the selected plugins.

**Configure SonarQube Server in Jenkins:**

1. Go to Manage Jenkins -> Configure System.
2. Find the SonarQube servers section, click Add SonarQube.
3. Click the box Environment Variables.
4. Enter the name for the server e.g. 'SonarQubeServer' (This is how you will access it later in the pipelines using
   withSonarQubeEnv('SonarQubeServer') )
5. Add the Sonar URL (If you are using docker, and you created the network as shown in the compose.yml file before, then
   use http://<name_of_contaier>:9000, otherwise use the Server's URL)
6. Add ServerAuthentication Token (Select the secret-text token we created for Sonar before)

**Configure SonarQube Tool:**

1. Go to Manage Jenkins -> Tools -> SonarQube Scanner Installation
2. Click Add SonarQube Scanner
3. Set Name of the scanner e.g. 'SonarQubeScanner' (This is how you will access it later in the pipelines using tool('
   SonarQubeScanner'))
4. Click Install Automatically and select the version of SonarQube Scanner.

**Configure Allure Tool:**

1. Go to Manage Jenkins -> Tools -> Allure Commandline Installation
2. Click Add SonarQube Scanner
3. Set Name of the scanner e.g. 'Allure' (This is how you will access it later in the pipelines using tool('Allure'))
4. Click Install Automatically and select the version of Allure Commandline.

**Create a New Job:**

1. Click on New Item.
2. Enter a name for your job, select Pipeline, and click OK.

**Configure the Pipeline (JenkinsFile in repository ):**

1. Under Pipeline section, select Pipeline script from SCM.
2. Choose Git and enter your repository URL.
3. Add your credentials and specify the branch name (master). *Preferably generate a GitHub token and pass it to the
   Jenkins Credentials as SecretKey.
4. Configure Jenkins to use the JenkinsFile ine the repository.

**Configure the Pipeline (Direct Groovy Script):**

1. Under Pipeline section, select Pipeline script from SCM.
2. Choose Git and enter your repository URL.
3. Insert the groovy script into the script section of the pipeline e.g. The script shown before.

**Run the Jenkins Job:**

1. Go back to your Jenkins job and click Build Now.
2. Monitor the console output to ensure the pipeline runs successfully.

By following these steps and configurations, you can effectively set up a CI/CD pipeline with Jenkins and perform code
analysis with SonarQube.
</div>
</details>