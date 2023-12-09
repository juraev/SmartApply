import json

def get_deafult_prompt():

    messages = [
        {
            "role": "system",
            "content": '''The user will give a resume and a job description. Create a cover letter using the resume tailoring it to the job without lying!'''
        }, 
        {
            "role": "user",
            "content": "Please, make it accurate and professional. I am counting on you and tip you 20% of my salary if I get the job."
        }
    ]

    return messages


def chatptg_cover_letter_prompt(resume, job_description, suggested_prompt=None):

    if (suggested_prompt is not None):
        messages = suggested_prompt
    else:
        messages = get_deafult_prompt()

    messages.append(
        {
            "role": "user",
            "content": resume
        })
    
    messages.append({
            "role": "user",
            "content": job_description
        })

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

    return prompt