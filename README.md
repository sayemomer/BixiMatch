# BixiMatch

# Problem Statement

Solve the supply and demand curve. Here, supply is the number of bikes in a station and a number of users which is the demand for a given day or even hour. It is essentially a supply meets demand problem.

<details>
  <summary>
    ## Contents 
  </summary>
  
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

    BIXI - Movements history
        Total row: ~4018722
        Column: 6
        Features: start_date, start_station_code ,end_date , end_station_code, duration_sec, is_member
        Source: https://bixi.com/en/open-data/

    Historical Hourly Weather Data
        Total row: ~45253
        Column: 37
        Features: 30 US & Canadian Cities + 6 Israeli Cities
        Source: [https://www.kaggle.com/datasets/mahmoudima/mma-facial-expression](https://www.kaggle.com/datasets/selfishgene/historical-hourly-weather-data)

## Images/Class Distribution

    Class Training Test
    Angry	  600	  60
    bored	  800	  50
    Engaged	850	  70
    Neutral	750	  65


## Data Cleaning Process for Facial Expression Recognition

### Labeling

### Resizing Images
All images are resized to a standard dimension to ensure consistency across the dataset.

```python
from keras.preprocessing.image import ImageDataGenerator

# Assuming images are in a directory 'data/train'
datagen = ImageDataGenerator(rescale=1./255)

# Standard dimensions for all images
standard_size = (150, 150)

# Generator will resize images automatically
train_generator = datagen.flow_from_directory(
    'data/train',
    target_size=standard_size,
    color_mode='grayscale', # Convert images to grayscale
    batch_size=32,
    class_mode='categorical'
)
```
### Grayscale Conversion

Images are converted to grayscale to focus on the important features without the distraction of color.
### Brightness Normalization

Uniform lighting conditions are applied to images to mitigate the effects of varying illumination.

```
# Additional configuration for ImageDataGenerator to adjust brightness

datagen = ImageDataGenerator(
    rescale=1./255,
    brightness_range=[0.8,1.2] # Adjust brightness
)
```
### Cropping

Images are cropped to remove background noise and focus on the face, the most important part for emotion detection.

## Class Distribution

## Sample Images

## Pixel Intensity Distribution


