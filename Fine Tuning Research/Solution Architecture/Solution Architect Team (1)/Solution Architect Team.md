**Solution Architecture Team in Model Training Report**

1. **Create Solution Architecture (Week 1 and Week 3)**

**Objective**: Create Solution Architecture, including data flow diagram for AI-generated content detection and feedback generation, draw the system architecture and add data flow annotations.

`	`**Use case:**

(1). **AI Detection:** Automatically label student writing as AI or human-generated with confidence explanation (show as percentage)
(2). **Feedback Generation:** Automatically generate personalized feedback based on rubric and student response (as prompt)

**Solution Architecture:**

1. **AI Detection:**
- Input: Student Submission
- Modules: Fine-tuning LLM -> Evaluation
- Output: AI/Human/Hybric label + explanation
2. **Feedback Generation:**
- Input: Student Submission + Rubric
- Modules: Fine-tuning LLM -> Evaluation Criteria
- Output: Feedback Generation

**Instruction:**

1. Create data/model flow diagram for AI detection:

<img src="Fine Tuning Research/Solution Architecture/Solution Architect Team (1)/AI_Detection.png" alt="AI Detection" width="600"><br>

- **Data Flow:**
- Input: string/JSON → Output: JSON
- Fine-tuning LLM: using Gemini 1.5 model
- Evaluation: calculate confidence score for overall
- AI Detection: AI or Human or Hybric
- **Example:** 
- Input: prompt engineering
- Expected Output:

  {  

  "label": "AI",  

  "confidence": 0.72,  

  "explanation": "Unusual phrase repetition similar to GPT"

}

2. Design flow diagram for rubric-aligned feedback generation:

<img src="Fine Tuning Research/Solution Architecture/Solution Architect Team (1)/Feedback_generation.png" alt="Feedback Generation" width="600"><br>

- **Data Flow:**
- Input: string/JSON → Output: JSON
- Fine-tuning LLM: using Gemini 1.5 model
- Evaluation: based on evaluation criteria designed by evaluation team. In particularly,
    * Correctness (Accuracy & Helpfulness) -- 1 to 5
    * Clarity (Understandability & Communication) -- 1 to 5
    * Tone (Supportiveness & Constructiveness)-- 1 to 5
    * Actionability (Clear Next Steps & Implementation) -- 1 to 5
    * Coherence (Consistency & Flow) -- 1 to 5
    * Emotion (Emotional Intelligence & Sensitivity) -- 1 to 5

- Output: Text, String, or JSON
    * Criterion Scores (each 1–5)
    * Overall Rating (average or adjusted in exceptional cases)
    * Reasoning (justification for each score with references to text)

- **Example:** 
- Input: Student Submission and Rubric.
- Expected Output:

  {  

    Correctness: 4
    Clarity: 5
    Tone: 5
    Actionability: 4
    Coherence: 5
    Emotion: 5
  Overall Rating: 4.5
  Reasoning: Supportive, clear, but would benefit from specifying example types.

}


**Module Descriptions:**

1. Input: process dataset designed by data accuracy team. The dataset is json format with 5 separate dataset.
1. Fine-tuning LLM model: using Gemini 1.5 model to get API on Google AI.
1. Evaluation: design by evaluation team to follow researched criteria for evaluating model. In particularly,
  (1) AI detection: Repetition, Lexical Diversity, Sentence Structure Diversity, Grammar, Content Specificity, Emotional Expressiveness, Coherence & Natural Transitions, Pronouns, Contextual Appropriateness.
  (2) Feedback Generation: Evaluate the given feedback against these criteria:
    * Correctness (Accuracy & Helpfulness) -- 1 to 5
    * Clarity (Understandability & Communication) -- 1 to 5
    * Tone (Supportiveness & Constructiveness) -- 1 to 5
    * Actionability (Clear Next Steps & Implementation) -- 1 to 5
    * Coherence (Consistency & Flow) -- 1 to 5
    * Emotion (Emotional Intelligence & Sensitivity) -- 1 to 5
1. AI Detection: classify the prompt whether it is AI, Human, or Hybrid
1. Feedback Generation: generating feedback for prompting based on evaluation criteria.

