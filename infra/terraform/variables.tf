variable "project_id" {
  type        = string
  description = "GCP project id"
}

variable "region" {
  type        = string
  description = "GCP region"
  default     = "us-east1"
}

variable "service_name" {
  type        = string
  default     = "mini-ecom-api"
}

variable "artifact_repo" {
  type        = string
  default     = "mini-ecom-repo"
}

variable "admin_password_secret_id" {
  type        = string
  default     = "admin-password"
}

variable "stripe_secret_key_secret_id" {
  type        = string
  default     = "stripe-secret-key"
}
