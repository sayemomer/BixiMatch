# BixiMatch

# Problem Statement

Solve the supply and demand curve. Here, supply is the number of bikes in a station and a number of users which is the demand for a given day or even hour. It is essentially a supply meets demand problem.

## Contents
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

## Classification Labels


# Data Collection & Preprocessing


## Dataset Summary
Here is a summary of the datasets used in the project:

    IMDB-WIKI
        Total Images: ~500,000
        Image/Class: ~10,000
        Features: Age / Gender labels
        Source: https://data.vision.ee.ethz.ch/cvl/rrothe/imdb-wiki/

    MMA FACIAL EXPRESSION
        Total Images: ~128,000
        Image/Class: ~6,500
        Features: Compact images, Only frontal faces, RGB images
        Source: https://www.kaggle.com/datasets/mahmoudima/mma-facial-expression

    UTKFace
        Total Images: ~20,000
        Image/Class: Unknown
        Features: Diverse images, Only frontal faces, Duplicate-free
        Source: https://susanqq.github.io/UTKFace/

    Real and Fake Face Detection
        Total Images: ~2,000
        Image/Class: ~1,000
        Features: High resolution, Only frontal faces, Duplicate-free
        Source: https://www.kaggle.com/ciplab/real-and-fake-face-detection`

    Flickr-Faces-HQ Dataset (FFHQ)
        Total Images: 70,000
        Image/Class: ~7,000
        Features: High quality images, Only frontal faces, Duplicate-free
        Source:https://github.com/NVlabs/ffhq-dataset

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


