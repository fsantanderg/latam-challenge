output "cluster_endpoint" {
  value = aws_eks_cluster.latam-vpc.endpoint
}

output "cluster_certificate_authority" {
  value = aws_eks_cluster.latam-vpc.certificate_authority.0.data
}

output "cluster_id" {
  value = aws_eks_cluster.latam-vpc.id
}
