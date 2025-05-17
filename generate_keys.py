import pickle
from pathlib import Path

import streamlit_authenticator as stauth

names = ["Johannes"]
usernames = ["jo"]
passwords = ["XXX"]

# Updating the credentials structure to match the expected format
credentials = {
    'usernames': {
        usernames[0]: {
            'name': names[0],
            'password': passwords[0]
        }
    }
}

# Hashing the passwords using the correct structure
hashed_credentials = stauth.Hasher.hash_passwords(credentials)

# Saving the hashed credentials to a file
file_path = Path(__file__).parent / "hashed_pw.pkl"
with file_path.open("wb") as file:
    pickle.dump(hashed_credentials, file)