import  openai



"""
Info:
- Module OpenAI: https://github.com/openai/openai-python
- Doc API ChatGPT: https://platform.openai.com/docs/api-reference/chat
"""


def main():
    
    # Set openai api key
    openai.api_key_path =  "api_key_path/apikey"
    
    response = openai.ChatCompletion.create(model = "gpt-3.5-turbo",
    messages = [{"role": "user", "content": "Grado mayor de la masoneria?"}])
    
    print(response)
                                                                               
    
if __name__ == "__main__":
    main()