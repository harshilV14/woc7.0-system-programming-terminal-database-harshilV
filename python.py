database = {}

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