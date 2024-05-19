import gradio as gr
from openai import OpenAI as oa
from diy4youth_students.diy4youth_student_api import call_api
client = oa(api_key='ONHD-1-sbdsf')

diy4youth_student_api_key = "ONHD-1-sbdsf"

def chat(prompt,system):
    system_content = system

    # set your question
    question = prompt

    # call diy4outh api to get answer 
    answer = call_api(diy4youth_student_api_key, question, system_content)
    if answer:
        return answer
    else:
        return print("Failed to fetch data.")

# def chat(prompt,system):


#     questions = [
#         {"role":"system", "content": system},
#         {"role":"user","content": prompt}
#     ]

#     response = client.chat.completions.create(
#         model="gpt-3.5-turbo",
#         messages=questions
#     )

#     return response.choices[0].message.content


demo = gr.Interface(
    fn=chat,
    inputs = [gr.components.Textbox(label="Enter your question", placeholder="Type your question here..."),
              gr.components.Textbox(label="Enter your system", placeholder="Type your question here...")],
    
    outputs = gr.components.Markdown(),
    title = "Therapist"
    
)


demo.launch(share = True)