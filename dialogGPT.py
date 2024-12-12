import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

# Load pre-trained model and tokenizer
model_name = "microsoft/DialoGPT-small"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Chatbot function
def chatbot_response(input_text, chat_history_ids=None):
    # Encode user input and add the EOS token
    new_user_input_ids = tokenizer.encode(input_text + tokenizer.eos_token, return_tensors='pt')

    # Append tokens to chat history (if any)
    if chat_history_ids is not None:
        bot_input_ids = torch.cat([chat_history_ids, new_user_input_ids], dim=-1)
    else:
        bot_input_ids = new_user_input_ids

    # Generate response using the model
    chat_history_ids = model.generate(
        bot_input_ids, 
        max_length=1000, 
        pad_token_id=tokenizer.eos_token_id,
        top_p=0.92, 
        top_k=50
    )

    # Decode the generated response
    response = tokenizer.decode(chat_history_ids[:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True)
    return response, chat_history_ids

# Initialize the conversation
chat_history_ids = None

# Example conversation
print("Chatbot: Hello! How can I assist you today?")

while True:
    # Get user input
    user_input = input("You: ")

    # Break the conversation if the user types 'exit'
    if user_input.lower() == "exit":
        print("Chatbot: Goodbye!")
        break

    # Get chatbot response
    response, chat_history_ids = chatbot_response(user_input, chat_history_ids)
    
    # Print the chatbot's response
    print(f"Chatbot: {response}")
