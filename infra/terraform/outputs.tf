output "artifact_registry_repo" {
  value = google_artifact_registry_repository.repo.name
}

# output "cloud_run_service_name" {
#   value = google_cloud_run_v2_service.api.name
# }

# output "cloud_run_url" {
#   value = google_cloud_run_v2_service.api.uri
# }

output "cloud_run_service_account" {
  value = google_service_account.run_sa.email
}
