FROM hashicorp/terraform:latest


ENTRYPOINT []

# Create the work directory
WORKDIR /app

# Copy all in terraform folder
COPY . /app

# Execute the Terraform Init and apply directly
CMD terraform init && terraform plan && terraform apply -auto-approve
