class InMemoryDB:
    def __init__(self):
        self.data = {}  # Main database storage
        self.transaction = None  # Tracks current transaction changes

    def begin_transaction(self):
        if self.transaction is not None:
            raise Exception("Transaction already in progress.")
        self.transaction = {}

    def put(self, key, value):
        if self.transaction is None:
            raise Exception("No active transaction. Use begin_transaction() first.")
        self.transaction[key] = value

    def get(self, key):
        # Return value from the transaction if it exists and the transaction is active, otherwise from main data
        if self.transaction and key in self.transaction:
            return self.transaction[key]
        return self.data.get(key, None)

    def commit(self):
        if self.transaction is None:
            raise Exception("No active transaction to commit.")
        self.data.update(self.transaction)
        self.transaction = None

    def rollback(self):
        if self.transaction is None:
            raise Exception("No active transaction to rollback.")
        self.transaction = None

# Example usage
db = InMemoryDB()

# Should return None as key 'A' does not exist
print(db.get("A"))

# Starts a new transaction
db.begin_transaction()
db.put("A", 5)  # Temporarily sets 'A' to 5

# Should still return None as changes are not committed
print(db.get("A"))

db.put("A", 6)  # Updates 'A' within the transaction
db.commit()  # Commits changes

# Now 'A' should return 6
print(db.get("A"))

# Starts another transaction and rolls back
db.begin_transaction()
db.put("B", 10)
db.rollback()  # Reverts changes

# 'B' should return None
print(db.get("B"))

# Throws an error, because there is no open transaction
db.commit()

# Throws an error because there is no ongoing transaction
db.rollback()

# Should return None because B does not exist in the database
print(db.get("B"))

# Starts a new transaction
db.begin_transaction()

# Set key B’s value to 10 within the transaction
db.put("B", 10)

# Rollback the transaction - revert any changes made to B
db.rollback()

# Should return None because changes to B were rolled back
print(db.get("B"))