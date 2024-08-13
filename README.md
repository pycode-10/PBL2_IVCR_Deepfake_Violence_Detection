# Deepfake and Violence Detection (IVCR)

The aim of this project is to detect deepfake and violent content using advanced machine learning and deep learning techniques. The repository includes components for training a detection model, deploying it via an API, and providing a user interface through a React application.

## Project Overview

### Training Notebooks

- **`Deepfake_Detection.ipynb`**: Contains the code for training the deepfake detection model. This includes data preprocessing, model architecture setup, and training procedures.

- **`Violence_Detection.ipynb`**: Provides code for evaluating the performance of the trained model, including metrics calculation, performance analysis, and testing.

### API Folder

- **`API/`**: Includes FastAPI code for serving the trained deepfake detection model. It contains:
  - **`apicode.py`**: Defines the API endpoints for model interaction.

### Trained Model
- **`deepfake_6.keras`**: This file contains the trained deepfake detection model.

### Dataset Preparation

- **`datasetcode.py`**: This Python script is responsible for resizing all the images in the dataset to the required dimensions for model training and evaluation. 

### Frontend Website Folder

- **`Frontend_Website_UI/`**: Contains the React-based web application that provides a user interface for the model. It includes:
  - **`public/`**: Static files and assets used by the React application.
  - **`src/`**: Source code for the React application, including components, hooks, and styles.
  - **`package.json`**: Manages Node.js dependencies and scripts.
  - **`package-lock.json`**: Ensures consistent dependency installations.

