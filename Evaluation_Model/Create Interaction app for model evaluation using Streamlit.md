Create Interaction app for model evaluation using Streamlit

1. Overview

   The Model Evaluation Tool is an interactive web-based application developed with Streamlit. It enables user to upload datasets, evaluate classification or generative AI models, and visualize results in a user-friendly interface. The tool provides evaluation metrics, confusion matrix visualization, and qualitative feedback to help users understand model performance.

1. Features

- Upload the test datasets in JSON format or enter few-shot prompts for model inference
- Support for classification models to label whether it is Human or AI
- Metric calculation:
  - Accuracy
  - Precision
  - Recall
  - F1 Score
- Key Components:
1) Evaluate\_model.py
- Load JSON dataset
- Computes metrics
- Generates feedback (correct/incorrect with short explaination)
1) App.py
- Provides interactive UI in Streamlit
- Handles file upload & prompt input
- Displays metrics, confusion matrix, feedback

1. System Design

- Input: JSON file with a few-shot prompt
- Processing:
  - Load dataset 
  - Compare predictions with ground truth labels
  - Compute evaluation metrics using sklearn.metrics
  - Generate qualitative feedback for each sample
- Output:
  - Dataset preview table (prompts, labels, predictions)
  - Evaluation results (accuracy, precision, recall, f1-score)
  - Confusion matrix visualization
  - Feedback for each prompt
