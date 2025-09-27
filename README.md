# LeafSense - Explainable Soybean Leaf Disease Detection

![GitHub top language](https://img.shields.io/github/languages/top/your-username/your-repo?style=for-the-badge&color=blue)
![License](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)

This project presents a deep learning approach for the early and accurate detection of soybean leaf diseases. Soybean leaf diseases pose a significant threat to agricultural productivity, especially in regions like Maharashtra, India, where timely identification is crucial. A custom-built **Convolutional Neural Network (CNN)** is implemented in TensorFlow and Keras to classify various diseases from leaf images.

A key feature of this project is its focus on model interpretability. By applying **Grad-CAM (Gradient-weighted Class Activation Mapping)** and **Grad-CAM++**, we can visualize the regions of the leaf image that our model focuses on when making a prediction. This helps in understanding the model's decision-making process and building trust in its diagnostic capabilities, which is crucial for real-world agricultural applications.

![Potassium Deficiency with Grad-CAM](https://i.imgur.com/8a6B8Jc.png)
[cite_start]*Figure: Original image of a soybean leaf with potassium deficiency (left) and its Grad-CAM++ heatmap (right), showing the model focusing on the discolored regions[cite: 263, 260].*

***

## Features
- **Custom CNN Architecture:** A lightweight and effective CNN model designed specifically for this classification task.
- **Robust Data Augmentation:** Utilizes techniques like random flipping, rotation, zooming, and contrast adjustments to improve model generalization and prevent overfitting.
- **Separate Training & Inference Models:** A clean implementation that uses a separate model for inference, ensuring that Grad-CAM visualizations are generated on original, non-augmented images.
- **Detailed Performance Evaluation:** The model's performance is thoroughly evaluated using metrics such as Accuracy, Precision, Recall, F1-Score, and a Confusion Matrix.
- **Model Interpretability:** Implements Grad-CAM to provide visual explanations for the model's predictions, making the "black box" more transparent.

***

## Dataset
The model was trained on a comprehensive dataset of soybean leaf images [https://datadryad.org/dataset/doi:10.5061/dryad.41ns1rnj3]. We have considered 4 classes,
- Healthy
- Backerial Blight
- Frogeye leaf spot
- Potassium deficiency

***

## Methodology

### 1. Data Preprocessing & Augmentation
The dataset is loaded and partitioned into training (80%), validation (10%), and testing (10%) sets. The training data goes through a series of on-the-fly augmentations to create a more robust mode. All images are standardized to a size of $256\times256$ pixels to align with model input requirements.

### 2. Custom CNN Architecture
The designed model follows a classic CNN structure, progressively extracting more complex features from the images. The architecture has been visualized in the below image.
<img src = "/images/model_arch.png">

| Layer Type | Filters / Units | Activation | Notes |
| :--- | :--- | :--- | :--- |
| **Input** | - | - | Image size: `(256, 256, 3)` |
| **Conv Block 1** | 32 | ReLU | Two Conv2D layers followed by MaxPooling |
| **Conv Block 2** | 64 | ReLU | One Conv2D layer followed by MaxPooling |
| **Conv Block 3** | 128 | ReLU | One Conv2D layer followed by MaxPooling |
| **Classifier** | 128 | ReLU | Flatten -> Dense -> Dropout (0.35) |
| **Output** | n_classes | Softmax | Final classification layer |

### 3. Training & Inference
A key aspect of this project is the use of two distinct models:
- **Training Model:** Includes the `data_augmentation` layers. This model is used exclusively for training.
- **Inference Model:** The learned weights from the training model are transferred to an identical architecture *without* the augmentation layers. This ensures that predictions and Grad-CAM visualizations are clean and based on the original input image.

***

## Results
The model achieves excellent performance on the test set, demonstrating its effectiveness in classifying soybean diseases.

- **Precision:** `0.9778` 
- **Recall:** `0.9774` 
- **F1-Score:** `0.9775`

### Confusion Matrix
The confusion matrix below illustrates the model's classification performance across all disease categories on the test set.

<img src = "/images/confusion_matrix.svg">
