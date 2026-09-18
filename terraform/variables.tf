variable "project_id" {
  description = "GCP project to provision resources in. Override with TF_VAR_project_id."
  type        = string
  default     = "ai-technologies-ur2"
}

variable "dataset_location" {
  description = "Location for the BigQuery datasets."
  type        = string
  default     = "europe-west1"
}

variable "group_count" {
  description = "Number of student groups to provision (dataset + service account + IAM per group). Override with TF_VAR_group_count."
  type        = number
  default     = 6

  validation {
    condition     = var.group_count > 0
    error_message = "group_count must be greater than 0."
  }
}

variable "group_domain" {
  description = <<-EOT
    Domain used to build each group's email: ur2-students-group-<idx>@<group_domain>.
    Defaults to googlegroups.com because these are plain consumer Google Groups
    (created manually at groups.google.com), not Cloud Identity/Workspace groups.
  EOT
  type        = string
  default     = "googlegroups.com"
}
