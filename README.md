# Sign Language Recognition
By Ben Suffin, Bo Zhang, and Tyler Reece
CS542 Final Project
Boston University

## Repository Overview
### Models
* alphabet_model_5000_CNN.h5 
* word_model_1000_CNN.h5
* SVMModel.ipynb
### Code
* generateDataset.py contains code for recording images for use in model creation, as well as preprocessing images. Capture and preprocess mode can be accessed by running the script with the command line argument "capture" and "preprocess" respectively
* signLanguageRecognition.py contains code for loading a model in .h5 format and classifying signs in real time. The model prints the predicted text to the screen
### Data
* /alphabet contains a dataset of letters A-Z, excluding J and Z (as those require movement). Each of the 24 classes has 5000 images
* /alphabet_preprocessed contains preprocessed images (cropped, shrunk, and grayscale) of the alphabet dataset, ready for use in model creation
* /words contains a dataset of several simple, static words in sign language, with 1000 images per class
* /words_preprocessed contains preprocessed images (cropped, shrunk, and grayscale of the words dataset
### Demo
* .mp4 files demonstrating real-time model classification of alphabet and word sign language
### Paper
*  .pdf file of the final paper 
* .pdf file of presentation slide given on 6/29
### Others
* See requirements.txt file for necessary modules and versions used in this project# CS542-Final-Project