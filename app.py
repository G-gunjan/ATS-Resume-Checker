from dotenv import load_dotenv

load_dotenv()
import base64
import streamlit as st
import os
import io
from PIL import Image 
import pdf2image
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(input, pdf_content, prompt):
    model = genai.GenerativeModel("gemini-2.5-flash")

  
    response = model.generate_content([input, pdf_content[0], prompt])
    return response.text


def input_pdf_setup(uploaded_file):
    if uploaded_file is not None:
        images = pdf2image.convert_from_bytes(uploaded_file.read())
        first_page = images[0]

       
        return [first_page]
    else:
        raise FileNotFoundError("No file uploaded")

## Streamlit App

st.set_page_config(page_title="ATS Resume EXpert")
st.header("ATS Tracking System")
input_text=st.text_area("Job Description: ",key="input")
uploaded_file=st.file_uploader("Upload your resume(PDF)...",type=["pdf"])


if uploaded_file is not None:
    st.write("PDF Uploaded Successfully")


submit1 = st.button("Tell Me About the Resume")

submit2 = st.button("How Can I Improvise my Skills")

submit3 = st.button("Percentage match")

submit4 = st.button("Optimize the resume")

submit5 = st.button("Recommend Job Roles")

#Resume Review 
input_prompt1 = """
You are a Technical HR Manager.

Evaluate the resume against the job description and respond ONLY in this format:
- Overall Fit: Strong / Moderate / Weak
- Role Level Match: Intern / Entry-level / Mid-level / Not Suitable
- Key Strengths: 3 bullets (1 line each)
- Key Gaps: 3 bullets (1 line each)
- Final Verdict: max 2 lines

Be direct. Avoid long explanations or paragraphs.
"""
#Skill Improvement Roadmap
input_prompt2 = """
You are a career mentor.

Based on gaps between the resume and job description, provide a CONCISE improvement roadmap:
- Priority Skills to Learn: max 5 bullets
- Recommended Certifications or Courses: max 3
- Suggested Projects: exactly 2
- 90-Day Learning Plan:
  • 0 –30 days
  • 31–60 days
  • 61–90 days

Keep it practical, brief, and role-focused.
"""
#ATS Percentage Match 
input_prompt3 = """
You are an ATS (Applicant Tracking System).

Compare the resume with the job description and return ONLY:
- ATS Match Percentage: XX%
- Missing or Weak Keywords: comma-separated (max 10)
- Resume Fix Suggestions: 3 short bullets

No explanations. No extra text.
"""
#optimize the resume
input_prompt4 = """
You are an ATS resume optimization expert.

Improve the resume content to better match the job description:
- Rewrite bullet points using strong action verbs
- Add measurable impact where possible
- Keep bullets concise and ATS-friendly

Return ONLY the improved bullet points.
"""
#recommend job roles
input_prompt5 = """
You are a career advisor.

Based on the resume, suggest:
- Best suited roles: max 3
- Roles that are currently risky to apply for
- One closely related alternative role

Keep recommendations short and practical.
"""

if submit1:
    if uploaded_file is not None:
        pdf_content=input_pdf_setup(uploaded_file)
        response=get_gemini_response(input_prompt1,pdf_content,input_text)
        st.subheader("The Repsonse is")
        st.write(response)
    else:
        st.write("Please uplaod the resume")

elif submit2:
    if uploaded_file is not None:
        pdf_content=input_pdf_setup(uploaded_file)
        response=get_gemini_response(input_prompt2,pdf_content,input_text)
        st.subheader("The Repsonse is")
        st.write(response)
    else:
        st.write("Please uplaod the resume")

elif submit3:
     if uploaded_file is not None:
            pdf_content=input_pdf_setup(uploaded_file)
            response=get_gemini_response(input_prompt3,pdf_content,input_text)
            st.subheader("The Repsonse is")
            st.write(response)
     else:
            st.write("Please uplaod the resume")


elif submit4:
     if uploaded_file is not None:
            pdf_content=input_pdf_setup(uploaded_file)
            response=get_gemini_response(input_prompt4,pdf_content,input_text)
            st.subheader("The Repsonse is")
            st.write(response)
     else:
            st.write("Please uplaod the resume")
elif submit5:
     if uploaded_file is not None:
            pdf_content=input_pdf_setup(uploaded_file)
            response=get_gemini_response(input_prompt5,pdf_content,input_text)
            st.subheader("The Repsonse is")
            st.write(response)
     else:
            st.write("Please uplaod the resume")

