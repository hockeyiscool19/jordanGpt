#!/bin/bash

source dev.env


case "$1" in
  -b) docker build -t jordangpt . ;;
  -r) docker run -it -p 7860:7860 jordangpt ;;
  -l) aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin $AWS_ACCOUNT_NUM.dkr.ecr.us-east-1.amazonaws.com ;;
  -p) docker push $AWS_ACCOUNT_NUM.dkr.ecr.us-east-1.amazonaws.com/jordangpt:tag && docker tag my-cli:latest $AWS_ACCOUNT_NUM.dkr.ecr.us-east-1.amazonaws.com/jordangpt:tag ;;
  -m) docker tag my-cli:latest $AWS_ACCOUNT_NUM.dkr.ecr.us-east-1.amazonaws.com/jordangpt:tag ;;
  -r) docker stop temp && docker rm temp ;;
  -a) docker build --no-cache -t jordangpt . && 
        aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin $AWS_ACCOUNT_NUM.dkr.ecr.us-east-1.amazonaws.com &&
        docker push $AWS_ACCOUNT_NUM.dkr.ecr.us-east-1.amazonaws.com/jordangpt:tag && docker tag my-cli:latest $AWS_ACCOUNT_NUM.dkr.ecr.us-east-1.amazonaws.com/jordangpt:tag &&
        docker tag my-cli:latest $AWS_ACCOUNT_NUM.dkr.ecr.us-east-1.amazonaws.com/jordangpt:tag &&
        docker stop temp && 
        docker rm temp &&
        docker run -it --name temp $AWS_ACCOUNT_NUM.dkr.ecr.us-east-1.amazonaws.com/jordangpt:tag ;;

  *) echo "Invalid option";;
esac

