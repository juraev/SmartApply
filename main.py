import gradio as gr

from textgen.llm import ChatGPT

def generate_cover_letter(resume, job_description):

    chatgpt = ChatGPT()

    # prepare the messages for the chatbot
    messages = [
        {
            "role": "system",
            "content": '''Users gives a resume and a job description. 
                    Create a cover letter for the job description based on the resume.'''
        }, 
        {
            "role": "user",
            "content": "Please, make it accurate and professional. I am counting on you and tip you 20% of my salary if I get the job."
        },
        {
            "role": "user",
            "content": resume
        },
        {
            "role": "user",
            "content": job_description
        }
    ]


    generated_text = f"Input 1: {resume}\nInput 2: {job_description}"
    return generated_text

inputs = [
    
    gr.Textbox(label="Resume", lines=10),
    gr.Textbox(label="Job Description", lines=10)
]

output = gr.Textbox(label="Cover Letter", lines=20)

gr.Interface(title="Smart Cover Letter", fn=generate_cover_letter, inputs=inputs, outputs=output).launch()
