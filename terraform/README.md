# Terraform — UR2 BigQuery sandboxes

Provisions, per student group, in the `ai-technologies-ur2` GCP project:

- a BigQuery dataset `dataset_group_<idx>`
- a service account `ur2-group-<idx>` that:
  - can execute BigQuery jobs (`roles/bigquery.jobUser`, project-level — BigQuery
    job execution has no dataset-scoped equivalent)
  - owns (and can view) only its own group's dataset (`roles/bigquery.dataOwner`)
- IAM bindings for the `ur2-students-group-<idx>@googlegroups.com` Google Group:
  - can execute BigQuery jobs (`roles/bigquery.jobUser`)
  - can view project/resource metadata (`roles/browser`)
  - can view tables and metadata in only its own group's dataset
    (`roles/bigquery.dataViewer`) — no ownership

## Group creation is manual, not managed by this Terraform

`ur2-students-group-<idx>` groups are plain **consumer Google Groups**
(created at [groups.google.com](https://groups.google.com)), not Cloud
Identity/Workspace groups. Terraform's `google_cloud_identity_group` resource
only manages Cloud Identity/Workspace groups, which requires a Cloud Identity
org — the `ai-technologies-ur2` project's account has none
(`gcloud organizations list` is empty). There is no public API to create
consumer Google Groups from Terraform, so **each group must be created
manually** in the Google Groups UI before running `terraform apply`; this
config only assumes the group already exists and grants it IAM roles.

## Usage

```bash
cd terraform
gcloud auth application-default login   # ADC used by the google provider
terraform init
cp terraform.tfvars.example terraform.tfvars   # edit group_count as needed
terraform plan
terraform apply
```

All variables can also be set via `TF_VAR_<name>` environment variables
instead of `terraform.tfvars`, e.g. `TF_VAR_group_count=5`.
