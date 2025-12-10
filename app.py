from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai
import fitz  # PyMuPDF

# Configure Gemini API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# ------------------------------
# Gemini response function
# ------------------------------
def get_gemini_response(input_text, resume_text, prompt):
    model = genai.GenerativeModel("gemini-2.5-flash")
    combined_text = input_text + "\n" + resume_text + "\n" + prompt
    response = model.generate_content(combined_text)
    return response.text

# ------------------------------
# Extract resume text from PDF
# ------------------------------
def input_pdf_setup(uploaded_file):
    if uploaded_file is not None:
        doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
        # Combine text of all pages (or first page only)
        resume_text = ""
        for page in doc:
            resume_text += page.get_text()
        return resume_text
    else:
        raise FileNotFoundError("No file uploaded")

# ------------------------------
# Streamlit UI
# ------------------------------
st.set_page_config(page_title="ATS Resume EXpert")
st.header("ATS Tracking System")

input_text = st.text_area("Job Description:", key="input")
uploaded_file = st.file_uploader("Upload your resume (PDF):", type=["pdf"])

if uploaded_file is not None:
    st.success("PDF Uploaded Successfully!")

# Buttons
submit1 = st.button("Tell Me About the Resume")
submit2 = st.button("How Can I Improvise my Skills")
submit3 = st.button("Percentage Match")
submit4 = st.button("Optimize the Resume")
submit5 = st.button("Recommend Job Roles")

# ------------------------------
# Prompts
# ------------------------------
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

input_prompt2 = """
You are a career mentor.
Based on gaps between the resume and job description, provide a CONCISE improvement roadmap:
- Priority Skills to Learn: max 5 bullets
- Recommended Certifications or Courses: max 3
- Suggested Projects: exactly 2
- 90-Day Learning Plan:
  • 0–30 days
  • 31–60 days
  • 61–90 days
Keep it practical, brief, and role-focused.
"""

input_prompt3 = """
You are an ATS (Applicant Tracking System).
Compare the resume with the job description and return ONLY:
- ATS Match Percentage: XX%
- Missing or Weak Keywords: comma-separated (max 10)
- Resume Fix Suggestions: 3 short bullets
No explanations. No extra text.
"""

input_prompt4 = """
You are an ATS resume optimization expert.
Improve the resume content to better match the job description:
- Rewrite bullet points using strong action verbs
- Add measurable impact where possible
- Keep bullets concise and ATS-friendly
Return ONLY the improved bullet points.
"""

input_prompt5 = """
You are a career advisor.
Based on the resume, suggest:
- Best suited roles: max 3
- Roles that are currently risky to apply for
- One closely related alternative role
Keep recommendations short and practical.
"""

# ------------------------------
# Button actions
# ------------------------------
if uploaded_file is not None:
    resume_text = input_pdf_setup(uploaded_file)

    if submit1:
        response = get_gemini_response(input_prompt1, resume_text, input_text)
        st.subheader("Resume Review")
        st.write(response)

    elif submit2:
        response = get_gemini_response(input_prompt2, resume_text, input_text)
        st.subheader("Skill Improvement Roadmap")
        st.write(response)

    elif submit3:
        response = get_gemini_response(input_prompt3, resume_text, input_text)
        st.subheader("ATS Match Percentage & Fixes")
        st.write(response)

    elif submit4:
        response = get_gemini_response(input_prompt4, resume_text, input_text)
        st.subheader("Optimized Resume")
        st.write(response)

    elif submit5:
        response = get_gemini_response(input_prompt5, resume_text, input_text)
        st.subheader("Recommended Job Roles")
        st.write(response)

else:
    st.info("Please upload your resume to proceed.")

