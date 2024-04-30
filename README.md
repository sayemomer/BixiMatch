# BixiMatch

# Problem Statement

Solve the supply and demand curve. Here, supply is the number of bikes in a station and a number of users which is the demand for a given day or even hour. It is essentially a supply meets demand problem.

<details>
  <summary><h2>Contents</h2></summary>
  
  - [Classification Labels](#classification-labels)

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

## Classification Labels


# Data Collection & Preprocessing


## Dataset Summary
Here is a summary of the datasets used in the project:

    BIXI - Movements history 2017
        Total row: ~4018722
        Column: 6
        Features: start_date, start_station_code ,end_date , end_station_code, duration_sec, is_member
        Source: https://bixi.com/en/open-data/

    Historical Hourly Weather Data
        Total row: ~45253
        Column: 37
        Features: 30 US & Canadian Cities + 6 Israeli Cities
        Source: [https://www.kaggle.com/datasets/mahmoudima/mma-facial-expression](https://www.kaggle.com/datasets/selfishgene/historical-hourly-weather-data)

## Training vs Test data distribution

## Data Cleaning Process

### Type Conversion

### Filter

### Merge

### Cropping

## Class Distribution

## Sample data

## Weather distribution/trips


