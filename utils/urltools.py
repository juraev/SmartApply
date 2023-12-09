
import requests
from bs4 import BeautifulSoup
import re

def extract_job_description(url):
    try:
        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, 'html.parser')

        # Look for specific patterns
        # Adjust these patterns based on the common structures you observe
        for pattern in ['job-description', 'job-details', 'description']:
            tag = soup.find_all(class_=re.compile(pattern))
            if tag:
                return ' '.join([t.get_text(separator='\n', strip=True) for t in tag])

        # Fallback: Search for headings that might indicate job description
        for heading in soup.find_all(['h1', 'h2', 'h3']):
            if 'job' in heading.get_text().lower() or 'description' in heading.get_text().lower():
                return heading.find_next_sibling().get_text(separator='\n', strip=True)

        # Final fallback: Extract from main or article tags
        main_content = soup.find(['main', 'article']) or soup
        return main_content.get_text(separator='\n', strip=True)

    except Exception as e:
        return f"An error occurred: {e}"

# Example usage
url = "https://boards.eu.greenhouse.io/mariadbplc/jobs/4226790101"
print(extract_job_description(url))
