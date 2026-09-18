terraform {
  backend "gcs" {
    bucket = "ai-technologies-ur2-terraform"
    prefix = "terraform/state"
  }
}
