# One service account per group, used by the group to own/run jobs against its own dataset.
resource "google_service_account" "group" {
  for_each = toset(local.group_indices)

  project      = var.project_id
  account_id   = "ur2-group-${each.value}"
  display_name = "UR2 group ${each.value} service account"

  depends_on = [google_project_service.apis]
}

# Service account: can execute BigQuery jobs (project-level requirement).
resource "google_project_iam_member" "sa_job_user" {
  for_each = google_service_account.group

  project = var.project_id
  role    = "roles/bigquery.jobUser"
  member  = "serviceAccount:${each.value.email}"
}

# Students group: can execute BigQuery jobs (project-level requirement).
resource "google_project_iam_member" "group_job_user" {
  for_each = local.group_emails

  project = var.project_id
  role    = "roles/bigquery.jobUser"
  member  = "group:${each.value}"
}

# Students group: can browse project/resource metadata.
resource "google_project_iam_member" "group_browser" {
  for_each = local.group_emails

  project = var.project_id
  role    = "roles/browser"
  member  = "group:${each.value}"
}
