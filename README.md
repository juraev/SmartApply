# Smart Apply


## Introduction
This Gradio app is designed to automatically generate a tailored cover letter based on a user's resume and a specific job description. Currently only ChatGPT is supported as the text generation model, but more models will be added in the future.


## Features
- **Input Resume**: Upload your resume in a text or PDF format.
- **Input Job Description**: Paste the job description or a URL to the job posting.
- **Modify LLM prompt**: Modify the LLM prompt to customize the generated cover letter.
- **Generate Cover Letter**: Automatically creates a cover letter that aligns your skills and experiences with the job requirements.


## How to Use
1. **Start the App**: Run the app by executing `python app.py` in your terminal.
2. **Upload Resume**: Paste your resume or click the 'Upload Resume' button and select your resume file.
3. **Input Job Description**: Paste the job description into the text box or paste to the job posting url.
4. **Generate**: Click on 'Generate Cover Letter' to process your inputs.
5. **Download Cover Letter**: After processing, copy the generated cover letter.


## Installation
To set up this Gradio app on your local machine, follow these steps:
1. Clone this repository: `git clone [repository-link]`.
2. Install requirements: `pip install -r requirements.txt`.
3. Run the app: `python app.py`.


## Technologies Used
- **Python**: Primary programming language. (Metal GPU supporing python if used in Apple Silicon Macs with local llama2).
- **Gradio**: For creating the web interface.
- **PyPDF**: For parsing PDF files.

## Contributions
Contributions to this project are welcome. Please follow the standard fork-and-pull request workflow.





