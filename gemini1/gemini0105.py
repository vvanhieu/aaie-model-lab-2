import json
import google.generativeai as genai
from pathlib import Path

# ---------------------------
# Configure Gemini
# ---------------------------
genai.configure(api_key="your API")
MODEL = "gemini-1.5-flash"

# ---------------------------
# Feedback Criteria
# ---------------------------
FEEDBACK_CRITERIA = """
You are an evaluator. Evaluate the given submission against these criteria:

1. Correctness (Accuracy & Helpfulness) -- 1 to 5
2. Clarity (Understandability & Communication) -- 1 to 5
3. Tone (Supportiveness & Constructiveness) -- 1 to 5
4. Actionability (Clear Next Steps & Implementation) -- 1 to 5
5. Coherence (Consistency & Flow) -- 1 to 5
6. Emotion (Emotional Intelligence & Sensitivity) -- 1 to 5

Output structure:
- Criterion Scores (each 1–5)
- Overall Rating (average or adjusted in exceptional cases)
- Reasoning (justification for each score with references to text)
"""

# ---------------------------
# AI Detection Criteria (generic)
# ---------------------------
AI_DETECTION_CRITERIA = """
You are an evaluator. Compare model prediction with actual label using these criteria:

Repetition, Lexical Diversity, Sentence Structure Diversity, Grammar, Content Specificity,
Emotional Expressiveness, Coherence & Natural Transitions, Pronouns, Contextual Appropriateness.

Input structure:
- Text: input text
- Label: actual label (AI/Human/Hybrid)
- Prediction: model prediction (AI/Human/Hybrid)

Output structure:
- Result: Correct / Incorrect
- Criteria-based analysis (reasoning under the criteria)
- Confidence_level: percentage estimate
"""

# ---------------------------
# Utility function for Gemini
# ---------------------------
def run_gemini(task_text, rubric_text):
    """Send task + rubric to Gemini"""
    model = genai.GenerativeModel(MODEL)
    full_prompt = f"{task_text}\n\nEvaluation Criteria:\n{rubric_text}"
    response = model.generate_content(full_prompt)
    return response.text if response else "⚠️ No response from Gemini."

# ---------------------------
# Process one dataset
# ---------------------------
def process_dataset(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    domain = data.get("domain", "Unknown Domain")
    prompt = data.get("prompt", "N/A")
    submissions = data.get("submissions", [])

    print(f"\n=== Processing Dataset: {file_path} ===")
    print(f"Domain: {domain}")
    print(f"Assignment Prompt: {prompt}\n")

    if not submissions:
        print("⚠️ No submissions found in this dataset.")
        return

    feedback_results = []

    for i, submission in enumerate(submissions, start=1):
        text = submission.get("final_submission", "").strip()
        label = submission.get("label_type", "Unknown")

        if not text:
            print(f"⚠️ Submission {i} has no text, skipping.")
            continue

        print(f"--- Submission {i} ---")
        print(f"Label: {label}")
        print(f"Text (preview): {text[:150]}...\n")  # show only first 150 chars

        # ---------------------------
        # Generate feedback using FEEDBACK_CRITERIA
        # ---------------------------
        feedback_prompt = f"Submission:\n{text}"
        feedback_result = run_gemini(feedback_prompt, FEEDBACK_CRITERIA)
        print("Generated Feedback (scored):\n", feedback_result[:500], "...\n")  # preview first 500 chars

        # ---------------------------
        # AI detection evaluation (optional)
        # ---------------------------
        ai_eval_prompt = f"Text: {text}\nLabel: {label}\nPrediction: {label}"  # using label as placeholder
        ai_eval_result = run_gemini(ai_eval_prompt, AI_DETECTION_CRITERIA)
        print("AI Detection Evaluation:\n", ai_eval_result[:500], "...\n")  # preview first 500 chars

        # Save results
        feedback_results.append({
            "submission_index": i,
            "label": label,
            "text": text,
            "feedback_scored": feedback_result,
            "ai_evaluation": ai_eval_result
        })

    # Optionally, save feedback results to JSON
    output_path = Path(file_path).stem + "_feedback_scored.json"
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(feedback_results, f, indent=2, ensure_ascii=False)
    print(f"Feedback results saved to {output_path}\n")

# ---------------------------
# Run on all datasets
# ---------------------------
json_files = [
    "dataset/accounting 1.json",
    "dataset/engineering 1.json",
    "dataset/teaching 1.json",
    "dataset/it 1.json",
    "dataset/psychology 1.json"
]

for file in json_files:
    process_dataset(file)
