locals {
  group_indices = [for i in range(var.group_count) : tostring(i + 1)]

  group_emails = {
    for idx in local.group_indices :
    idx => "ur2-students-group-${idx}@${var.group_domain}"
  }
}

resource "google_project_service" "apis" {
  for_each = toset([
    "bigquery.googleapis.com",
    "iam.googleapis.com",
    "cloudresourcemanager.googleapis.com",
  ])

  project            = var.project_id
  service            = each.value
  disable_on_destroy = false
}
