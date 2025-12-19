**Secure Mini E-Commerce Application (DevSecOps automation on GCP)**
CloudRun URL(public): https://mini-ecom-api-3aqghzu3iq-ue.a.run.app/   -- /health -- /docs -- /products

---------------------------------------------------------------------------------------------------------

This project is a secure, cloud-native mini e-commerce web application built as part of a DevSecOps assessment.
It demonstrates full-stack development, containerization, CI/CD automation, cloud security best practices, and infrastructure as code on Google Cloud Platform (GCP).

**The application includes:**
A static frontend website
A FastAPI backend API
Firestore database
Stripe (test mode) payment integration
Secure admin access
Automated CI/CD deployment to Cloud Run

**Application Features**
**Frontend (5 Pages)**
1. Home Page
  -Banner and navigation
  -Featured products
2. Products Page
  -Product listing with images and prices
  -Add-to-cart functionality
3. Product Details Page
  -Individual product view
4. Cart & Checkout Page
  -Cart summary
  -Stripe test checkout
5. Admin Orders Page
   -Password-protected
  -Displays all customer orders

**Backend API**
-Built using FastAPI (Python)
-RESTful endpoints:
  /health
  /products/
  /orders/
  /checkout/
-Firestore used as the primary database
-Admin authentication using header-based password validation
-Stripe Sandbox checkout integration

**FrontEnd**
-Frontend assets are served from the backend container
-Backend API runs as a Cloud Run service
-No credentials are hardcoded
-All secrets retrieved securely at runtime

**Tech Stack used: **
Frontend	        HTML, CSS, JavaScript
Backend	          Python, FastAPI
Database	        Firestore
Payments	        Stripe (Test Mode)
Containerization	Docker
Hosting	          Cloud Run
CI/CD	            GitHub Actions
IaC	              Terraform
Security	        IAM, Secret Manager, HTTPS



----------------------------------------------------------------------------

**Author**

Ashok
DevOps / DevSecOps / Cloud automation
