# memory-database
In-Memory Key-Value Database with Transaction Support

**Overview**

This project implements an in-memory key-value database with transaction support. The database allows you to perform the following operations:

      1. Start a transaction.

      2. Add or update key-value pairs within a transaction.

      3. Retrieve values associated with keys.

      4. Commit changes made during a transaction.

      5. Rollback changes to revert to the previous state.

This functionality ensures "all-or-nothing" updates, which is crucial for scenarios like financial transactions.

**Features**

      - Transactions ensure temporary changes are not visible until committed.

      - Rollback allows reverting changes during a transaction.

      - Keys are strings, and values are integers.

      - Enforces single active transaction at a time.

**Setup**

_**Requirements**_

    - Python 3.7 or higher

_**Running the Code**_

Clone the repository to your local machine: git clone [repository-url]

Navigate to the project directory: cd [project-directory]

Run the Python script: python in_memory_db_transactions.py

**Example Usage**

The code includes an example demonstrating the functionality:

# Create the database instance
db = InMemoryDB()

# Start a transaction
db.begin_transaction()
db.put("A", 5)  # Temporarily sets 'A' to 5
db.commit()      # Commits changes

# Retrieve the value of 'A'
print(db.get("A"))  # Output: 5

# Start another transaction and rollback changes
db.begin_transaction()
db.put("B", 10)
db.rollback()    # Reverts changes

# Verify 'B' does not exist
print(db.get("B"))  # Output: None

**Suggested Improvements for the Assignment**

  - Clarify Instructions: Clearly specify behavior for edge cases (e.g., nested transactions, duplicate keys).

  - Add More Methods: Include support for operations like delete(key) or get_all() for retrieving all keys.

  - Grading Enhancement: Include automated tests for verifying functionality, reducing manual grading effort and allowing the student's to understand their grade quicker. 

  - Real-World Application: Add a case study (e.g., a mock payment system) to contextualize usage.
