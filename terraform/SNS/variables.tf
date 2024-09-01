variable "region" {
  default     = "us-east-2"
}

variable "topic_name" {
  description = "The name of the SNS topic"
  default     = "data-processing-topic"
}
