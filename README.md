# 🏦 Bank Account Management System

> **A small bank behind a command prompt:** welcome customers, open accounts, move money, and keep a record of every deposit and withdrawal. 💳

This beginner-friendly Python project simulates a simple bank account management system in the terminal. It gives you a menu for creating customers and accounts, depositing and withdrawing money, checking balances, and reviewing transactions.

The code is also a hands-on tour of object-oriented programming. Customers, bank accounts, and transactions are represented as separate classes, while a management class coordinates the workflows and saves records to CSV files.

> [!NOTE]
> This is an educational programming example. It stores account records in ordinary CSV files and is not designed to handle real money, real banking credentials, or sensitive customer data.

---

## 🗺️ Contents

- [✨ Features](#-features)
- [🧭 A typical session](#-a-typical-session)
- [🏛️ How the program is organized](#️-how-the-program-is-organized)
- [🧰 Requirements](#-requirements)
- [🚀 Getting started](#-getting-started)
- [🖥️ Menu guide](#️-menu-guide)
- [💵 How deposits and withdrawals work](#-how-deposits-and-withdrawals-work)
- [🧾 Transaction history](#-transaction-history)
- [📁 Data files](#-data-files)
- [🧠 Programming concepts](#-programming-concepts)
- [⚠️ Current behavior and limitations](#️-current-behavior-and-limitations)
- [🌱 Ideas for future improvements](#-ideas-for-future-improvements)
- [✅ Learning challenges](#-learning-challenges)
- [📜 License](#-license)

---

## ✨ Features

- 👤 **Add customers** with a numeric customer ID and name.
- 🏧 **Create accounts** for registered customers.
- 🔐 **Protect account actions with a PIN check.**
- 💰 **Deposit money** into an account.
- 💸 **Withdraw money** when the account has enough funds.
- 📊 **Check an authenticated account's balance.**
- 🧾 **View transaction history** for an account.
- 💾 **Save customers, accounts, and transactions** to separate CSV files.
- 📥 **Load saved records** and continue account and transaction numbering.
- 🧱 **Practice classes, inheritance, abstraction, encapsulation, and object collaboration.**

---

## 🧭 A typical session

A natural first run follows this path:

1. 👤 Choose **1** to add a customer.
2. 🏧 Choose **2** to create an account for that customer's ID.
3. 🔐 Choose a four-digit PIN when prompted.
4. 💰 Choose **3** to make a deposit.
5. 💸 Choose **4** to withdraw money, or **5** to check the balance.
6. 🧾 Choose **6** to see that account's transactions.
7. 💾 Choose **7** to save the records before ending the program.

The system stores information in memory during the session. It does not automatically load records when it starts or save them when it exits. Use **8** to load and **7** to save.

---

## 🏛️ How the program is organized

### 🧑 `Person`

`Person` is an abstract base class for shared customer information. It stores a name and declares `display_info()` as an abstract method. Any concrete subclass must implement that method.

### 👤 `Customer`

`Customer` inherits from `Person`. It adds a private customer ID and implements `display_info()`. The ID is exposed through `get_customer_id()`.

### 🏦 `BankAccount`

`BankAccount` stores one account's number, owner customer ID, account type, PIN, and balance. A new account starts with a balance of zero.

It provides methods to:

- Check a PIN.
- Deposit a positive amount.
- Withdraw a positive amount that does not exceed the balance.
- Read account information through getters.
- Set the balance when restoring a saved account.

### 🧾 `Transaction`

`Transaction` represents one deposit or withdrawal. It stores a transaction ID, account number, transaction type, and amount, with getters and a display method.

### 🗂️ `Bank_Management`

The management class keeps three lists: customers, accounts, and transactions. It also creates account and transaction numbers, runs the banking workflows, and reads or writes CSV files.

### 🖥️ Menu loop

The `menu()` method repeatedly displays the available actions and calls the matching method. Choosing **9** exits the loop.

---

## 🧰 Requirements

- 🐍 Python 3
- 📦 No third-party packages

The code uses Python's built-in `abc` and `csv` modules.

---

## 🚀 Getting started

1. Save the code to a file, for example `bank_management.py`.
2. Open a terminal in the folder where you saved it.
3. Run the program:

   ```bash
   python bank_management.py
   ```

   On systems where Python is invoked as `python3`, use:

   ```bash
   python3 bank_management.py
   ```

The program opens the interactive menu. Enter the number beside the action you want, then respond to its prompts.

---

## 🖥️ Menu guide

### 1️⃣ Add Customer

Enter a customer ID and name. The customer ID must be a whole number. The current code does not ask for an address, contact details, or other customer information.

### 2️⃣ Create Account

Enter the ID of an existing customer, an account type, and a four-digit PIN. The program assigns the next account number automatically, starting at **10001**.

The account type is entered as text. Although the prompt suggests **Savings** or **Current**, the program does not restrict the input to those two choices.

### 3️⃣ Deposit Money

Enter an account number and PIN, then enter a deposit amount. Only a positive amount is accepted. A successful deposit increases the balance and creates a transaction record.

### 4️⃣ Withdraw Money

Authenticate with the account number and PIN, then enter a withdrawal amount. The amount must be positive and no greater than the available balance. Successful withdrawals are recorded as transactions.

### 5️⃣ Check Balance

Authenticate with the account number and PIN to display the current balance.

### 6️⃣ Transaction History

Authenticate with the account number and PIN to list the transactions currently recorded for that account. If there are no matching transactions, the program reports that none were found.

### 7️⃣ Save Records

Writes the in-memory records to three files:

- `customers.csv`
- `accounts.csv`
- `transactions.csv`

Each save replaces that file with the current contents of its corresponding list.

### 8️⃣ Load Records

Reads records from the three CSV files and appends them to the current in-memory lists. This is useful when starting a new session, but loading repeatedly in the same session can duplicate records.

### 9️⃣ Exit

Ends the program. The current code does not save automatically when you exit, so save first if you want to keep changes.

---

## 💵 How deposits and withdrawals work

The account class keeps the balance changes together with the validation rules:

- A deposit succeeds only if `amount > 0`.
- A withdrawal succeeds only if `amount > 0` and `amount <= balance`.
- A successful operation returns `True`; an invalid operation returns `False`.
- The management class creates a `Transaction` only after the balance operation succeeds.

For example, if an account has a balance of 500, a withdrawal of 125 succeeds and leaves 375. A withdrawal of 600 fails and does not create a transaction.

Amounts are represented as Python floating-point numbers in this educational implementation.

---

## 🧾 Transaction history

Every successful deposit or withdrawal receives a sequential transaction ID. Transaction records are kept in memory in the `transactions` list and associated with an account number.

When transaction history is requested, the program scans that list and displays only records whose account number matches the authenticated account.

A transaction stores its type and amount. The code does not store a timestamp, resulting balance, branch, or transaction description.

---

## 📁 Data files

The program uses three CSV files in the current working directory.

### `customers.csv`

```csv
Customer_ID,Name
101,Jordan Lee
```

### `accounts.csv`

```csv
Account_Number,Customer_ID,Account_Type,PIN,Balance
10001,101,Savings,1234,500.0
```

### `transactions.csv`

```csv
Transaction_ID,Account_Number,Type,Amount
1,10001,Deposit,500.0
```

The filenames are hard-coded in the save and load methods. The files are written with Python's default text encoding and without an explicit encoding setting.

When records are loaded, the program updates its account and transaction counters so newly created records can continue after the largest saved IDs.

---

## 🧠 Programming concepts

### 🧩 Abstraction

`Person` inherits from `ABC` and marks `display_info()` as abstract. This establishes a common method requirement for concrete person types. `Customer` fulfills that requirement.

### 🧬 Inheritance

`Customer(Person)` inherits the name handling from `Person` and calls `super().__init__(name)` to initialize it.

### 🔐 Encapsulation

Customer IDs, account details, PINs, balances, and transaction details use double-underscore attributes. Getter methods provide controlled access to many of those values.

### 🤝 Objects working together

The management class coordinates customer, account, and transaction objects. A deposit, for example, authenticates an account, asks that account to update its balance, and then creates a transaction object to record the successful operation.

### 📄 CSV persistence

The `csv` module converts in-memory objects into rows and reconstructs objects from saved rows. This lets the small program preserve data between sessions without an external database.

---

## ⚠️ Current behavior and limitations

This README documents the code as supplied:

- 🔐 **PINs are saved in plain text** in `accounts.csv`. The code is for learning only and should not store real credentials.
- 💾 Records are saved only when **Save Records** is selected. Choosing **Exit** does not save automatically.
- 📥 Loading appends to the lists. Loading more than once may create duplicate customers, accounts, and transactions.
- 🧩 The three files are loaded in sequence. If a later file is missing, earlier files may already have been loaded before the error message appears.
- 🆔 Customer IDs are not checked for duplicates.
- 🏧 The code does not prevent multiple accounts of the same type for a customer.
- 📝 Names and account types are not checked for blank values.
- 💵 Floating-point numbers can introduce rounding surprises in monetary calculations. Financial applications generally use decimal arithmetic and explicit currency rules.
- 🧾 Transactions have no timestamps and cannot be edited or reversed through the menu.
- 🔢 Account and transaction counters are kept in memory and rebuilt from saved rows when files are loaded.
- 🛠️ Some methods, such as `display_info()`, exist on the data classes but are not used by the menu.

These constraints make the project approachable, while also providing useful topics for the next iteration.

---

## 🌱 Ideas for future improvements

- 🔒 Hash PINs and never save them in readable form.
- 💰 Use Python's `decimal.Decimal` for currency and define a rounding policy.
- 🧪 Add tests for authentication, deposits, withdrawals, and persistence.
- 🧹 Prevent duplicate customer IDs and validate names and account types.
- 📥 Make loading safe to repeat by replacing current lists or checking for existing records.
- 🧾 Add timestamps and a balance-after-transaction field to transaction history.
- 🛟 Validate the CSV files completely before changing in-memory state.
- 📂 Add clear file error handling to the save operation.
- 🧑‍💻 Separate terminal input/output from banking rules.
- 🏷️ Add account statements, transaction filters, and customer lookup.
- 🗃️ Move from CSV files to a database if the application grows.
- 🔐 Add account lockout or rate limits after repeated incorrect PIN attempts.

---

## ✅ Learning challenges

Try answering these questions or implementing the exercises:

1. ❓ Why can `Person` not be instantiated directly?
2. 🧬 What does `super().__init__(name)` do in the customer constructor?
3. 💳 Why does `deposit()` return a Boolean value?
4. 🧾 At what point is a transaction created during a deposit?
5. 🔁 What happens if **Load Records** is selected twice?
6. 🔐 How could you avoid storing a PIN as plain text?
7. 💵 Why are floating-point values a poor fit for exact currency calculations?
8. 🧪 How would you test that a failed withdrawal leaves both the balance and transaction list unchanged?
9. 🧱 How might you separate the menu from the banking operations?

A strong first exercise is to test the account rules: a valid deposit increases the balance, an invalid deposit does not, a withdrawal cannot exceed the balance, and only successful operations appear in transaction history. 🧪

---

## 📜 License

No license was included with the supplied code. Add a license file if you plan to share or redistribute the project.


