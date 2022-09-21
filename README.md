# Cloud Resume Challenge
This project is my solution to cloud resume challenge which creates a serverless website with visiter counter using AWS. You can see the challenge [here](https://cloudresumechallenge.dev/)

### Prerequisites
1. AWS Account
2. AWS CLI installed(for more information check [here](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) 
3. Domain Name (for more information check [here](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/domain-register.html)

### Building Website as Infrastucture as Code
Run this commands inside working directory.
1. Change "-Name" variable inside Route53, "DomainName" variable inside ACMCertificate and "-Aliases" variable inside CloudfrontDistributionWebsite as your domain name in template.yaml file 
![alt text](https://github.com/MalikGuzeldemirci/Cloud-Resume-Challenge/blob/master/README.md-photos/c1.png)
![alt text](https://github.com/MalikGuzeldemirci/Cloud-Resume-Challenge/blob/master/README.md-photos/c2.png)
![alt text](https://github.com/MalikGuzeldemirci/Cloud-Resume-Challenge/blob/master/README.md-photos/c3.png)
2. Delete my samconfig.toml file and use "sam build" command
![alt text](https://github.com/MalikGuzeldemirci/Cloud-Resume-Challenge/blob/master/README.md-photos/sam-build.png)
3. Use "sam deploy --guided" command and complete the config questions. Make sure to choose region as us-east-1
![alt text](https://github.com/MalikGuzeldemirci/Cloud-Resume-Challenge/blob/master/README.md-photos/sam-deploy.png)
4. Wait for the certificate to be created then go to AWS Certificate Manager and validate your domain name (for more information check [here](https://docs.aws.amazon.com/acm/latest/userguide/dns-validation.html)
![alt text](https://github.com/MalikGuzeldemirci/Cloud-Resume-Challenge/blob/master/README.md-photos/certificatepng.png)
5. After the validation and some time "sam deploy --guided" command will be completed.
6. Go to getCount funciton and change FunctionName parameter inside invoke funtion as your ARN of AWS incrementCount lambda function
![alt text](https://github.com/MalikGuzeldemirci/Cloud-Resume-Challenge/blob/master/README.md-photos/getCount.png)
7. Upload your website files (including index.html) inside website directory and make sure you fetch your api inside your html file if you want to count visit number
![alt text](https://github.com/MalikGuzeldemirci/Cloud-Resume-Challenge/blob/master/README.md-photos/fetch.png)
8. Upload your website files to S3 using "aws s3 sync ./website s3://{S3 Bucket Name}" command  
![alt text](https://github.com/MalikGuzeldemirci/Cloud-Resume-Challenge/blob/master/README.md-photos/uploadS3.png)
9. Run createTableItem.py file to add column named VisitCount to your table element
10. Use "sam build" and "sam deploy" commands again
11. CI/CD part was handled in github/workflow/main.yaml file. You just need to upload all files to github repository and add your AWS keys named as AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY in github secrets.

**Note: If you change any other my name variables inside any file such as BucketName that I used in my code, you have to rearrange my code according to it.**
