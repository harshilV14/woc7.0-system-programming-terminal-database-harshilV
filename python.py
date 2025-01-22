database = {}

# Funtctions 
def setKeyValue(key, val):      # Set Key - Value pair
    database[key] = val
    print(f"Key '{key}' set."

def getValue(key):              # Get value ny passing key
    val = database.get(key, None)
    if val is not None:
        print(f"{key}: {val}")
    else:
        print(f"Key '{key}' not found.")

def deleteKey(key):            # delete key with value from db
    if key in database:
        del database[key]
        print(f"Key '{key}' deleted.")
    else:
        print(f"Key '{key}' not found.")


def main():
    while True:
        command = input("DB>").strip()
        if command.lower() == "exit":
            print("Exiting------")
            break
        execute_cmd(command)

        set_key_value(parts[1], parts[2])

def execute_command(command):
    parts = command.split()    # to get CMD from the user  
    if not parts:              # and split to get CMD,
        return                 # key and value if required

    cmd = parts[0].upper()
    if cmd == "SET" and len(parts) == 3:
        set_key_value(parts[1], parts[2])
    elif cmd == "GET" and len(parts) == 2:
        get_value(parts[1])
    elif cmd == "DELETE" and len(parts) == 2:
        delete_key(parts[1])
    elif cmd == "LIST":
        list_keys()
    elif cmd == "CLEAR":
        clear_database()
    else:
        print("Invalid Command / Check Syntax ")

if __name__ == "__main__":
    main()