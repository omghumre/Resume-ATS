from dotenv import load_dotenv

load_dotenv()

import streamlit as st 
import os 
from PIL import Image 
import pdf2image
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(input, pdf_content, propmt):
    model=genai.GenerativeModel('gemini-pro-vision')
    response = model.generate_content([input, pdf_content[0], propmt])
    return response.text

def input_pdf_setup(uploaded_file):
    if uploaded_file is not None:
    
        images = pdf2image.convert_from_bytes(uploaded_file.read())

        first_page = images[0]

        img_byte_arr = io.BytesIO()
        first_page.save(img_byte_arr,format='JPEG')
        img_byte_arr = img_byte_arr.getvalue()

        pdf_parts = [

            {
                "mime_type" : "image/jpeg",
                "data" : base64.b64encode(img_byte_arr).decode()
            }

        ]

        return pdf_parts
    else:
        raise FileNotFoundError("No file uploaded")


