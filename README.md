# Second Hand Luxury Market Data Pipeline 
This project demonstrates the second hand luxury market trend analysis pipeline using Google Cloud Platform (GCP). 

It processes and analyzes second hand luxury product sales data to uncover insights such as Seller Distribution by Country, Average Brand Price and so on.
The entire pipeline is developed using Batch Processing with Apache Spark on Dataproc, Workflow Orchestration with Apache Airflow (Cloud Composer), and Data Warehousing with BigQuery. Some part of the project is automated using Terraform (Infrastructure as Code). 

This project is the final part of this Zoomcamp: https://github.com/DataTalksClub/data-engineering-zoomcamp

## 🛠 Tech Stack
- Cloud Provider:

  Google Cloud Platform (GCP): Scalable and fully managed cloud services.
  
- Infrastructure as Code (IaC):

  Terraform: Automate the creation of infrastructure (Cloud Storage and BigQuery).

- Batch Processing:

  Apache Spark on Dataproc: Perform large-scale batch transformations on luxury sales data.

- Workflow Orchestration:
  
  Apache Airflow (Cloud Composer): Schedule and manage the ETL workflow.

- Data Warehouse:
  
  BigQuery: Serverless and scalable data warehouse for analysis.

 - Data Visualization:
    
   Looker Studio: Visualization tool for reporting and insights.
   
## 🔧Project Architecture
This project sets up an automated data pipeline using Docker, Airflow, dataproc, Terraform, and Spark, all integrated into Google Cloud Platform (GCP). The pipeline will store data in Google Cloud Storage (GCS), process and transform it in batches, perform transformations using dataproc, and load it into BigQuery.

![Screenshot 2025-04-11 231134](https://github.com/user-attachments/assets/7b0f469f-26bd-4b32-ae24-7d985733929d)

The pipeline consists of the following key components:

 - Kaggle + Google Colab : for data ingestion

 - Docker: Containerizes Terraform.


- Airflow: Orchestrates the entire pipeline with DAGs (Directed Acyclic Graphs).


- Terraform: Automates the provisioning of GCP resources like storage buckets and BigQuery datasets.


- Spark: Processes data in batches and writes it to BigQuery for reporting or analysis.

- Looker: Studio for visualization

## 📊Dashboard:
Key Insights:

- 🗺 Seller Distribution by Country

- 💸 Average Brand Price

- 👜 Product Type % by Brand

- 📈 Sales % by Day Interval

  
  
  ![Vestiaire_Collective_Data_page-0001](https://github.com/user-attachments/assets/7b439afc-9f20-4f71-ac9c-0169d02fa1ad)




## 🔄 Reproducibility
How to Run the Project:
Clone the repository.

### 📦 Prerequisites

1- Google Cloud Platform (GCP) Project

2- Billing Enabled on the project

3- Service Account with the following IAM roles:

  - roles/storage.admin

  - roles/bigquery.admin

  - roles/dataproc.editor

  - roles/composer.admin

  - roles/iam.serviceAccountUser

  - Terraform 

  - Docker

  - Kaggle API token for data extraction

  - Python 3 (for GCP and Kaggle scripts if used locally)

## 🐳 Docker & Terraform Setup

  - Dockerfile
  - Terraform Files (variables.tf and main.tf)

1. Dockerfile
  
   ```YAML FROM hashicorp/terraform:latest
    
    ENTRYPOINT []
    WORKDIR /app
    COPY . /app
    CMD terraform init && terraform plan && terraform apply -auto-approve  


2. Build Docker Image
  
      ```Bash docker build -t tf-gcp .``` 
  
3. Run Terraform in Docker
  
    ```
       docker run -it --rm \
       -v $(pwd):/workspace \
       -v $(pwd)/key.json:/key.json \
       -e GOOGLE_APPLICATION_CREDENTIALS=/key.json \
       tf-gcp
    
4. If needed run :
    ```Bash
            terraform init
            terraform plan
            terraform apply -auto-approve

## 📥 Kaggle Data Extraction (Colab) : Kaggle → Colab → GCS

Use colab_notebook.ipynb to:

- Authenticate to Kaggle

- Download dataset
  
- Upload to GCS using google.cloud.storage

## ⚙️ Airflow DAGs (Composer)

1- Create Cloud Composer Environment

2- Create DAGs (Directed Acyclic Graphs)

 - Write Airflow DAGs to automate workflows. These DAGs will:

- Process data from GCS (loading data into BigQuery).
  
  How you can also submit it manually
  ```
     bq load --source_format=CSV \
      --autodetect \
      --skip_leading_rows=1 \
      --field_delimiter=',' \
      --quote='"' \
      --allow_quoted_newlines \
      --allow_jagged_rows \
      'project_id:table.dataset' \
      gs://bucket-Name/data/processed/dataset.csv/*.csv

- Trigger batch processing file using Dataproc.
  
  Before create a cluster:
    ```
   gcloud dataproc clusters create cluster-Name\
  --region=europe-west1 \
  --zone=europe-west1-b \
  --master-machine-type=n1-standard-2 \
  --worker-machine-type=n1-standard-2 \
  --num-workers=2 \
  --enable-component-gateway \
  --image-version=2.1.84-debian11 \
  --autoscaling-policy=basic-autoscaling-policy\
  --master-boot-disk-size=500GB \
  --worker-boot-disk-size=500GB \
  --bucket=bucket-Name

Then submit it :
    <pre> ``` gcloud dataproc jobs submit pyspark gs://bucket-Name/Scripts/Spark_Batch_processing.py \
             --cluster=cluster-Name \ 
              --region=europe-west1 ``` </pre>
           

3- Upload DAGs to Cloud Composer

- Upload your Airflow DAG files to the GCS bucket.

- This will automatically register the DAGs in Airflow.

  
![Screenshot 2025-04-13 112724](https://github.com/user-attachments/assets/862bbb9c-1a76-408d-859e-24730d6cea1d)

  

## Next Step 
Environment Separation
 - Create distinct Dev / Prod environments using Terraform workspaces or separate configurations.

State Management with GCS Backend
 - Store Terraform state remotely in GCS for collaboration and safety, with locking enabled.

Monitoring, Logging & Alerts
 -  Enable Stackdriver (Cloud Monitoring) for DataProc, Composer, and BigQuery to track job health and trigger alerts on failures.

## ✅ Credits
Built by Me , using open data from <a href="https://www.kaggle.com/datasets/justinpakzad/vestiaire-fashion-dataset" target="_blank">Kaggle Vestiaire Collective Dataset</a>, GCP services, and open-source tooling.

## 💡 License
This project is licensed under the MIT License - see the LICENSE file for details.

## 🧑‍💻 Author
Assitan NIARE 

www.linkedin.com/in/
assitan-niaré-data

