# ATS Resume Checker Project

## Demo
https://free-resume-ats.streamlit.app/

## Overview

The ATS (Applicant Tracking System) Resume Checker is a web application designed to help users evaluate their resumes against specific job descriptions. Utilizing Google Gemini AI, the application provides detailed feedback on the alignment between the resume and job description, including a percentage match and identification of missing keywords.

## Features

- **Resume Upload**: Users can upload their resumes in PDF format.
- **Job Description Input**: Users can input the job description they are targeting.
- **Detailed Analysis**: The tool generates a detailed evaluation of the resume, highlighting strengths and weaknesses.
- **Percentage Match**: The application calculates and displays the percentage match between the resume and the job description, listing missing keywords and final thoughts.

## Installation

### Prerequisites

- Python 3.6 or higher
- Pip (Python package installer)

### Required Libraries

Install the required libraries using pip:

```bash
pip install streamlit python-dotenv pillow pdf2image google-generativeai
```

## Setup

1. **Clone the Repository**: Clone the project repository and navigate into the project directory.

   ```bash
   git clone https://github.com/omghumre/Resume-ATS
   ```

2. **Environment Variables**: Create a `.env` file in the root directory of the project and add your Google API key.

   ```bash
   touch .env
   ```

   Add the following line to the `.env` file:

   ```
   GOOGLE_API_KEY=your_google_api_key
   ```

3. **Run the Application**: Start the Streamlit application.

   ```bash
   streamlit run app.py
   ```

## Usage

### Uploading a Resume

- Click on the "Browse files" button to upload your resume in PDF format.
- The application will confirm the successful upload of the file.

### Inputting Job Description

- Enter the job description in the provided text area.

### Analyzing the Resume

- Click on the "Tell Me About the Resume" button to receive a professional evaluation of your resume.
- Alternatively, click on the "Percentage match" button to get a percentage match along with missing keywords and final thoughts.

## Contribution

Contributions to the ATS Resume Checker project are welcome. To contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Acknowledgments

- Thanks to Google for providing the Generative AI API.
- Special thanks to the Streamlit team for their user-friendly web application framework.

For any questions or issues, please open an issue in the repository.
