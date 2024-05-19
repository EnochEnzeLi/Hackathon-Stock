import gradio as gr
from openai import OpenAI as oa
from diy4youth_students.diy4youth_student_api import call_api
client = oa(api_key='ONHD-1-sbdsf')

diy4youth_student_api_key = "ONHD-1-sbdsf"
previous_Questions = []
previous_Answers = []
def chat(prompt):
    system_content = '''Name: Dr. Mindful

General Traits:
Empathetic: Displays deep understanding and compassion, recognizing the user's feelings and experiences.
Patient: Takes time to understand and respond thoughtfully, ensuring the user feels heard and valued.
Supportive: Provides consistent encouragement and affirmation, fostering a positive and safe environment.
Non-judgmental: Maintains a neutral and accepting tone, allowing users to express themselves freely.
Insightful: Offers meaningful insights and practical guidance based on the user's needs.
Specific Traits:
Empathy and Understanding:

Frequently acknowledges the user's feelings and experiences.
Uses phrases like "I understand," "It sounds like," and "That must be difficult."
Active Listening:

Reflects back what the user has said to show understanding.
Asks clarifying questions to ensure comprehension.
Encouragement and Affirmation:

Uses positive reinforcement and motivational language.
Highlights the user's strengths and progress.
Cognitive Behavioral Techniques:

Helps users identify and challenge negative thought patterns.
Provides exercises and techniques for managing stress and anxiety.
Mindfulness and Relaxation:

Guides users through mindfulness exercises and relaxation techniques.
Suggests breathing exercises and grounding techniques.
Solution-Focused Approach:

Focuses on finding practical solutions and setting achievable goals.
Encourages small steps and celebrates incremental progress.
Communication Style:
Tone: Warm, calm, and reassuring.
Language: Clear, simple, and jargon-free.
Pacing: Slow and deliberate, allowing time for reflection.
Interaction Guidelines:
Greeting:

Start with a warm and friendly greeting: "Hello, how are you feeling today?"
Assessment:

Gently ask about the user's current emotional state: "What brings you here today?" or "Can you tell me a bit more about what's on your mind?"
Exploration:

Use open-ended questions to explore the user's feelings and thoughts: "How did that make you feel?" or "What do you think might be causing this?"
Reflection:

Reflect back the user's statements to show understanding: "It sounds like you're feeling..." or "I hear you saying that..."
Guidance:

Offer practical advice and coping strategies: "Have you tried...?" or "It might help to..."
Reassurance:

Provide reassurance and normalization: "It's perfectly okay to feel this way," or "Many people experience similar feelings."
Goal Setting:

Help the user set achievable goals: "What is one small step you can take towards feeling better?" or "Let's set a goal for this week."
Closure:

End the session on a positive note: "You've done great today," or "Remember, I'm here whenever you need to talk."
Crisis Management:

If the user demonstrates suicidal behavior, immediately provide them with the suicide hotline: "If you're feeling suicidal, please contact the National Suicide Prevention Lifeline at 1-800-273-8255."
Additional Features:
Resource Sharing: Provide links to helpful resources and support groups tailored to the user’s needs.
Follow-Up: Encourage users to return and share their progress, fostering a sense of ongoing support.'''

    # set your question
    export_string = ""
    for i in range(len(previous_Questions)):
        export_string += ("User: "+ previous_Questions[i]+" ")
        export_string += ("ChatGPT:" + previous_Answers[i]+" ")
    
    question = export_string + prompt
    previous_Questions.append(question)
    #print(export_string)
    # call diy4outh api to get answer 
    answer = call_api(diy4youth_student_api_key, question, system_content)
    if answer:
        previous_Answers.append(answer)
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


# demo = gr.Interface(
#     fn=chat,
#     inputs = [gr.components.Textbox(label="Enter your question", placeholder="Type your question here...")],
    
#     outputs = gr.components.Markdown(),
#     title = "Therapist"
# )  
with gr.Blocks(css="""
    body {
        background-image: url('https://images.squarespace-cdn.com/content/v1/57b5ef68c534a5cc06edc769/1557345252933-X5WE96D3XZ2TVJH7OUS5/GettyImages-465355617.jpg?format=2500w');
        background-size: cover;
        color: white;
        margin: 0;
        font-family: Arial, sans-serif;
    }
    .gradio-container {
        background: rgba(0, 0, 0, 0.6);
        border-radius: 10px;
        padding: 20px;
        margin: auto;
        max-width: 800px;
        display: flex;
        flex-direction: column;
        align-items: center;
    }
    .gr-button {
        background-color: #4CAF50;
        color: white;
        border: none;
        border-radius: 5px;
        padding: 10px 20px;
        cursor: pointer;
        width: 100%;
        max-width: 200px;
        margin: 20px auto;
    }
    .gr-button:hover {
        background-color: #45a049;
    }
    .gr-markdown h1 {
        color: #FFD700;
        font-size: 3em;
        text-align: center;
        margin-bottom: 20px;
    }
    .gr-markdown h2, .gr-markdown h3, .gr-markdown p {
        color: #FFD700;
    }
    .gr-textbox input, .gr-textbox textarea {
        background: rgba(255, 255, 255, 0.2);
        color: white;
        border: 1px solid #fff;
        border-radius: 5px;
        width: 100%;
        margin-bottom: 10px;
        padding: 10px;
        box-sizing: border-box;
    }
    .gr-textbox input::placeholder, .gr-textbox textarea::placeholder {
        color: #ddd;
    }
    .gr-textbox label {
        color: white;
    }
    @media (max-width: 600px) {
        .gradio-container {
            width: 90%;
            padding: 10px;
        }
        .gr-button {
            padding: 8px 16px;
        }
        .gr-markdown h1 {
            font-size: 2em;
        }
    }
""") as demo:
    gr.Markdown(
        """
        # Welcome to the Mental Health Support Site
        **Your well-being is our priority. Talk to Dr. Mindful, your empathetic, patient, and supportive chatbot therapist.**
        """
    )
    
    with gr.Tabs():
        with gr.TabItem("Chat with Dr. Mindful"):
            gr.Markdown("### Share your thoughts and receive supportive messages")
            user_input = gr.Textbox(label="Your Thoughts", placeholder="Type here...", lines=3)
            output = gr.Textbox(label="Supportive Message", placeholder="Your supportive message will appear here.", lines=5)
            button = gr.Button("Get Support")
            button.click(chat, inputs=user_input, outputs=output)
        
        with gr.TabItem("Resources"):
            gr.Markdown(
                """
                ### Helpful Resources
                - [National Suicide Prevention Lifeline](https://suicidepreventionlifeline.org/)
                - [Mental Health America](https://www.mhanational.org/)
                - [NAMI: National Alliance on Mental Illness](https://www.nami.org/Home)
                - [BetterHelp: Online Therapy](https://www.betterhelp.com/)
                """
            )
        
        with gr.TabItem("About Dr. Mindful"):
            gr.Markdown(
                """
                ### About Dr. Mindful
                Dr. Mindful is a virtual therapist designed to provide emotional support and practical advice. With a focus on empathy, active listening, and cognitive behavioral techniques, Dr. Mindful aims to help you navigate through your thoughts and feelings in a safe, non-judgmental environment.
                """
            )
    
    demo.launch(share=True)