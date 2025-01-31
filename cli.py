import sys
from database import DatabaseManager

class CLI:
    def __init__(self):  # Corrected method name
        self.database = DatabaseManager()

    def run(self):
        print("Enter 'help' to list commands.")
        while True:
            try:
                command = input("> ").strip()
                if command.lower() == "exit":
                    print("Exiting.......")
                    break
                self.handle_command(command)
            except Exception as e:
                print(f"Error: {e}")

    def handle_command(self, command):
        tokens = command.split()
        if not tokens:
            return

        cmd = tokens[0].lower()

        if cmd == "create" and len(tokens) > 2 and tokens[1].lower() == "database":
            db_name = tokens[2]
            print(self.database.createDatabase(db_name))

        elif cmd == "list" and len(tokens) > 1 and tokens[1].lower() == "databases":
            print("\n".join(self.database.listDatabases()))

        elif cmd == "use" and len(tokens) > 2 and tokens[1].lower() == "database":
            db_name = tokens[2]
            print(self.database.useDatabase(db_name))

        elif cmd == "create" and len(tokens) > 2 and tokens[1].lower() == "table":
            table_name = tokens[2]
            print(self.database.createTable(table_name))

        elif cmd == "insert" and len(tokens) > 3 and tokens[1].lower() == "into":
            table_name = tokens[2]
            try:
                entry = eval(" ".join(tokens[3:]))
                if isinstance(entry, dict):
                    print(self.database.insertEntry(table_name, entry))
                else:
                    print(
                        "Invalid entry format. Use a dictionary format (e.g., {'id': 1, 'name': 'Alice'})."
                    )
            except Exception as e:
                print(f"Error parsing entry: {e}")

        elif cmd == "list" and len(tokens) > 1 and tokens[1].lower() == "tables":
            print("\n".join(self.database.listTables()))

        elif (
            cmd == "list"
            and len(tokens) > 3
            and tokens[1].lower() == "entries"
            and tokens[2].lower() == "in"
        ):
            table_name = tokens[3]
            entries = self.database.listEntries(table_name)
            if isinstance(entries, list):
                for entry in entries:
                    print(entry)
            else:
                print(entries)

        elif (
            cmd == "delete"
            and len(tokens) > 4
            and tokens[1].lower() == "entry"
            and tokens[2].lower() == "from"
        ):
            table_name = tokens[3]
            try:
                primary_key_value = int(tokens[5])  # Assuming primary key is an integer
                print(self.database.deleteEntry(table_name, primary_key_value))
            except Exception as e:
                print(f"Invalid primary key value: {e}.")

        elif cmd == "help":
            self.print_help()

        else:
            print("Invalid command. Type 'help' for a list of valid commands.")

    def print_help(self):
        print(
            """
Commands:
  CREATE DATABASE <database_name>       - Create a new database.
  LIST DATABASES                        - List all databases.
  USE DATABASE <database_name>          - Select a database to work with.
  CREATE TABLE <table_name>             - Create a new table in the current database.
  INSERT INTO <table_name> <entry>      - Add a new entry to a table (use dictionary format for entry).
  LIST TABLES                           - List all tables in the current database.
  LIST ENTRIES IN <table_name>          - List all entries in a specified table.
  DELETE ENTRY FROM <table_name> WHERE id=<value>
                                        - Delete a specific entry using its primary key.
  EXIT                                  - Exit the application.
        """
        )
