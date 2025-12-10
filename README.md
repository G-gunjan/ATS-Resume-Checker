## Demo
https://free-ats-resume-checker.streamlit.app/
# ATS Resume Checker 📄✅

An AI-powered **ATS (Applicant Tracking System) Resume Analyzer** built using **Streamlit** and **Google Gemini**.  
This app helps candidates evaluate their resume against a job description and get actionable insights.

---

## 🚀 Features

- ✅ Resume vs Job Description analysis  
- 📊 ATS Match Percentage  
- 🧠 Skill improvement roadmap (90-day plan)  
- ✍️ Resume optimization suggestions  
- 🎯 Role recommendations based on profile  

---

## 🛠 Tech Stack

- Python  
- Streamlit  
- Google Gemini API  
- pdf2image  
- Poppler (for PDF processing)

---
## ⚙️ Setup Instructions 
### 1️⃣ Clone the repository
```bash
git clone https://github.com/G-gunjan/ATS-Resume-Checker.git
cd ATS-Resume-Checker
```
### 2️⃣ Create virtual environment
```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```
### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```
### 4️⃣ Add Google API Key
Create a .env file:
```bash
GOOGLE_API_KEY=your_api_key_here
```
### Usage

Run the Streamlit app locally:
```bash
streamlit run app.py
```
* Enter the Job Description.

* Upload your Resume (PDF).

* Click the desired button:

* Tell Me About the Resume

* Percentage Match

* How Can I Improvise My Skills

* Optimize the Resume

* Recommend Job Roles

* Get AI-generated insights instantly.

### Dependencies

* Python 3.10+

* Streamlit

* Google Generative AI (google-generativeai)

* pdf2image

* Pillow

* PyMuPDF (fitz)

* python-dotenv
## Contribution
Contributions to the ATS Resume Checker project are welcome. To contribute:

* Fork the repository.
* Create a new branch (git checkout -b feature-branch).
* Make your changes and commit them (git commit -m 'Add some feature').
* Push to the branch (git push origin feature-branch).
* Open a pull request.
## License
This project is licensed under the MIT License. See the LICENSE file for more details.

## Acknowledgments
Thanks to Google for providing the Generative AI API.
Special thanks to the Streamlit team for their user-friendly web application framework.
For any questions or issues, please open an issue in the repository.
