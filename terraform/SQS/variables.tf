variable "region" {
  default     = "us-east-2"
}

variable "queue_name" {
  description = "SQS data-processing-queue"
  default     = "data-processing-queue"
}

variable "visibility_timeout_seconds" {
  description = "The visibility timeout for the SQS queue"
  default     = 30
}

variable "message_retention_seconds" {
  description = "The number of seconds a message can be retained in the queue"
  default     = 86400
}

variable "delay_seconds" {
  description = "The delay in seconds for delivery of messages"
  default     = 0
}

variable "max_message_size" {
  description = "The maximum message size in bytes"
  default     = 262144
}

variable "receive_wait_time_seconds" {
  description = "The wait time for receiving messages"
  default     = 0
}
