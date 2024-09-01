provider "aws" {
  region = "us-east-2"  # Especifica la región donde deseas crear el topic SNS
}

resource "aws_sns_topic" "data_processing_topic" {
  name = "data-processing-topic"
  # Puedes agregar más configuraciones según sea necesario
}
