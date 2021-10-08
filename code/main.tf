provider "aws" {
        region = "us-east-1"
}

resource "aws_instance" "vm" {
        ami = "ami-02e136e904f3da870"
        subnet_id = "subnet-0969c4681270c7fe5"
        instance_type = "t3.micro"
        tags = {
                Name = "my-first-tf-node"
        }
}
