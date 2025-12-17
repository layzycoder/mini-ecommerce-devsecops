from google.cloud import firestore
import os

_db = None

def get_firestore_client():
    global _db
    if _db is None:
        _db = firestore.Client()
    return _db
