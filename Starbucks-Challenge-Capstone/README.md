# Udacity Data Scientist Nanodegree - Project Starbucks Challenge

## Table of Contents
1. [Introduction](#introduction)
2. [File Descriptions](#descriptions)
3. [Instructions](#instructions)
4. [Acknowledgements](#acknowledgements)


<a name="introduction"></a>
## Introduction

![Alt-Text](https://storage.googleapis.com/afs-prod/media/4f106493fa9a417582aa8c58342db214/1000.jpeg)

The data set of this project contains simulated data that mimics customer behavior on the Starbucks rewards mobile app. Once every few days, Starbucks sends out an offer to users of the mobile app. An offer can be merely an advertisement for a drink or an actual offer such as a discount or BOGO (buy one get one free). Some users might not receive any offer during certain weeks. Not all users receive the same offer. We combine transaction, demographic and offer data to determine what kind of offer will be the most effective to stimulate conversion, in other words, which offer to send to each customer.
For this project, we will be leveraging the data graciously provided to us by Udacity. This is given to us in the form of three JSON files. Before delving into those individual files, let us first understand the three types of offers that Starbucks is looking to potentially send its customers:

- **Buy-One-Get-One (BOGO)**: In this particular offer, a customer is given a reward that enables them to receive an extra, equal product at no cost. The customer must spend a certain threshold in order to make this reward available.
- **Discount**: With this offer, a customer is given a reward that knocks a certain percentage off the original cost of the product they are choosing to purchase, subject to limitations.
- **Informational**: With this final offer, there isn’t necessarily a reward but rather an opportunity for a customer to purchase a certain object given a requisite amount of money. (This might be something like letting customers know that Pumpkin Spice Latte is coming available again toward the beginning of autumn.)


<a name="descriptions"></a>
## File Descriptions
With that understanding established, let’s now look at the three provided JSON files and their respective elements:

**profile.json**
This file contains dummy information about Rewards program users. This will serve as the basis for basic customer information.
(17000 users x 5 fields)
  - gender: (categorical) M, F, O, or null
  - age: (numeric) missing value encoded as 118
  - id: (string / hash)
  - became_member_on: (date) format YYYYMMDD
  - income: (numeric)

**portfolio.json**
This file contains offers sent during a 30-day test period. This will serve as the basis to understand our customers’ purchasing patterns.
(10 offers x 6 fields)
  - reward: (numeric) money awarded for the amount spent
  - channels: (list) web, email, mobile, social
  - difficulty: (numeric) money required to be spent to receive reward
  - duration: (numeric) time for offer to be open, in days
  - offer_type: (string) bogo, discount, informational
  - id: (string / hash)

**transcript.json**
This file contains event log information. Complementing the file above, this file will serve as a more granular look into customer behavior.
(306648 events x 4 fields)
  - person: (string / hash)
  - event: (string) offer received, offer viewed, transaction, offer completed
  - value: (dictionary) different values depending on the event type
  - offer id : (string / hash) not associated with any “transaction”
  - amount: (numeric) money spent in “transaction”
  - reward: (numeric) money gained from “offer completed”
  - time: (numeric) hours after start of test

### Libraries Used
* Pandas
* Numpy
* Matplotlib
* Seaborn
* Scikit-learn

All of these modules can be installed by using the Anaconda package.

<a name="instructions"></a>
## Instructions
Run the codes inside Jupyter notebook to complete the project.

## Acknowledgements

* [Udacity](https://www.udacity.com/) for providing an excellent Data Scientist training program.
* [Starbucks](https://www.starbucks.com/) for providing the dataset
