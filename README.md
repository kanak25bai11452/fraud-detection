# Fraud Detection System using Machine Learning

## Project Description

This project is a simple Machine Learning-based Fraud Detection System that classifies a transaction as **Fraudulent** or **Legitimate** based on the transaction amount.

The system uses a **Logistic Regression** model trained on sample data. It demonstrates the basic workflow of Machine Learning including training, saving the model, and making predictions.

The project runs using a **Command Line Interface (CLI)** and does not require any graphical interface.


## Requirements

Make sure the following are installed on your system:

* Python (version 3.7 or above)
* pip (Python package manager)


## Dependencies Installation

Open Command Prompt / Terminal and run the following commands:

pip install pandas
pip install scikit-learn


## Setup Instructions

1. Download or clone this repository to your system
2. Open terminal (Command Prompt / PowerShell / VS Code Terminal)
3. Navigate to the project folder: cd fraud-detection

Download → Open Terminal → cd fraud-detection → install → run

Make sure the following files are present in the folder:
* train.py
* main.py
* README.md

(Note: model.pkl will be generated after running the training script if not already present)


## Configuration Steps

No additional configuration is required.

The trained model file (`model.pkl`) will be automatically created after running the training script.


##  Execution Steps

### Step 1: Train the Model

Run the following command in the terminal:

python train.py

This will:

* Train the Machine Learning model
* Generate the file `model.pkl`


### Step 2: Run the Fraud Detection System

Run:

python main.py


### Step 3: Provide Input

Enter a transaction amount when prompted.

Example:
Enter transaction amount: 500


## Sample Output

Input:
500
Output:
Legitimate Transaction

Input:
20000
Output:
Fraudulent Transaction


## Project Structure

fraud-detection/
│
├── train.py        → Script for training the model
├── main.py         → Script for prediction
├── model.pkl       → Saved trained model
├── README.md       → Project documentation


## Important Notes

* The project runs completely using the command line (CLI)
* No GUI is required
* Always run `train.py` before `main.py` if `model.pkl` is not present
* The file `model.pkl` is a binary file and cannot be opened manually


## Future Improvements

* Use real-world datasets
* Add more features (time, location, user behavior)
* Improve model accuracy
* Develop a web or GUI-based application


## Author
KANAK GUPTA
25BAI11452
