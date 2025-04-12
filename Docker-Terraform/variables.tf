variable "credentials" {
  description = "My credentials"
  default     = "/key.json"

}

variable "project" {
  description = "Project"
  default     = "project_id"

}

variable "region" {
  description = "Region"
  default     = "europe-west1"

}

variable "location" {
  description = "Project Location"
  default     = "EU"

}

variable "bq_dataset_name" {
  description = "My BigQuery Dataset Name"
  default     = "dataset"

}

variable "gcs_bucket_name" {
  description = "My Storage Bucket Name"
  default     = "bucket-Name"

}

variable "gcs_storage_class" {
  description = "Bucket Storage Class"
  default     = "STANDARD"

}