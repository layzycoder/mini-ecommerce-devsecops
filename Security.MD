
This document describes the security architecture, controls, and best practices implemented in this Mini E-Commerce application which is deployed on Google Cloud Platform (GCP).
The goal is to ensure confidentiality, integrity, and availability while following DevSecOps principles and practices.

-- Implemented Identity & Access Management (IAM)
-- CloudRun uses the dedicated service account
-- SecretManager access Roles implemented 
-- GitHub authenticates to GCP using workload Identity federation 
-- SecretManagement used for admin passwords, Strip Sandbox secret key
-- Network level HTTPS enforcement implemented
-- Admin to access the Admin Order section using the Admin password
-- Docker image scanning using Trivy
-- 
