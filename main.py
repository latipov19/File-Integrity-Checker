import hashlib

def get_file_hash(filename):
    # Faylni bayt ko'rinishida o'qiymiz
    with open(filename, "rb") as f:
        bytes = f.read() 
        # SHA-256 algoritmi orqali hash hisoblaymiz
        readable_hash = hashlib.sha256(bytes).hexdigest()
        return readable_hash

# Ishlatib ko'ramiz:
file_name = "test.txt" # Kompyuteringizdagi fayl nomi
print(f"Fayl hashi: {get_file_hash(file_name)}")
