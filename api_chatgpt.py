import openai
import typer
import datetime
from rich import print
from rich.table import Table

"""
Info:
- Module OpenAI: https://github.com/openai/openai-python
- Create you API key: https://platform.openai.com/account/api-keys
- Doc API ChatGPT: https://platform.openai.com/docs/api-reference/chat
"""


def main():
    
    # Set openai api key
    openai.api_key_path =  "api_key_path/apikey"
    
    print("[bold red]ChatGPT[/bold red] - [bold green]use API[/bold green] - [bold blue]Script[/bold blue]")
    
    table = Table("Command", "Description")
    table.add_row("exit", "Exit script")
    table.add_row("new", "Create new chat context")
    table.add_row("save", "Save chat context in local file")

    
    print(table)
    
    # Clear context
    context = [{"role": "system", "content": "Assistant Devops, programmer, sysadmin"}]
        
    # Set context "system"
    messages = context
        
    while True:

        content = __prompt()
        
        if content == "new":
            print("New context created")
            messages = [context]
            content = __prompt()
            
        if content == "save":
            now = datetime.datetime.now()
            filename = now.strftime("%Y%m%d_%H_%M_%S") + ".txt"
            __save_file(response_ask, filename)
            print("Context saved in local file")
            content = __prompt()
                
        messages.append({"role": "user", "content": content})
                
        response = openai.ChatCompletion.create(model = "gpt-3.5-turbo",messages = messages)
        
        response_ask = response.choices[0].message.content
        
        messages.append({"role": "assistant", "content": response_ask})
        
        print(f"[bold green]> [/bold green] [green]{response_ask}[/green]")
        
    
def __prompt() -> str:
    
    prompt = typer.prompt("\n¿Ask? ")

    if prompt == "exit":
        exit = typer.confirm("¿You're sure?")
        if exit:
            print("¡Bye!")
            raise typer.Abort()
        
        return __prompt()

    return prompt

# save file context in local file
def __save_file(message, filename):
    with open(filename, "w") as f:
        f.write(str(message))
    print(f"Response saved to file: {filename}")
                              
    
if __name__ == "__main__":
    typer.run(main)