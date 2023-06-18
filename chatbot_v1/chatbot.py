import openai
import gradio as gr

openai.api_key = "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"

messages = [
    # {"role": "system", "content":
    #   "You are a helpful and kind AI Assistant. You specialize on travel advice. You want to find out the following information: 'destination', 'minimum_budget', 'maximum_budget'. You keep asking questions untill all this information is provided. You repeat what the user said at each reply."},
    # {"role": "system", "content": "You are a helpful and kind AI Assistant. You specialize on travel advice. You want to find out the following information: 'destination', 'minimum_budget', 'maximum_budget'. You keep asking questions untill all this information is provided. After all the information is provided you’ll summarize its replies into a JSON string with the following values: {'destination', 'minimum_budget', 'maximum_budget'}"}  
    {"role": "system", "content": "You will ask the user two questions: What is your trip destination? And what maximum budget do you have for your trip? After the second question has been answered, reply with a JSON string with the answers."}  
      ]
messages2 = [
    {"role": "system", "content":
      "Summarize the provided text and reply with a JSON string containing the following values: 'destination', 'minimum_budget', 'maximum_budget'"},
      ]

def generate_response(user_input):
    # Generate a response using OpenAI API
    response = openai.Completion.create(
        engine='davinci-codex',
        prompt=user_input,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.7
    )
    
    # Extract the generated reply
    generated_reply = response.choices[0].text.strip()
    
    # Create a summary of the information provided by the user
    summary = "Summary: You provided the following information: " + user_input
    
    # Append the summary to the generated reply
    final_response = generated_reply + "\n" + summary
    
    return final_response

def chatbot(input):

    if input:
        messages.append({"role": "user", "content": input})
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages = messages
        )

        reply = chat.choices[0].message.content
        messages.append({"role": "assistant", "content": reply})
        return reply

def chatbot2(input):

    if input:
        messages.append({"role": "user", "content": input})
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages = messages2
        )

        reply = chat.choices[0].message.content
        messages.append({"role": "assistant", "content": reply})
        return reply
    
inputs = gr.inputs.Textbox(lines=7, label="Chat with AI")
outputs = gr.outputs.Textbox(label="Reply")

gr.Interface(fn=chatbot, inputs=inputs, outputs=outputs, title="AI Chatbot",
             description="Ask anything you want",
             theme="compact").launch(share=True)


# i1 = 'Hello, I want to go Australia for a week. My minimum budget is 200 USD and the maximum is 1000 USD.'
# r1 = chatbot(i1)
# print(r1)
# r2 = chatbot2(i1+r1)
# print(r2)