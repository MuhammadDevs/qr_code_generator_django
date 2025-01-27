
# Django QR Code Generator

## Overview

This Django application allows you to generate QR codes for any link. Whether you need a QR code for a website, a social media profile, or any other URL, this project provides a simple interface to create and download QR codes instantly.

## Features

- **Generate QR Codes:** Input any URL, and the app will generate a QR code for it.
- **Simple Interface:** User-friendly design makes it easy to generate QR codes quickly.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/MuhammadDevs/qr_code_generator_django.git
   ```

2. Navigate to the project directory:

   ```bash
   cd qr_code_generator_django
   ```

3. Apply migrations:

   ```bash
   python manage.py migrate
   ```

4. Run the development server:

   ```bash
   python manage.py runserver
   ```

6. Open your browser and visit:

   ```
   http://127.0.0.1:8000/
   ```
## Acknowledgments

- [Django](https://www.djangoproject.com/) - The web framework used.
- [qrcode](https://pypi.org/project/qrcode/) - The Python library for generating QR codes.

