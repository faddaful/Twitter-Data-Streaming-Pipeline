# Twitter Streaming Data Pipeline using Python on Airflow, Amazon EC2, and Amazon S3**

In this project, I undertook the exciting challenge of building a robust Twitter Streaming Data Pipeline that seamlessly extracts tweets from specified users using the Twitter API, transforms the data into a structured CSS data frame using Python, and then orchestrates the entire process using Apache Airflow. The final results are stored efficiently in an Amazon S3 bucket, ensuring scalability and accessibility for future use.

## Project Steps:

### 1. Twitter Data Extraction:
   - Utilized Twitter API and secret tokens to fetch tweets continuously.
   - Employed Tweepy library for seamless Twitter authentication.
   - Created API objects using the target username for extraction.
   - Verified successful data extraction by printing tweets as JSON files.

### 2. Data Transformation:
   - Transformed the JSON-format tweets into a structured Pandas data frame using Python.
   - Utilized libraries like Datetime, Pandas, and json to achieve this conversion.

### 3. Apache Airflow Setup and EC2 Instance Creation:
   - Established an Amazon EC2 instance to facilitate project deployment and execution.
   - Created an EC2 instance on AWS, providing a scalable and controlled environment.
   - Ensured connectivity between the EC2 instance and the Airflow server.

### 4. Code Deployment and Orchestration:
   - Moved project files and code from the local machine to the Airflow server.
   - Orchestrated the data pipeline execution using Apache Airflow.
   - Created DAGs (Directed Acyclic Graphs) to define the workflow and dependencies.

### 5. S3 Bucket and Data Storage:
   - Leveraged Amazon S3, a reliable and scalable storage solution.
   - Executed the code within the Airflow environment to capture transformed data.
   - Created an S3 bucket to securely store the resulting data for future analysis.

### 6. Key Technologies and Libraries Used:
  - Twitter API for data extraction.
  - Tweepy for Twitter authentication.
  - Datetime, Pandas, S3fs, and json for data manipulation and transformation.
  - Apache Airflow for orchestration and scheduling.
  - Amazon EC2 for deploying code and running the data pipeline.
  - Amazon S3 for secure and scalable data storage.

Through the systematic execution of these steps, I successfully designed and implemented a comprehensive Twitter Streaming Data Pipeline. This pipeline not only efficiently extracts and transforms Twitter data but also ensures seamless deployment and execution using Apache Airflow and Amazon EC2. The data's ultimate destination is an Amazon S3 bucket, providing a reliable and scalable storage solution for future analysis and insights. This project showcases the power of data engineering in managing and processing real-time social media data for informed decision-making.
