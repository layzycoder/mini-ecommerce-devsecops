from google.cloud import firestore
import os
import google.auth


def get_project_id() -> str:
    # Prefer env vars used by GCP SDKs
    pid = os.getenv("GOOGLE_CLOUD_PROJECT") or os.getenv("GCP_PROJECT_ID")
    if pid:
        return pid

    _, pid = google.auth.default()
    if not pid:
        raise RuntimeError("Project was not passed and could not be determined from the environment.")
    return pid

def get_firestore_client():
    project_id = get_project_id()
    return firestore.Client(project=project_id)

# _db = None

# def get_firestore_client():
#     global _db
#     if _db is None:
#         _db = firestore.Client()
#     return _db
