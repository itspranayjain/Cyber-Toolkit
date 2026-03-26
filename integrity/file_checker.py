import hashlib

def get_hash(file_path):
    h = hashlib.sha256()

    try:
        with open(file_path, "rb") as f:
            while chunk := f.read(4096):
                h.update(chunk)
        return h.hexdigest()
    except:
        return None


def check_file(file_path, old_hash):
    new_hash = get_hash(file_path)

    if new_hash is None:
        print("File not found ❌")
        return

    if new_hash == old_hash:
        print("File is SAFE ✅")
    else:
        print("File has been MODIFIED ⚠️")
