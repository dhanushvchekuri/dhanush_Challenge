# AWS Infrastructure with Terraform

This project demonstrates the setup of a simple web infrastructure on AWS using Terraform. It provisions a Virtual Private Cloud (VPC), public subnets, security groups, EC2 instances, an Application Load Balancer (ALB), and corresponding target groups. This setup ensures high availability and scalability for a basic web application.

## Table of Contents

- [Requirements](#requirements)
- [Project Structure](#project-structure)
- [Resources Created](#resources-created)
- [User Data Scripts](#user-data-scripts)
- [How to Deploy](#how-to-deploy)
- [Outputs](#outputs)
- [Cleanup](#cleanup)
- [Conclusion](#conclusion)

## Requirements

Before you can deploy this infrastructure, ensure you have the following:

- [Terraform](https://www.terraform.io/downloads.html) (version 1.0 or later)
- An AWS account with necessary permissions to create resources such as VPCs, EC2 instances, load balancers, and security groups.

## Project Structure

The repository contains the following files:

- `main.tf`: Defines the main infrastructure resources such as VPC, subnets, EC2 instances, ALB, security groups, etc.
- `provider.tf`: Specifies the AWS provider configuration, including the region and provider version.
- `variables.tf`: Defines the input variables for the Terraform configuration, such as the VPC CIDR block.
- `userdata1.sh`: User data script for configuring the first EC2 instance (webserver1).
- `userdata2.sh`: User data script for configuring the second EC2 instance (webserver2).

### Directory Structure

```bash
.
├── main.tf
├── provider.tf
├── variables.tf
├── userdata1.sh
└── userdata2.sh
```

### Resources Created

The Terraform configuration deploys the following AWS resources:

> **VPC**: A Virtual Private Cloud with a configurable CIDR block (10.0.0.0/16 by default). <br>

>**Subnets**: Two public subnets in different Availability Zones (AZs) (us-east-1a and us-east-1b) to provide redundancy. <br>

>**Internet Gateway**: To enable outbound internet access for the instances within the VPC. <br>

>**Route Table**: Associates a route table to the subnets to route traffic to the internet via the internet gateway. <br>

>**Security Group**: Configures inbound rules for HTTP (port 80) and SSH (port 22) and outbound traffic to allow communication between EC2 instances and the internet. <br>

>**EC2 Instances**: Two instances (webserver1 and webserver2) with Apache HTTP Server, each in a different subnet for high availability. <br>

>**Application Load Balancer (ALB)**: Distributes HTTP traffic across the two EC2 instances. <br>

>**Target Group**: ALB forwards traffic to EC2 instances using this target group. <br>

>**Listener**: Listens on port 80 and forwards HTTP traffic to the target group.

### User Data Scripts

Both scripts userdata.sh and userdata.1sh serves a basic Hello World HTML page with slight changes. The instances are differentiated by:

`Hello World (i1)` for Instance 1

`Hello World (i2)` for Instance 2

to show the load balancer balancing the load between two instances. Both scripts install the necessary software (Apache), write a custom HTML page to /var/www/html/index.html, and ensure the web server is started and enabled on boot.

### How to Deploy

1. Clone this repository: Download or clone the repository to your local machine.
   
   `git clone https://github.com/dhanushvchekuri/dhanush_Challenge.git`

   `cd dhanush_Challenge`
2. Initialize Terraform: Run the following command to initialize Terraform, which will download the necessary provider plugins.

   `terraform init`
   
3. Review the plan: Check what resources Terraform will create by running:
   
   `terraform plan`

   This will give you a detailed preview of all the changes Terraform will apply.

4. Apply the configuration: Deploy the resources by executing:
   
   `terraform apply`

   Review and confirm the action by typing **yes**.

5. Access the Load Balancer: After deployment, Terraform will output the DNS name of the load balancer. You can use this DNS to access your web application through a browser.

### Outputs

Upon successful deployment, Terraform will output the following:

Load Balancer DNS Name: This is the public DNS address of your ALB, which you can use to access the application.
The output looks something like:

`loadbalancerdns = "myalb-1234567890.us-east-1.elb.amazonaws.com`

### Cleanup

To tear down and clean up all the AWS resources created by this Terraform configuration, run: `terraform destroy`

This command will remove all the resources, ensuring you don’t incur billing charges for unused infra.

### Conclusion

This project provides a basic AWS infrastructure using Terraform that includes a VPC, two public subnets, EC2 instances with Apache installed, and an Application Load Balancer (ALB) for distributing traffic. Next step is to expand this setup by adding Auto Scaling Groups (ASG), more complex networking features and deploying microservices on instances of ASGs.
