import typer
import json
import asyncio
app = typer.Typer()



json_template = dict[
    "timestamp": str,
    "amount": float,
    "currency": str,
    "type": str,
    "raw_data": str,
    ]

json_list: list[dict[str,str | float]] = []

#i want to have no repeition in the checking of the amount non float value, so i will create a function that takes the amount as a string and returns a float value, and if there is an error it will return 0.0 and print an error message
def parse_amount(amount_str: str) -> float:
    #i want to have logic that only allows positive amounts, so i will check if the amount is negative and if it is, i will print an error message and return 0.0
    try:
        return float(amount_str)
    except (ValueError, TypeError):
        print(f"Error: Invalid amount '{amount_str}'. Assigning 0.0.")
        return 0.0



def parse_line (line: str) -> dict[str,str | float]:
    #split line by spaces
    parts = line.split()
    #if there are less than 4 parts, the line is not in the correct format and i want to prevent the program from crashing, so i will print an error message and return an empty dictionary
    if len(parts) < 4:
        print(f"Error: Line '{line}' is not in the correct format. Expected at least 4 parts but got {len(parts)}.")
        #i want to have the part thats missing to have the same type but have "unknown" or 0.0 as the value, so i will check which part is missing and assign the appropriate value
        timestamp = parts[0] if len(parts) > 0 else "unknown"
        #use a safe token so missing amount defaults instead of crashing from parts[1]
        amount_token = parts[1] if len(parts) > 1 else "0.0"
        amount = parse_amount(amount_token)
       
        currency = parts[2] if len(parts) > 2 else "unknown"
        transaction_type = parts[3] if len(parts) > 3 else "unknown"
    else:
        #assign each part to a variable
        timestamp = parts[0]
        #i want to be able to handle the case where the amount is not a valid float, so i will use a try-except block to catch the exception and assign 0.0 as the value if there is an error
        amount = parse_amount(parts[1])
        currency = parts[2]
        transaction_type = parts[3]
    data = {
        "timestamp": timestamp,
        "amount": amount,
        "currency": currency,
        "type": transaction_type,
        "raw_data": line
    }
    json_list.append(data)
    return data
   


@app.command("parse-file")
def parse_file(file_path: str):
    json_list.clear()
    with open(file_path, "r") as f:
        for line in f:
            stripped_line = line.strip()
            if not stripped_line:
                continue
            parse_line(stripped_line)

        with open("results.txt", "w") as f:
            f.write(json.dumps(json_list, indent=2))  
        typer.echo("results.txt has been created with the parsed data.") 



async def catagorise():
    async with asyncio.TaskGroup() as tg:
        for item in json_list:
            with open("results.txt", "w") as f:
                f.write(json.dumps(item, indent=4))


    print("results.txt has been created with the parsed data.")





if __name__ == "__main__":
    app()
