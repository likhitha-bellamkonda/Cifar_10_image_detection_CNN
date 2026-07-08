# CIFAR-10 Image Classification using CNN

## 📌 Project Overview

This project implements an image classification model using a **Convolutional Neural Network (CNN)** trained on the **CIFAR-10** dataset. The model learns to classify images into one of ten object categories using deep learning techniques with TensorFlow and Keras.

---

## 🎯 Objective

The goal of this project is to build a deep learning model capable of accurately classifying images from the CIFAR-10 dataset into their respective categories.

---

## 📂 Dataset

The CIFAR-10 dataset contains **60,000 color images** of size **32 × 32 pixels**.

* Training Images: 50,000
* Test Images: 10,000
* Number of Classes: 10

### Classes

* Airplane
* Automobile
* Bird
* Cat
* Deer
* Dog
* Frog
* Horse
* Ship
* Truck

The dataset is directly loaded from TensorFlow:

```python
from tensorflow.keras.datasets import cifar10

(X_train, y_train), (X_test, y_test) = cifar10.load_data()
```

---

## 🛠 Technologies Used

* Python
* TensorFlow
* Keras
* NumPy
* Matplotlib
* Scikit-learn

---

## 🔄 Project Workflow

1. Load the CIFAR-10 dataset.
2. Normalize pixel values.
3. Convert labels into categorical format.
4. Build a Convolutional Neural Network.
5. Train the model.
6. Evaluate model performance.
7. Predict image classes.
8. Visualize predictions.

---

## 🧠 CNN Architecture

The model consists of:

* Convolution Layer (ReLU)
* Max Pooling Layer
* Convolution Layer
* Max Pooling Layer
* Flatten Layer
* Dense Hidden Layer
* Dropout Layer
* Output Layer (Softmax)

---

## 📊 Model Evaluation

Evaluation metrics include:

* Training Accuracy
* Validation Accuracy
* Test Accuracy
* Loss
* Prediction on unseen images

Example:

```
Test Loss : 0.89%
Test Accuracy : 70.06%
```

---

## 🚀 How to Run

### Clone the repository

```bash
git clone https://github.com/your-username/cifar10-image-classification.git
```

### Move into the project

```bash
cd cifar10-image-classification
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the project

```bash
python cifar10_cnn.py
```

Or, if using Jupyter Notebook:

```bash
jupyter notebook
```

Open the notebook and run all cells.

---

## 📁 Project Structure

```
CIFAR10-Image-Classification/
│
├── cifar10_cnn.ipynb
├── model.keras
├── requirements.txt
├── README.md
├── images/
└── results/
```

---

## 📈 Future Improvements

* Apply Data Augmentation
* Use Transfer Learning (ResNet50, VGG16, MobileNet)
* Hyperparameter Tuning
* Deploy using Streamlit or Flask
* Improve accuracy with Batch Normalization

---

## 🎓 Learning Outcomes

Through this project, I gained practical experience in:

* Image preprocessing
* Convolutional Neural Networks (CNNs)
* TensorFlow and Keras
* Model training and evaluation
* Deep learning for computer vision
* Image classification techniques

---

## 👩‍💻 Author

**Bellamkonda Likhitha Satya Naga Lakshmi**

* B.Sc. Data Science Graduate
* Aspiring Data Scientist / AI Engineer
* Skilled in Python, Machine Learning, Deep Learning, SQL, Power BI, and Generative AI

---

## ⭐ If you found this project helpful, consider giving it a star on GitHub!
