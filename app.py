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
    images = pdf2image.convert_from_bytes(uploaded_file.read())
