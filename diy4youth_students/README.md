
# DIY4Youth API Client

## Description
This is a simple API client package for the DIY4Youth students calling a predefined API and fetching data.

## Installation

1. Unzip the diy4youth_students.zip
2. Put the diy4youth_students folder under your project
3. Install requests library

```
pip install requests
```

## Basic Usage

Here is a simple example of how to use this client:

```python
from diy4youth_students.diy4youth_student_api import call_api

# set the diy4youth student api key
diy4youth_student_api_key = "your-idy4youth-student-api-key"

# set your question
question = "tell me a joke"

# call diy4outh api to get answer 
answer = call_api(diy4youth_student_api_key, question)
if answer:
    print(answer)
else:
    print("Failed to fetch data.")
```

## Advanced Usage

Here is an example of how to add system content:

```python
from diy4youth_students.diy4youth_student_api import call_api

# set the diy4youth student api key
diy4youth_student_api_key = "your-idy4youth-student-api-key"

# set your question
system_content = "You are a K12 teacher."

# set your question
question = "I am a grade 1 student, please teach me math."

# call diy4outh api to get answer 
answer = call_api(diy4youth_student_api_key, question, system_content)
if answer:
    print(answer)
else:
    print("Failed to fetch data.")
```
