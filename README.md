
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

3. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Apply migrations:

   ```bash
   python manage.py migrate
   ```

5. Run the development server:

   ```bash
   python manage.py runserver
   ```

6. Open your browser and visit:

   ```
   http://127.0.0.1:8000/
   ```

## Usage

1. Enter a URL into the input field.
2. Click on the "Generate QR Code" button.
3. Download the generated QR code as an image.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for suggestions and improvements.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Django](https://www.djangoproject.com/) - The web framework used.
- [qrcode](https://pypi.org/project/qrcode/) - The Python library for generating QR codes.

