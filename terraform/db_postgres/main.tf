provider "aws" {
  region = "us-east-2"
}

resource "aws_db_instance" "postgres_instance" {
  allocated_storage    = 20
  max_allocated_storage  = 100
  engine               = "postgres"
  engine_version       = "13.15"
  instance_class       = "db.t3.micro" #Tamano de la Maquina
  db_name              = "latamdb"
  username             = "latam_user"
  password             = "latam_password"
  skip_final_snapshot  = true

  multi_az = false

  vpc_security_group_ids = [aws_security_group.db_sg.id]

  backup_retention_period = 7
}

resource "aws_security_group" "db_sg" {
  name_prefix = "db-sg"

  ingress {
    from_port   = 5432
    to_port     = 5432
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = "postgres-db-sg"
  }
}
