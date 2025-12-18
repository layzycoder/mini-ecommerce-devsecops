resource "google_project_service" "services" {
  for_each = toset([
    "run.googleapis.com",
    "artifactregistry.googleapis.com",
    "secretmanager.googleapis.com",
    "firestore.googleapis.com",
    "cloudbuild.googleapis.com",
    "iam.googleapis.com",
    "logging.googleapis.com"
  ])
  service            = each.value
  disable_on_destroy = false
}

resource "google_artifact_registry_repository" "repo" {
  location      = var.region
  repository_id = var.artifact_repo
  format        = "DOCKER"
  depends_on    = [google_project_service.services]
}

resource "google_service_account" "run_sa" {
  account_id   = "${var.service_name}-sa"
  display_name = "Cloud Run SA for ${var.service_name}"
  depends_on   = [google_project_service.services]
}

resource "google_secret_manager_secret" "admin_password" {
  secret_id = var.admin_password_secret_id
  depends_on = [google_project_service.services]

  replication { 
    auto {} 
    }
}

resource "google_secret_manager_secret" "stripe_secret_key" {
  secret_id = var.stripe_secret_key_secret_id
  depends_on = [google_project_service.services]

  replication { 
    auto {} 
    }
}

resource "google_secret_manager_secret_iam_member" "admin_secret_access" {
  secret_id = google_secret_manager_secret.admin_password.id
  role      = "roles/secretmanager.secretAccessor"
  member    = "serviceAccount:${google_service_account.run_sa.email}"
}

resource "google_secret_manager_secret_iam_member" "stripe_secret_access" {
  secret_id = google_secret_manager_secret.stripe_secret_key.id
  role      = "roles/secretmanager.secretAccessor"
  member    = "serviceAccount:${google_service_account.run_sa.email}"
}

resource "google_project_iam_member" "firestore_user" {
  project = var.project_id
  role    = "roles/datastore.user"
  member  = "serviceAccount:${google_service_account.run_sa.email}"
}

# resource "google_cloud_run_v2_service" "api" {
#   name     = var.service_name
#   location = var.region
#   depends_on = [google_project_service.services]

#   template {
#     service_account = google_service_account.run_sa.email

#     containers {
#       image = "us-docker.pkg.dev/${var.project_id}/${var.artifact_repo}/${var.service_name}:latest"

#       ports { container_port = 8080 }

#       env {
#         name  = "GOOGLE_CLOUD_PROJECT"
#         value = var.project_id
#       }
#       env {
#         name  = "GCP_PROJECT_ID"
#         value = var.project_id
#       }
#     }
#   }
# }

# resource "google_cloud_run_v2_service_iam_member" "public_invoker" {
#   name     = google_cloud_run_v2_service.api.name
#   location = google_cloud_run_v2_service.api.location
#   role     = "roles/run.invoker"
#   member   = "allUsers"
# }
