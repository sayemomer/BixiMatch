# BixiMatch

# Problem Statement

Solve the supply and demand curve. Here, supply is the number of bikes in a station and a number of users which is the demand for a given day or even hour. It is essentially a supply meets demand problem.

<details>
  <h2>Contents</h2>
  
  - [Regression Level](#Target-Feature)

  - [Data Collection & Preprocessing](#data-collection--preprocessing)
    - [Dataset Summary](#dataset-summary)
    - [Images/Class Distribution](#imagesclass-distribution)
    - [Data Cleaning Process for Facial Expression Recognition](#data-cleaning-process-for-facial-expression-recognition)
      - [Labeling](#labeling)
      - [Resizing Images](#resizing-images)
      - [Grayscale Conversion](#grayscale-conversion)
      - [Brightness Normalization](#brightness-normalization)
      - [Cropping](#cropping)
    - [Class Distribution](#class-distribution-1)
  - [CNN Architecture , Training, & Evaluation](#cnn-architecture--training--evaluation)
    - [Architecture](#architecture)
  - [Bias Analysis, Model refinement, & deep evaluation](#bias-analysis-model-refinement--deep-evaluation)
    - [Performance Metrics](#performance-metrics)
    - [Variants comparison](#variants-comparison)
    - [Confusion Matrix Analysis](#confusion-matrix-analysis)
      - [Main Model](#main-model)
      - [Variants](#variants)
    - [Impact of Architectural Variations](#impact-of-architectural-variations)
    - [Bias Analysis](#bias-analysis)
      - [Bias detection result](#bias-detection-result)
      - [Bias Mitigation](#bias-mitigation)
      - [Bias detection result after mitigation](#bias-detection-result-after-mitigation)
    - [K-fold Cross Validation](#k-fold-cross-validation)
      - [Original Model](#original-model)
      - [K-fold Model](#k-fold-model)
      - [original vs k-fold](#original-vs-k-fold)
  - [Steps for Running the Python File](#steps-for-running-the-python-file)
    - [Prerequisites](#prerequisites)
    - [Setup the Datasets](#setup-the-datasets)
    - [Setup Virtual Environment](#setup-virtual-environment)
    - [Install Dependencies](#install-dependencies)
    - [Execution Steps](#execution-steps)
    - [Expected Output](#expected-output)

 - [Refecence to the original project](#refecence-to-the-original-project)
  - [Conclusion and Future Work](#conclusion-and-future-work)
</details>

# Target Feature

- Number of trips per day

# Data Collection & Preprocessing


## Dataset Summary
Here is a summary of the datasets used in the project:

    BIXI - Movements history 2014 to 2017
        Total row: ~4018722 * 4
        Column: 6
        Features: start_date, start_station_code ,end_date , end_station_code, duration_sec, is_member
        Source: https://bixi.com/en/open-data/

    Historical Hourly Weather Data
        Total row: ~45253
        Column: 37
        Features: 30 US & Canadian Cities + 6 Israeli Cities
        Source: [https://www.kaggle.com/datasets/mahmoudima/mma-facial-expression](https://www.kaggle.com/datasets/selfishgene/historical-hourly-weather-data)

## Training vs Test data distribution

 - 2014 to 2016 bike uses data is used for training and corresponding weather data
- 2017 bike uses data is used for testing and corresponding weather data

## Data Cleaning Process

### Type Conversion

 1. Convert the start_date and end_date to datetime format

### Filter

  1. Filter the data weather data for the only city of Montreal

### Merge

  1. Merge the bike data with the weather data based on the start_date

### Imputing missing values

  1. Impute the missing values in the weather data using the mean , meadian or mode of the column

### Droping rows

  1. Drop the rows with missing values in the bike data

## Data distribution

## Sample data

 See notebooks/data_exploration.ipynb

# Feature Engineering

## Feature Extraction

  1. Extract the features from the date column like num_week, weekday, hour

## Feature Selection

  1. Group by the data based on the num_week, weekday, hour
  2. Calculate the number of trips per day based on the group
  3. Drop the columns which are not required for the model

## Feature Transformation

  1. Level encoding for the categorical column Description of the weather
  2. Normalization of the train and test data using MinMaxScaler

# Model Selection

## Model & Training

## Model

  1. Linear Regression

## Training

  1. Train the model using the training data
  2. Predict the number of trips per day using the test data

## Model Evaluation

  1. Calculate the MSE value for the model


### TODO

- [ ] Prototype the model using streamlit
- [ ] Develop FastAPI for the model
- [ ] Automate the using docker








