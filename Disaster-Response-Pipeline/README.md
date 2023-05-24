# Udacity Data Scientist Nanodegree - Project Disaster Response Pipeline

## Table of Contents
1. [Introduction](#introduction)
2. [File Description](#descripton)
3. [Installing and Instruction](#instructions)
4. [Acknowledgements](#acknowledgements)

<a name="introduction"></a>
## Introduction


![Alt-Text](https://www.savethechildren.org/content/dam/global/images/countries/nepal/nepal-helicopter-emergency-m174091-hero.jpg/_jcr_content/renditions/cq5dam.thumbnail.1700.1700.jpg)



This project "Disaster Response Pipeline" is part of the Udacity Data Scientist Nanodegree in cooperation with Figure Eight.
The target of the project is to classify disaster messages based on data from real disasters with the help of a Natural Language Processing Model (NLP).

Proceeding with the **help of machine learning** has the **advantage** that disaster messages coming in via the various channels can be **classified quickly** without having to read through the entire text manually. This means that they **can then be assigned** by several disaster response agencies **immediately** and in a **targeted manner** to the right aid organization.

**This will help the disaster victims to receive prompt medical aid and speedy recovery from the effects of the disasters.**

<a name="description"></a>
## File Description

### Folder: app
**run.py** - python script to launch web application.<br/>
Folder: templates - web dependency files (go.html & master.html) required to run the web application.

### Folder: data
**disaster_messages.csv** - real messages sent during disaster events (provided by Figure Eight)<br/>
**disaster_categories.csv** - categories of the messages<br/>
**process_data.py** - ETL pipeline used to load, clean, extract feature and store data in SQLite database<br/>
**ETL Pipeline Preparation.ipynb** - Jupyter Notebook used to prepare ETL pipeline<br/>
**DisasterResponse.db** - cleaned data stored in SQlite database

### Folder: models
**train_classifier.py** - ML pipeline used to load cleaned data, train model and save trained model as pickle (.pkl) file for later use<br/>
**classifier.pkl** - pickle file contains trained model<br/>
**ML Pipeline Preparation.ipynb** - Jupyter Notebook used to prepare ML pipeline

### Libraries Used

* Numpy
* Pandas
* Scikit-learn
* NLTK
* SQLalchemy
* Pickle
* Flask, Plotly

All of these modules can be installed by using the Anaconda package.

<a name="instructions"></a>
## Instructions:

1. Run the following commands in the project's root directory to set up your database and model.

    - To run ETL pipeline that cleans data and stores in database
        `python data/process_data.py data/disaster_messages.csv data/disaster_categories.csv data/DisasterResponse.db`
    - To run ML pipeline that trains classifier and saves
        `python models/train_classifier.py data/DisasterResponse.db models/classifier.pkl`

2. Run the following command in the app's directory to run your web app.
    `python run.py`

3. Go to http://0.0.0.0:3001/

<a name="acknowledgements"></a>
## Acknowledgements

* [Udacity](https://www.udacity.com/) for providing an excellent Data Scientist training program.
* [Figure Eight](https://www.figure-eight.com/) for providing dataset to train our model.
