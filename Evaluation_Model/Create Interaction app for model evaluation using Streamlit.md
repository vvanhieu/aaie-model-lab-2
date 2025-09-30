Create Interaction app for model evaluation using Streamlit

1. Overview

   The Model Evaluation Tool is an interactive web-based application developed with Streamlit. It enables user to upload datasets, evaluate classification or generative AI models, and visualize results in a user-friendly interface. The tool provides evaluation metrics, confusion matrix visualization, and qualitative feedback to help users understand model performance.

2. Features

- Upload the test datasets in JSON format or enter few-shot prompts for model inference
- Support for classification models to label whether it is Human or AI
- Metric calculation:
  - Accuracy
  - Precision
  - Recall
  - F1 Score
- Key Components:
a) Evaluate\_model.py
- Load JSON dataset
- Computes metrics
- Generates feedback (correct/incorrect with short explaination)
b) App.py
- Provides interactive UI in Streamlit
- Handles file upload & prompt input
- Displays metrics, confusion matrix, feedback

3. System Design

- Input: JSON file with a few-shot prompt or the text writting
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

4. Streamlit Output:

*1. Model Process and Evaluation Output:*


<img src="modelprocess_evaluation_output.png" alt="Model Process and Evaluation Output" width="600"><br>

* Input Samples – A preview of the text prompts, their correct labels (Human or AI), and the model's predictions.

* Evaluation Metrics – Measures such as accuracy, precision, recall, and F1 score, which describe how well the model performed.

* Confusion Matrix – A simple table and heatmap that visualize where the model made correct predictions and where it made mistakes.

*2. Feedback Generation Output:*

<img src="feedback_generation_output.png" alt="Feedback Generation Output" width="600"><br>

This part of the system evaluates not only whether predictions were correct but also the quality of the feedback given by the model. It uses six dimensions (each scored from 1–5):
* Correctness – Was the prediction and reasoning accurate?
* Clarity – Was the explanation easy to understand?
* Tone – Was the feedback professional and constructive?
* Actionability – Did it provide clear next steps or improvements?
* Coherence – Was the explanation logically structured?
* Emotion – Was the response empathetic or human-like in sensitivity?