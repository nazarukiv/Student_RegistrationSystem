# Student Registration System

The Student Registration System is a Python-based desktop application built using the Tkinter library for the graphical user interface. It allows users to register, update, search, and manage student details. The data is stored in an Excel file using the OpenPyXL library.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Folder Structure](#folder-structure)
- [Contributing](#contributing)

  
## Features

- Register new students with details such as name, class, gender, date of birth, religion, skills, and parent details.
- Upload and display student profile pictures.
- Search for students by registration number.
- Update student details.
- Clear form fields.
- Data is stored in an Excel file (`Student_data.xlsx`).

## Installation

1. **Clone the Repository:**
    ```bash
    git clone https://github.com/your-username/student-registration-system.git
    cd student-registration-system
    ```

2. **Install Dependencies:**
    Make sure you have Python installed. Then, install the required packages:
    ```bash
    pip install pillow openpyxl
    ```

3. **Run the Application:**
    ```bash
    python main.py
    ```

## Usage

1. **Running the Application:**
    - Open a terminal and navigate to the project directory.
    - Run `python main.py` to start the application.

2. **Register a New Student:**
    - Fill in the student's details in the provided fields.
    - Upload a profile picture by clicking the "Upload" button.
    - Click the "Save" button to save the student's details.

3. **Search for a Student:**
    - Enter the student's registration number in the search box.
    - Click the "Search" button to retrieve and display the student's details.

4. **Update Student Details:**
    - Search for the student you want to update.
    - Modify the student's details as needed.
    - Click the "Update" button to save the changes.

5. **Clear Form Fields:**
    - Click the "Reset" button to clear all form fields.

6. **Exit the Application:**
    - Click the "Exit" button to close the application.

## Folder Structure

- `media/`: Contains image files used in the application.
- `main.py`: The main application script.
- `README.md`: The documentation file.
- `requirements.txt`: A file listing the required Python packages.
- `Student_data.xlsx`: The Excel file where student data is stored.

## Contributing

Contributions are welcome! If you have any improvements or new features to add, please open a pull request.

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add some feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Open a pull request.


## Contact

For any inquiries or feedback, please contact [nazaruk649@ukr.net](mailto:nazaruk649@ukr.net).