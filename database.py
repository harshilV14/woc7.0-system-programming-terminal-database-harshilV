import os
import json
def createDatabase(database_name):
    file_name = f"{database_name}.json"
    if os.path.exists(file_name):
        return f" '{database_name}' already exists"
    with open(file_name, 'w') as db_file:
        json.dump({}, db_file)
    return f"Database {database_name} created ."

def listDatabases():
    databases = [f for f in os.listdir() if f.endswith('.json')]
    return databases if databases else "No database found"

def accessDatabase(database_name):
    file_name = f"{database_name}.json"
    if os.path.exists(file_name):
        return file_name
    return f"Database {database_name} does not exist"

def createTable(database_name, tableName):
    file_name = f"{database_name}.json"
    if not os.path.exists(file_name):
        return f"Database {database_name} does not exist"
    with open(file_name, 'r+') as dbFile:
        data = json.load(dbFile)
        if tableName in data:
            return f"Table {tableName} already exist"
        data[table_name] = []
        dbFile.seek(0)
        json.dump(data, dbFile, indent=4)
    return f"Table {tableName} created"

def listAllTables(database_name):
    file_name = f"{database_name}.json"
    if not os.path.exists(file_name):
        return f"Database {database_name} does not exist"
    with open(file_name, 'r+') as dbFile:
        data = json.load(dbFile)
    return list(data.keys()) if data else "No table found."

def insertEntry(database_name, tableName, entry):
    file_name = f"{database_name}.json"
    if not os.path.exists(file_name):
        return f"Database {database_name} does not exist"
    with open(file_name, 'r+') as dbFile:
        data = json.load(dbFile)
        if tableName not in data:
            return f"{tableName} does not exist"
        primaryKey = list(data.keys())[0]
        if any(row.get(primaryKey) == entry[primaryKey] for row in data[tableName]):
            return f"Primary Key {primaryKey} must be unique"
        data[tableName].append(entry)
        dbFile.seek(0)
        json.dump(data, dbFile, indent=4)
    return f"Entry added to {tableName}"

def readTable(database_name, tableName):
    file_name = f"{database_name}.json"
    if not os.path.exists(file_name):
        return f"Database {database_name} does not exist"
    with open(file_name, 'r') as dbFile:
        data = json.load(dbFile)
        if tableName not in data:
            return f"Table {tableName} does not exist"
    return data[tableName]

def updateTableEntry(database_name, tableName, primaryKey, updates):
    file_name = f"{database_name}.json"
    if not os.path.exists(file_name):
        return f"Database {database_name} does not exist"
    with open(file_name, 'r') as dbFile:
        data = json.load(dbFile)
        if tableName not in data:
            return f"Table {tableName} does not exist"
        for row in data[tableName]:
            if row.get(primaryKey):
                row.update(updates)
                dbFile.seek(0)
                json.dump(data, dbFile, indent=4)
                return f"Entry with{primaryKey} updated"
        return f"No entry with {primaryKey} found"

def deleteEntry(database_name, tableName, primaryKey):
    file_name = f"{database_name}.json"
    if not os.path.exists(file_name):
        return f"Database {database_name} does not exist"
    with open(file_name, 'r') as dbFile:
        data = json.load(dbFile)
        if tableName not in data:
            return f"Table {tableName} does not exist"
        data[tableName] = [row for row in data[tableName] if row.get(primaryKey) != primaryKey]
        dbFile.seek(0)
        json.dump(data, dbFile, indent = 4)
    return f"Entry with {primaryKey} deleted"

def listAllEnteries(database_name, tableName):
    file_name = f"{database_name}.json"
    if not os.path.exists(file_name):
        return f"Database {database_name} does not exist"
    with open(file_name, 'r') as dbFile:
        data = json.load(dbFile)
        if tableName not in data:
            return f"Table {tableName} does not exist"
    return data[tableName] if data[tableName] else f"No entries in table {tableName}"