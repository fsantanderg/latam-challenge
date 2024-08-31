resource "aws_vpc" "latam-vpc" {
  cidr_block = "10.0.0.0/16"

  tags = {
    Name = "latam-vpc-vpc"
  }
}

resource "aws_subnet" "private" {
  count                   = 2
  vpc_id                  = aws_vpc.latam-vpc.id
  cidr_block              = cidrsubnet(aws_vpc.latam-vpc.cidr_block, 8, count.index)
  availability_zone       = element(data.aws_availability_zones.available.names, count.index)
  map_public_ip_on_launch = false

  tags = {
    Name = "private-subnet-${count.index}"
  }
}



//output "private_subnets" {
//  value = aws_subnet.private[*].id
//}

resource "kubernetes_persistent_volume_claim" "postgres_citus_pvc" {
  count = 10

  metadata {
    name      = "postgres-pv-claim-${count.index}"
    namespace = "latam"
  }

  spec {
    access_modes = ["ReadWriteOnce"]

    resources {
      requests = {
        storage = "5Gi"
      }
    }
  }
}
