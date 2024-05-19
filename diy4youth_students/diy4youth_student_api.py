# DIY4Youth provides api for the k12 students to learn AI technology, please do not misuse it.
import requests


def call_api(diy4youth_student_api_key, prompt, system_content=None):
    """
    Calls the API at the specified URL and returns the data.

    Parameters:
    diy4youth_student_api_key (str): Student's access key for the diy4youth services.
    prompt (str): The user role's content.
    system_content (str): The system role's content if applicable, None otherwise.

    Returns:
    str: The data received from the API if successful, None otherwise.
    """
    try:
        if diy4youth_student_api_key and prompt:
            url = "https://www.diy4youth.org/ai/gpt"  # "http://127.0.0.1:5050/ai/gpt"  # fixed url for diy4youth students only

            data = {
                "diy4youth_student_api_key": diy4youth_student_api_key,
                "prompt": prompt,
                "system_content": system_content
            }

            response = requests.post(url, json=data)
            print("remote response", url, response)
            return response.json()
        else:
            print("Missing parameter")
            return None
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

