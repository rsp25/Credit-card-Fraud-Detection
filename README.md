# Credit card fraud detection

## Table of Content
  * [Overview](#overview)
  * [Motivation](#motivation)
  * [Technical Aspect](#technical-aspect)
  * [Installation](#installation)
  * [Run](#run)
  * [Deployement on Heroku](#deployement-on-heroku)
  * [Directory Tree](#directory-tree)
  * [Bug / Feature Request](#bug---feature-request)
  * [Technologies Used](#technologies-used)

## Overview
This model will help you to predict the occurrence of credit card fraud on the basis of your background information.

## Motivation
Now-a-days with the advancement of technology, frauds are becoming very common. This wil help to give the probability of occurrence of fraud.

## Technical Aspect
This project is divided into three parts:
1. Training a machine learning model with the help of classification algorithms. 
2. Building and hosting a Flask web app.
3. Building a simple UI using html & css
    - A user needs to provide income, family size, month in which he/she started working (begin month), age and years of employment. 
    - Answers of basic questions should b provided with either Yes or No.
    - After providing the inputs prediction of prediction of occurrence of fraud will be shown.

## Installation
The code is written in jupyter notebook and flask server is written in spyder app, so in order to run this code in simpliest manner just download anaconda. 
If your machine doesn't support anaconda simply download jupyter notebook using python(cmd) and instead of spyder you can use visual studio.

## Run
1.Download the whole project 
2.Open main.py file in spyder 
3.Run main.py file.
4.You will get a URL in console.
5.Copy the URL in local browser and you will be redirected to the UI. 

## Deployement on Heroku
https://creditcardfraudcalculator.herokuapp.com/

Click on the above link to open the project.


## Directory Tree 
```
├── templates
│   ├── index.html
├── Procfile
├── README.md
├── credit_card_fraud-Copy1.ipynb
├── credit_card_fraud_model.pickle
├── main.py
├── requirements.txt

```

## Bug / Feature Request
If you find a bug (the website couldn't handle the query and / or gave undesired results), kindly open an issue [here](https://github.com/rsp25/Credit-card-Fraud-Detection/issues/new) by including your search query and the expected result.

If you'd like to request a new function, feel free to do so by opening an issue [here](https://github.com/rsp25/Credit-card-Fraud-Detection/issues/new). Please include sample queries and their corresponding results.

## Technologies Used

1.pandas 
2.numpy
3.Matplotlib
4.Seaborn
5.Classification models
  - Decision Tree model
  - Random Forest
