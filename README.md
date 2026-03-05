# 🔐 File Integrity Checker

A simple Python project used to **verify whether a file has been modified or not** by comparing cryptographic hash values.

---

## 📌 Project Purpose

The purpose of this project is to demonstrate how **file integrity verification** works using hashing.  
When a file is sent from one place to another, its **hash value** can be generated and later compared with another hash of the received file.

If both hashes are the same → the file is **safe and unchanged**.  
If the hashes are different → the file **has been modified or corrupted**.

---

## ⚙️ How It Works

1️⃣ A hash value of a file is generated using a hashing algorithm.  
2️⃣ The hash value acts like a **digital fingerprint** of the file.  
3️⃣ When the file is received, another hash is generated.  
4️⃣ Both hashes are compared.

- ✅ Same hash → File integrity is preserved  
- ❌ Different hash → File was modified

---

## 🚀 How to Use

1. Generate the **hash value** of the original file.
2. Save or send this hash together with the file.
3. After receiving the file, generate the hash again.
4. Compare both hash values.
5. The program will tell you whether the file is **safe or modified**.

---

## 🛠 Technologies Used

- 🐍 Python  
- 🔐 SHA-256 Hashing  
- 🎨 Terminal text styling

---

## 🎯 Learning Goal

This project helps understand:

- Cryptographic hashing
- File integrity verification
- Basic cybersecurity concepts

---

## Team members:

**Bekmurod G'ofurov**<br>
**Shoxruh Latipov**<br>
**Shirinhon Bahodirova**<br>
**Oyazimhon Abdumalikova**
