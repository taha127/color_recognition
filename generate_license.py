import hashlib
from pathlib import Path

license_key = input("Enter License Key: ").strip()
license_hash = hashlib.sha256(license_key.encode()).hexdigest()
Path("generated").mkdir(exist_ok=True)

with open("generated/generated_license.py", "w", encoding="utf-8") as f:

    f.write(f'VALID_LICENSE_HASH = "{license_hash}"\n')

print("Done.")
