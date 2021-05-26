from config.rich_configuration import console

emphasize = lambda word: f"[magenta]{word}[/]"
confirmation = lambda sentence: console.print(f"[green]✔ {sentence}[/]")
