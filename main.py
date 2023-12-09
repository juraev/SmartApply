import json
from io import BytesIO

import gradio as gr

from utils.llmtools import ChatGPT, GPT_4_5_TURBO, GPT_3_5_TURBO
from utils.prompts import chatptg_cover_letter_prompt, get_deafult_prompt
from utils.pdftools import get_resume_from_bytes_pdf
from utils.urltools import extract_job_description


def generate_cover_letter_chatgpt(job_description, resume_text, resume_file, prompt):

    # Check if both or neither resume input is provided; or 
    # job description is empty;

    empty_resume = resume_text is None or resume_text == ""
    if empty_resume :
        if resume_file is None:
            return "Please provide a resume."
    else:
        if resume_file is not None:
            return "Please provide either text or a PDF file, but not both."

    if job_description is None or job_description == "":
        return "Please provide a job description."
    
    # I should add more robust check for this
    # also need to check if the promt is valid for the model
    try:
        prompt = json.loads(prompt)
    except json.decoder.JSONDecodeError:
        return "Please provide a valid JSON prompt."
        
    # read the resume from the file
    if empty_resume:
        # send BytesIO object to get_resume_from_bytes_pdf
        resume = get_resume_from_bytes_pdf(BytesIO(resume_file))
    else:
        resume = resume_text
    
    chatgpt = ChatGPT(GPT_4_5_TURBO)
    
    # check if the job description is url
    # making a simple test for now
    if job_description.startswith("http"):
        job_description, success = extract_job_description(job_description, chatgpt)

        if not success:
            return job_description

    # prepare the messages for the chatbot and generate the cover letter
    prompt = chatptg_cover_letter_prompt(resume, job_description, suggested_prompt=prompt)
    response = chatgpt.generate_text(prompt)
    
    cover_letter_args_json = response.choices[0]\
        .message.tool_calls[0].function.arguments
    
    cover_letter = json.loads(cover_letter_args_json)["cover_letter"]
    
    return cover_letter



def clear():
    return ["", "", json.dumps(get_deafult_prompt(), indent=4)]

def reset():
    return json.dumps(get_deafult_prompt(), indent=4)

def fill():
    with open("generated/resume.txt", "r") as file:
        resume = file.read()

    with open("generated/job_description.txt", "r") as file:
        job_description = file.read()

    return [job_description, resume]


with gr.Blocks(gr.themes.Soft()) as demo:
    gr.Markdown("# Smart Apply")
    with gr.Row():
        with gr.Column():
            tbJob = gr.Textbox(label="Job Description", lines=5, max_lines=10)
            tbPrompt = gr.Textbox(label="Prompt", lines=5, value=json.dumps(get_deafult_prompt(), indent=4))

            with gr.Row():
                fill_btn = gr.Button(value="Example Data")
                clear_btn = gr.Button(value="Clear")

            with gr.Row():
                reset_btn = gr.Button(value="Reset Prompt")
                submit_btn = gr.Button(value="Generate Cover Letter", variant="primary")


        with gr.Column():
            tbResume = gr.Textbox(label="Resume", lines=5, max_lines=10)
            fileResume = gr.File(label="Upload PDF Resume", file_types=[".pdf"], type="binary")
            tbCoverLetter = gr.Textbox(label="Cover Letter", lines=20)

        clear_btn.click(clear, inputs=[], outputs=[tbJob, tbResume, tbPrompt])
        reset_btn.click(reset, inputs=[], outputs=[tbPrompt])

        fill_btn.click(fill, inputs=[], outputs=[tbJob, tbResume])
        submit_btn.click(generate_cover_letter_chatgpt, inputs=[tbJob, tbResume, fileResume, tbPrompt], outputs=[tbCoverLetter])

demo.launch()