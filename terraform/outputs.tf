output "dataset_ids" {
  description = "BigQuery dataset id per group index."
  value       = { for idx, ds in google_bigquery_dataset.group : idx => ds.dataset_id }
}

output "service_account_emails" {
  description = "Service account email per group index."
  value       = { for idx, sa in google_service_account.group : idx => sa.email }
}

output "group_emails" {
  description = "Students group email per group index (expected to already exist)."
  value       = local.group_emails
}
