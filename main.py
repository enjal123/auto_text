import firebase_admin
from firebase_admin import credentials, firestore

print("Starting test...")

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

print("Firebase initialized")

db = firestore.client()

print("Fetching users...")

docs = list(db.collection("users").stream())

print(f"Users count: {len(docs)}")
