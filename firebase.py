import firebase_admin
from firebase_admin import credentials, auth, firestore
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
import requests
from firebase_init import initialize_firebase

import json
import os
presigned_url = "https://health-file.s3.us-east-2.amazonaws.com/final.json?response-content-disposition=inline&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLWVhc3QtMiJIMEYCIQCzz8GeF1KJxdNl9iYl16nTTMZ9nRASafDalpRIf1lwFwIhAJZl6y2Dt1uICIThv5k8mU90CKo6UW0k0r4q5u6sC%2FvKKtQDCMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNTQ1MDA5ODU4Nzk3IgzPicX5zZX6CXmL67oqqAOeJIpPLat9ZF5jG8d35F3KUymcFEZ3hcl1XBsRKxRXYDY2yhTYyY3hSvdpoc3sxoSYsJqhlkk9xF5RyIZvcvr%2FLiD59mpoZibUU%2Fe5K2PBQ6kT2Br%2BatHtxZitKRM97%2BVC3FgbOno7ENF8xFSj4GUZBqPQruxrTqMQUQhXXUDOyX%2FryL%2FNy5r3kAB3c%2Fh9%2FTjCtV46sdaXOOP8Z1lLU5I6blHESDk4RGRaDQwVSuIZY7NX%2Bh9E6W2h9t1u6fww2BsGbbDvKV7YnkijfAt1qzHWxG5zWkZTXztbUP7dlqT0gVPU4Y66z2tAiwSNHyxS9RS2NFBxKuwpSlGX0yMaNCV7QeHBcE7bfpITczTh%2BtnqbNimnXi7v%2BeGR2DZZA2NsnAHly5rKALQlgynH9A9nKQcwNWpHoAVsssMeU9PaE3Nbz1t53BI3IXM7ddh31WiKLMQ5BiZeFbxIAC9LwJFuvs67%2Fo1i8mJnKDloyIKA%2BpBJY2eBhyERrv%2FM1hQfX7Ov4ZFnNwiIjSt%2FLXsAkqK7WMG74a6yWgqamcxuj6uOLiY3sOavd4hVenRMKHluLoGOuMC%2F7k6dCN3iAgfXz5oUGZ3roRohzq5C90ty9p0nlM4EUiEOdVfKAY3ir2ybLJG%2BU%2FAJbMgweJPtwKydGWrj%2B4%2BH25SeQ1SyM%2BVMz3CJ8yDBYc0jbk1S0s17Cl6pOn2enaBN5J8131ozlBRIHHj09UWtKEpjO%2FDttbobJ1OXAPcZonXAZqOoyuLttIv4rBjOlschSDNbCcivYhiBptlpAayZnmZFHScMsu6lL291ucrOteD%2BqKbAgIJvWsY5VhFlfPVMBi%2BNXIMrQSCGUr63DUPuu3dPlbrHPgP1wOofzwaKTtFPyiCtCzi6OGmhLcZBR1dH1S%2B0hm4ZXzU%2FUMh94EYDBZV74uEqXExv9HCkvtZsNkAZXBa6Ga1OxN7H4KZSMtil%2BLeSk4hK9MwNp5ioC0TWZwu%2FVGouZxXWMcCZRA4QdWLBYbwcxAqV21DKrlAnywIM41Z9KNQCg%2BEjyabbBcX1p6WTA%3D%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=ASIAX5ZI6PDWZTRWZS2U%2F20241202%2Fus-east-2%2Fs3%2Faws4_request&X-Amz-Date=20241202T222058Z&X-Amz-Expires=43200&X-Amz-SignedHeaders=host&X-Amz-Signature=c9218e107c2f9ee1f70473b3d7837bf1d68f2d005b8a5b4349f4ec396e24837e"

initialize_firebase()
db = firestore.client()


# # Dynamically construct the file path to the JSON file
# current_dir = os.path.dirname(os.path.abspath(__file__))  # Get the directory of the current script
# file_path = os.path.join(current_dir, "ht04.json")  # Path to 'ht.json'

# # Verify the file exists before initializing Firebase
# if not os.path.exists(file_path):
#     raise FileNotFoundError(f"The file 'ht.json' was not found at {file_path}")
# if not firebase_admin._apps:
#     # Initialize Firebase Admin SDK
#     cred = credentials.Certificate(file_path)  # Ensure the correct path to your credentials
#     firebase_admin.initialize_app(cred)

# # Get Firestore database reference
# db = firestore.client()


def signup_user(email: str, password: str, username: str, age: int, gender: str, blood_type: str):
    """
    Create a user in Firebase Authentication and store additional details in Firestore.
    """
    try:
        # Create a new user in Firebase Authentication
        user = auth.create_user(email=email, password=password)
        print("User created in Firebase Authentication:", user.uid)
        
        # Store additional user data in Firestore
        user_data = {
            'username': username,
            'email': email,
            'password': generate_password_hash(password),  # Store hashed password
            'age': age,
            'gender': gender,
            'blood_type': blood_type,
            'created_at': datetime.now()  # Optional: store account creation timestamp
        }
        
        # Save user data in Firestore
        db.collection('users').document(user.uid).set(user_data)
        print("User data saved in Firestore.")

        return True, "User registered successfully!", user.uid
    except Exception as e:
        print(f"Error during signup_user: {e}")
        return False, str(e), None

def login_user(email: str, password: str):
    """
    Authenticate user using Firebase Authentication and verify password against Firestore.
    """
    try:
        user = auth.get_user_by_email(email)
        
        # Fetch user details from Firestore to verify password
        user_ref = db.collection('users').document(user.uid)
        user_doc = user_ref.get()
        
        if user_doc.exists:
            user_data = user_doc.to_dict()
            # Verify the hashed password
            if check_password_hash(user_data['password'], password):
                return True, f"Welcome {user_data['username']}!", user.uid
            else:
                return False, "Incorrect password.", None
        else:
            return False, "User details not found in Firestore.", None
    except Exception as e:
        return False, "Authentication failed. Please check your credentials.", None



def update_daily_data(uid: str, health_data: dict):
    """
    Update the `daily-data` sub-field with the provided health data for today's date.
    """
    current_date = datetime.now().strftime("%Y-%m-%d")  # Format: YYYY-MM-DD

    # Reference to the user's document in Firestore
    user_ref = db.collection('users').document(uid)

    try:
        # Update the specific date in the `daily-data` field with new health data
        user_ref.update({
            f'daily_data.{current_date}': health_data
        })
        print(f"Updated daily data for {current_date} under user {uid}.")
        return True
    except Exception as e:
        print(f"Failed to update daily data: {e}")
        return False

def check_existing_data(uid: str) -> bool:
    """
    Check if health data for the current date already exists.
    """
    current_date = datetime.now().strftime("%Y-%m-%d")
    user_ref = db.collection('users').document(uid)

    try:
        user_doc = user_ref.get()
        if user_doc.exists:
            user_data = user_doc.to_dict()
            return current_date in user_data.get('daily_data', {})
        return False
    except Exception as e:
        print(f"Error checking existing data: {e}")
        return False
    

def get_first_user_uid():
    """Fetch the UID of the first user in Firestore."""
    try:
        users = db.collection('users').limit(1).get()
        if users:
            return users[0].id  # Get the document ID of the first user
        else:
            print("No users found in Firestore.")
            return None
    except Exception as e:
        print(f"Error fetching user UID: {e}")
        return None
