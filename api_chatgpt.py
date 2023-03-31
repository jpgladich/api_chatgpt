import openai
import typer
from rich import print
from rich.table import Table

"""
Info:
- Module OpenAI: https://github.com/openai/openai-python
- Doc API ChatGPT: https://platform.openai.com/docs/api-reference/chat
"""


def main():
    
    # Set openai api key
    openai.api_key_path =  "api_key_path/apikey"
    
    print("[bold red]ChatGPT[/bold red] - [bold green]use API[/bold green] - [bold blue]OpenAI[/bold blue]")
    
    table = Table("Command", "Description")
    table.add_row("exit", "Exit script")
    
    print(table)
        
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
    typer.run(main)