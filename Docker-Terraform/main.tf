terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "~> 6.18"
    }
  }
     required_version = ">= 1.0"
}

provider "google" {
  credentials = file("key.json")
  project     = var.project
  region      = var.region
}


resource "google_storage_bucket" "bucket-Name" {
  name          = var.gcs_bucket_name
  location      = var.location
  force_destroy = true

  lifecycle_rule {
    condition {
      age = 3
    }
    action {
      type = "Delete"
    }
  }

  lifecycle_rule {
    condition {
      age = 1
    }
    action {
      type = "AbortIncompleteMultipartUpload"
    }
  }
}


resource "google_bigquery_dataset" "my_dataset" {
  dataset_id = var.bq_dataset_name
  location   = var.location
}