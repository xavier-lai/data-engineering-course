# One BigQuery dataset per group.
resource "google_bigquery_dataset" "group" {
  for_each = toset(local.group_indices)

  project    = var.project_id
  dataset_id = "dataset_group_${each.value}"
  location   = var.dataset_location

  depends_on = [google_project_service.apis]
}

# Service account: owns (and therefore can view) only its own group's dataset.
resource "google_bigquery_dataset_iam_member" "sa_owner" {
  for_each = google_bigquery_dataset.group

  project    = var.project_id
  dataset_id = each.value.dataset_id
  role       = "roles/bigquery.dataOwner"
  member     = "serviceAccount:${google_service_account.group[each.key].email}"
}

# Students group: can view tables/metadata in their own group's dataset only (no ownership).
resource "google_bigquery_dataset_iam_member" "group_viewer" {
  for_each = google_bigquery_dataset.group

  project    = var.project_id
  dataset_id = each.value.dataset_id
  role       = "roles/bigquery.dataViewer"
  member     = "group:${local.group_emails[each.key]}"
}
