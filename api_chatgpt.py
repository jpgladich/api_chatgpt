import openai



"""
Info:
- Module OpenAI: https://github.com/openai/openai-python
- Doc API ChatGPT: https://platform.openai.com/docs/api-reference/chat
"""


def main():
    
    # Set openai api key
    openai.api_key_path =  "api_key_path/apikey"
        
    # Set context "system"
    messages = [{"role": "system", "content": "Assistant Devops, programmer, sysadmin"}]
        
    while True:

        ask = input("Ask: ")
        
        if ask == "exit":
            break
        
        messages.append({"role": "user", "content": ask})
        
        
        response = openai.ChatCompletion.create(model = "gpt-3.5-turbo",messages = messages)
        
        response_ask = response.choices[0].message.content
        
        messages.append({"role": "assistant", "content": response_ask})
        
        print(response_ask)
                                                                               
    
if __name__ == "__main__":
    main()