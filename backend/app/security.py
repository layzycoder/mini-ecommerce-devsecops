from google.cloud import secretmanager
import google.auth


def get_project_id() -> str:
    _, project_id = google.auth.default()

    if not project_id:
        raise RuntimeError("GCP project ID not available via default credentials")

    return project_id


def get_admin_password() -> str:
    project_id = get_project_id()

    client = secretmanager.SecretManagerServiceClient()
    name = f"projects/{project_id}/secrets/admin-password/versions/latest"

    response = client.access_secret_version(name=name)
    return response.payload.data.decode("UTF-8").strip()

def get_stripe_secret_key() -> str:
    project_id = get_project_id()
    client = secretmanager.SecretManagerServiceClient()
    name = f"projects/{project_id}/secrets/stripe-secret-key/versions/latest"

    response = client.access_secret_version(name=name)
    return response.payload.data.decode("UTF-8").strip()
