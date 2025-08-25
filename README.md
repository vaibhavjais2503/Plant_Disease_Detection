## AgriGuard - Crop Disease Detection
AgriGuard is an advanced machine learning project designed to classify various crops and their diseases using Convolutional Neural Networks (CNN). This project aims to assist farmers and agricultural experts in identifying plant diseases at an early stage, thereby improving crop management and yield.
AgriGuard utilizes a CNN-based approach to accurately classify 38 different types of crop diseases. The project processes over 100,000 images to identify diseases, enabling early intervention and effective treatment.

## Dataset
The dataset used in this project includes:

##Training Images: 79,000
Validation Images: 17,000
Testing Images: 20% of the total dataset
Subcategories: 38 types of crops and their diseases
The dataset covers a wide range of crop diseases such as Apple Scab, Black Rot, Cedar Apple Rust, and more.

## Model Architecture
The model architecture is built on a 4-layer CNN with the following details:

Layer 1: Convolutional layer with 32 filters
Layer 2: Convolutional layer with 64 filters
Layer 3: Convolutional layer with 128 filters
Layer 4: Fully connected layer
Techniques: Gradient clipping, adaptive learning rate optimizers, data augmentation
The model processes 32 images per batch, ensuring efficient training and validation.

## Technologies Used
Python
TensorFlow
Keras
Convolutional Neural Networks (CNN)
Image Processing
Data Augmentation
Machine Learning
Deep Learning
Results
Validation Accuracy: 92%
Error Rate Reduction: Achieved through data augmentation and precise parameter tuning
Installation
To set up the project locally, follow these steps:

## Clone the repository:

git clone https://github.com/yourusername/AgriGuard.git
cd AgriGuard
Create and activate a virtual environment:

python3 -m venv venv
source venv/bin/activate
Install the required dependencies:

pip install -r requirements.txt

## Usage
Prepare the dataset: Ensure the dataset is structured correctly and placed in the appropriate directory.
Train the model: Run the training script to train the CNN model on the dataset.

python train.py
Evaluate the model: Use the evaluation script to test the model's accuracy and performance.
bash
Copy code
python evaluate.py
Contributing
Contributions are welcome! Please read the contributing guidelines for more information.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
