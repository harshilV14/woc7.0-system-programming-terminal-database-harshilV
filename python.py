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

def execute_cmd(command):
    print("Cnd not implemented")

if __name__ == "__main__":
    main()