import gradio as gr
import json

from textgen.llm import ChatGPT

def generate_cover_letter(resume, job_description):

    chatgpt = ChatGPT()

    # prepare the messages for the chatbot
    messages = [
        {
            "role": "system",
            "content": '''Users gives a resume and a job description. 
                    Create a cover letter for the job description based on the resume and save it.'''
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

    prompt = {
        "messages": messages,
        "tools": [
            {
                "type": "function",
                "function":{
                    "name": "save_cover_letter",
                    "description": "Save the given cover letter.",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "cover_letter":{
                                "type": "string",
                                "description": "The cover letter to save."
                            }
                        }
                    }
                }
            }
        ],
        "tool_choice": "auto"
    }

    response = chatgpt.generate_text(prompt)
    
    cover_letter_args_json = response.choices[0]\
        .message.tool_calls[0].function.arguments
    
    cover_letter = json.loads(cover_letter_args_json)["cover_letter"]
    
    return cover_letter

inputs = [
    
    gr.Textbox(label="Resume", lines=10),
    gr.Textbox(label="Job Description", lines=10)
]

output = gr.Textbox(label="Cover Letter", lines=20)

gr.Interface(title="Smart Cover Letter", fn=generate_cover_letter, inputs=inputs, outputs=output).launch()
