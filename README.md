# Twitter-Data-Streaming-Pipeline using python on Airflow, Amazon ec2 and Amazon s3

This project use Twitter API to extract Tweets continuously on Twitter from a specified user. Use python to transform the data from json to css data frame, then deploy the code on Apache airflow and Amazon EC2 and save the final result to Amazon S3.

A number of libraries were used;
Datetime
Pandas
S3fs
Airflow
Tweepy
json

All these libraries will need to be install and imported appropriately.

The steps taken for this project are:

1. Extract the tweets from Twitter using your twitter API and secret tokens
2. Provide twitter authentication using tweepy
3. Create API objects using the required username.
4. Print those tweets as json file to confirm it worked
5. convert the json to pandas data frame.
6. Create an ec2 instance on AWS
7. Use that to connect to airflow server
8. Move all files from your local machine to airflow.
9. Execute the code in airflow and create an S3 bucket
10. Store the resulting data in the S3 bucket for future use.
