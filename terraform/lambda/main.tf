provider "aws" {
  region = "us-east-2"
}

resource "aws_lambda_function" "latam_lambda_function" {
  function_name = "latam-lambda-function"
  package_type  = "Image"
  image_uri     = "111111111111.dkr.ecr.us-east-2.amazonaws.com/lambda_ecr_repo:latest"
  role          = aws_iam_role.lambda_exec_role.arn

  environment {
    variables = {
      DATABASE_URL = "postgresql://latam_user:latam_password@localhost/latambd"
    }
  }
}

resource "aws_iam_role" "lambda_exec_role" {
  name = "lambda_exec_role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17",
    Statement = [
      {
        Action    = "sts:AssumeRole",
        Effect    = "Allow",
        Principal = {
          Service = "lambda.amazonaws.com"
        }
      }
    ]
  })
}

resource "aws_iam_role_policy_attachment" "lambda_policy_attach" {
  role       = aws_iam_role.lambda_exec_role.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
}

resource "aws_iam_role_policy_attachment" "sqs_policy_attach" {
  role       = aws_iam_role.lambda_exec_role.name
  policy_arn = "arn:aws:iam::aws:policy/AmazonSQSFullAccess"
}

resource "aws_iam_role_policy_attachment" "rds_policy_attach" {
  role       = aws_iam_role.lambda_exec_role.name
  policy_arn = "arn:aws:iam::aws:policy/AmazonRDSFullAccess"
}
