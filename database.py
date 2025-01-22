import os
import json


class DatabaseManager:
    def __init__(self):
        self.current_database = None

    def createDatabase(self, databaseName):
        file_name = f"{databaseName}.json"
        if os.path.exists(file_name):
            return f"Database {databaseName} already exists."
        with open(file_name, "w") as dbFile:
            json.dump({}, dbFile)
        return f"Database {databaseName} created."
    
    def listDatabases(self):
        databases = [f for f in os.listdir() if f.endswith('.json')]
        return databases if databases else "No databases found."

    def listTables(self):
        if not self.current_database:
            return "No database selected. Use USE DATABASE <databaseName> first."
        file_name = f"{self.current_database}.json"
        with open(file_name, "r") as dbFile:
            data = json.load(dbFile)
        return list(data.keys()) if data else ["No tables found."]

    def useDatabase(self, databaseName):
        file_name = f"{databaseName}.json"
        if not os.path.exists(file_name):
            return f"Database {databaseName} does not exist."
        self.current_database = databaseName
        return f"Using database: {databaseName}"

    def createTable(self, tableName):
        if not self.current_database:
            return "No database selected. Use USE DATABASE <databaseName> first."
        file_name = f"{self.current_database}.json"
        with open(file_name, "r+") as dbFile:
            data = json.load(dbFile)
            if tableName in data:
                return f"Table {tableName} already exists."
            data[tableName] = []
            dbFile.seek(0)
            json.dump(data, dbFile, indent=4)
        return f"Table {tableName} created successfully."

    def insertEntry(self, tableName, entry):
        if not self.current_database:
            return "No database selected. Use USE DATABASE <databaseName> first."
        file_name = f"{self.current_database}.json"
        with open(file_name, "r+") as dbFile:
            data = json.load(dbFile)
            if tableName not in data:
                return f"Table {tableName} does not exist."
            primaryKey = list(entry.keys())[0]
            if any(row.get(primaryKey) == entry[primaryKey] for row in data[tableName]):
                return f"Primary key {primaryKey} must be unique."
            data[tableName].append(entry)
            dbFile.seek(0)
            json.dump(data, dbFile, indent=4)
        return f"Entry added to table {tableName}."

    def listEntries(self, tableName):
        if not self.current_database:
            return "No database selected. Use USE DATABASE <databaseName> first."
        file_name = f"{self.current_database}.json"
        with open(file_name, "r") as dbFile:
            data = json.load(dbFile)
            if tableName not in data:
                return f"Table {tableName} does not exist."
        return (
            data[tableName] if data[tableName] else f"No entries in table {tableName}."
        )

    def deleteEntry(self, tableName, value):
        if not self.current_database:
            return "No database selected. Use USE DATABASE <databaseName> first."
        file_name = f"{self.current_database}.json"
        with open(file_name, "r+") as dbFile:
            data = json.load(dbFile)
            if tableName not in data:
                return f"Table {tableName} does not exist."
            original_length = len(data[tableName])
            data[tableName] = [
                entry for entry in data[tableName] if entry.get("id") != value
            ]
            if len(data[tableName]) == original_length:
                return f"Entry with primary key {value} not found."
            dbFile.seek(0)
            json.dump(data, dbFile, indent=4)
            dbFile.truncate()
        return f"Entry with primary key {value} deleted from table {tableName}."
