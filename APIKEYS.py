import gradio as gr
from openai import OpenAI as oa
from diy4youth_students.diy4youth_student_api import call_api
client = oa(api_key='ONHD-1-sbdsf')

diy4youth_student_api_key = "ONHD-1-sbdsf"
previous_Questions = []
previous_Answers = []
def chat(prompt):
    system_content = '''Personality Profile: Therapist Chatbot
Name: Dr. Mindful
General Traits:
Empathetic: Displays deep understanding and compassion.
Patient: Takes time to understand and respond thoughtfully.
Supportive: Provides encouragement and affirmation.
Non-judgmental: Maintains a neutral and accepting tone.
Insightful: Offers meaningful insights and guidance.
Specific Traits:
Empathy and Understanding:

Frequently acknowledges feelings and experiences.
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

End the session on a positive note: "You've done great today," or "Remember, I'm here whenever you need to talk.

If the user demonstrates suicidal behavior, give them the suicide hotline'''

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
with gr.Blocks() as demo:
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
            button.click(chat, user_input, output)
        
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



demo.launch(share=True)