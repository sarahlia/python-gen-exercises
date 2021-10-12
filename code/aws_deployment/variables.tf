variable "profile" {
        type = string
        default = "default"
}

variable "region-master" {
        type = string
        default = "us-east-1"
}

variable "region-worker" {
        type = string
        default = "us-west-2"
}

variable "workers-count" {
  type    = number
  default = 1
}

variable "instance-type" {
  type    = string
  default = "t3.micro"
}

variable "webserver-port" {
  type    = number
  default = 80
}