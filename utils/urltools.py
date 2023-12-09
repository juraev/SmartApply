
import requests
from bs4 import BeautifulSoup
import json

from utils.prompts import get_job_extraction_prompt

def extract_job_description(url, llm):
    try:
        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract text from the parsed HTML
        text = soup.get_text(separator='\n')

        prompt = get_job_extraction_prompt(text)

        response = llm.generate_text(prompt)

        job = response.choices[0]\
        .message.tool_calls[0].function.arguments

        job_description = json.loads(job)["job"]

        return job_description, True

    except Exception as e:
        return f"An error occurred while retrieving the job data: {e}", False


# if __name__ == "__main__":
#     from utils.llmtools import ChatGPT, GPT_4_5_TURBO, GPT_3_5_TURBO

#     chatgpt = ChatGPT(GPT_3_5_TURBO)
    
#     url = "https://boards.eu.greenhouse.io/mariadbplc/jobs/4226790101"
#     chatgpt = ChatGPT(GPT_4_5_TURBO)
#     print(extract_job_description(url))
