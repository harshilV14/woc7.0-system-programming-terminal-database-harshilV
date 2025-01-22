def main():
    from database.py import DatabaseManager
    from cli.py import CLI

    print("Welcome to DBMS........")
    print("Enter 'help' to show available commands  |  Enter 'exit' to quit")

    cli = CLI()
    cli.run()

if __name__ == "__main__":
    main()