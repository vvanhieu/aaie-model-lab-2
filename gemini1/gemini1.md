SIT378 – Project B

Project name: AAIE – LLM Prototyping and Training

-----

**Report: Implementing Role-Based Prompting with selected model (Gemini 1.5 flash model) for AI Detection & Feedback Generation**

-----

1. **Overview**

   The aim of this work was  test role-based prompting against gemini, and perform two tasks:

(1) AI Detection Task: Classify student submissions as Human, AI, or Hybrid and justify based on linguistic criteria.
(2) Feedback Generation Task: Generate structured academic feedback scored across six evaluation dimensions.

The experiment was conducted with a set of test prompts and student-like submissions, focusing on academic integrity evaluation and supportive academic assessment.

2. **Methodology:**

- Model Used: Gemini 1.5 Flash (via Google AI Studio).
- Domain Focus: Academic Integrity, Education, and Environmental Science.
- Evaluation Strategy: Each prompt was submitted to the model. The generated outputs were analyzed along two dimensions:
a) AI Detection Quality: clarity of evaluation, reasoning, and recommendations for further investigation.
b) Feedback Quality: clarity, rubric alignment, and actionability of suggestions.

   a. AI Detection Criteria

- The model's classifications (Human / AI / Hybrid) were checked against markers such as:
- Repetition
- Lexical Diversity
- Sentence Structure Diversity
- Grammar
- Content Specificity
- Emotional Expressiveness
- Coherence & Natural Transitions
- Pronouns & Contextual Appropriateness
- Output Assessment: Each prediction was marked Correct or Incorrect and given a short explanation with confidence score in percentage.

  b. Feedback Evaluation Criteria:

- Feedback quality was scored on a 1–5 scale using six dimensions:
- Correctness – accurate, helpful
- Clarity – easy to understand
- Tone – supportive, constructive
- Actionability – clear next steps
- Coherence – logical flow
- Emotion – empathetic, sensitive
- Output Assessment: Each feedback was scored across criteria, averaged, and explained briefly.

3. **Implementation**

a. *Environment Set-up:*

- Selected Model: Gemini 1.5 flash

- Create Jsonl dataset format: the five designated training datasets


b. *Role-Based Prompting:*

1) **Role 1: Academic Integrity Evaluator (AI Detection):**
- Classify label the submission whether it is Human, AI, or Hybrid
- Rational: provide evidences, the reason such as grammar, cites, or lack of research.
- Explanation: provide full detail such as what student have and what they need to improve
- Flags: summary the key points (main keys)

2) **Role 2: Supportive Academic Assessor (Feedback Generation):**
- Score submission against 6 criteria (Correctness, Clarity, Tone, Actionability, Coherence, Emotion).
- Compute Overall Rating (average): show the rating from 1 to 5, such as excellent, good, average, need improvement, and poor
- Provide feedback text and reasoning for each score.

c. *Input Submission*
- Five training datasets

4. **The Result**

   1. *AI Detection Output:*

      **AI Detection Output 1:**  
      
         Domain: Teaching
         Assignment Prompt: Examine current research on early literacy development and evaluate evidence-based approaches for supporting pre-reading skills in diverse learners aged 3 to 6 years.

         --- Submission 1 ---
         Label: AI
         Text (preview): Current research on early literacy development highlights the foundational role of phonological awareness, vocabulary acquisition, and print knowledge...

         --- Submission 2 ---
         Label: AI
         Text (preview): Early literacy development involves acquiring key skills such as phonological awareness, vocabulary, and an understanding of print, which typically em...

         --- Submission 3 ---
         Label: Human
         Text (preview): Early literacy development is such a critical phase in a child's life, especially between the ages of 3 and 6, where so much foundational learning tak...

         --- Submission 4 ---
         Label: Human
         Text (preview): Learning to read doesn't just start when a child enters school—early literacy development begins much earlier, especially between the ages of 3 and 6....

         --- Submission 5 ---
         Label: Hybrid
         Text (preview): Early literacy development is a critical phase for children aged between 3 and 6. During this foundational period, children typically begin developing...

         --- Submission 6 ---
         Label: Hybrid
         Text (preview): Literacy development in children does not need to begin with school age. Indeed, key skills such as phonological awareness, vocabulary, and an underst...


         === Processing Dataset: dataset/it 1.json ===
         Domain: Information Technology
         Assignment Prompt: In a few sentences, examine the role of Artificial Intelligence in modern cybersecurity, providing examples of its applications and potential risks.

         --- Submission 1 ---
         Label: AI
         Text (preview): Artificial Intelligence plays a pivotal role in modern cybersecurity by automating threat detection, enhancing incident response, and reducing false p...

         --- Submission 2 ---
         Label: AI
         Text (preview): AI-based cybersecurity solutions such as behavioral analytics and automated intrusion detection systems have allowed organizations to proactively dete...

         --- Submission 3 ---
         Label: Human
         Text (preview): Last year, my company faced a targeted phishing campaign. At the time, we were testing a new AI-based email filter. It actually flagged several emails...

         --- Submission 4 ---
         Label: Human
         Text (preview): As a junior security analyst, I used to spend hours going through alerts manually. Once we integrated an AI-powered tool into our workflow, it cut our...

         --- Submission 5 ---
         Label: Hybrid
         Text (preview): We used AI to monitor user activity across our cloud environment. While the algorithm caught some abnormal logins, it also raised false alarms that co...

         --- Submission 6 ---
         Label: Hybrid
         Text (preview): We recently ran a red team-blue team exercise. Our AI tools were excellent at identifying command-and-control traffic, but when it came to lateral mov...


         === Processing Dataset: dataset/accounting 1.json ===
         Domain: Accounting
         Assignment Prompt: Analyze the impact of blockchain technology on traditional accounting practices, including auditing and financial reporting.

         --- Submission 1 ---
         Label: AI
         Text (preview): Blockchain technology, defined by its decentralization, immutability, and transparency, is transforming traditional accounting practices, particularly...

         --- Submission 2 ---
         Label: AI
         Text (preview): Blockchain technology, defined by its decentralization, immutability, and transparency, is revolutionizing traditional accounting practices, particula...

         --- Submission 3 ---
         Label: Human
         Text (preview): As a business student fascinated by tech, I see blockchain revolutionizing traditional accounting. Its decentralized, tamper-proof ledger could transf...

         --- Submission 4 ---
         Label: Human
         Text (preview): As a business student fascinated by tech, I see blockchain reshaping accounting, auditing, and financial reporting, though it’s not without challenges...

         --- Submission 5 ---
         Label: Hybrid
         Text (preview): Blockchain technology significantly reshapes traditional accounting practices, including auditing and financial reporting, by enhancing transparency, ...

         --- Submission 6 ---
         Label: Hybrid
         Text (preview): Blockchain technology significantly transforms traditional accounting practices, enhancing efficiency, transparency, and security. Its decentralized, ...


         === Processing Dataset: dataset/psychology 1.json ===
         Domain: Psychology
         Assignment Prompt: Critically evaluate the role of cognitive biases in human decision-making. Select at least three cognitive biases (e.g., confirmation bias, anchoring, availability heuristic) and explain how they influence decision-making in real-world scenarios (e.g., healthcare, law, relationships, consumer behavior). Discuss the psychological theories behind them and explore how awareness or mitigation strategies can improve judgment.

         --- Submission 1 ---
         Label: AI
         Text (preview): Cognitive biases significantly influence human decision-making, often leading to systematic errors in judgment. For instance, confirmation bias leads ...

         --- Submission 2 ---
         Label: AI
         Text (preview): Cognitive biases play a crucial role in shaping decision-making, often leading to irrational or suboptimal choices. Confirmation bias affects decision...

         --- Submission 3 ---
         Label: Human
         Text (preview): Cognitive biases have a big influence on how we make decisions, often without us even realizing it. For instance, confirmation bias makes us focus on ...

         --- Submission 4 ---
         Label: Human
         Text (preview): Cognitive biases shape how we make decisions by twisting our judgment in ways we're often unaware of. For example, confirmation bias makes us seek out...

         --- Submission 5 ---
         Label: Hybrid
         Text (preview): Cognitive biases, such as confirmation bias, anchoring, and the availability heuristic, will be able to shape human decision-making by distorting perc...

         --- Submission 6 ---
         Label: Hybrid
         Text (preview): Cognitive biases, such as confirmation bias (Nickerson, 1998), anchoring (Tversky & Kahneman, 1974), and the availability heuristic, affect decision-m...


         === Processing Dataset: dataset/engineering 1.json ===
         Domain: Manufacturing Engineering
         Assignment Prompt: Describe how a manufacturing engineer sets up a basic production line for a new consumer product. Explain the steps taken from design to assembly, including equipment layout, efficiency considerations, and safety.

         --- Submission 1 ---
         Label: AI
         Text (preview): To set up a basic production line for a new consumer product, a manufacturing engineer follows a structured, multi-phase process. It begins with desig...

         --- Submission 2 ---
         Label: AI
         Text (preview): A manufacturing engineer sets up a production line through a step-by-step approach that begins with understanding the final product's design. This inc...

         --- Submission 3 ---
         Label: Human
         Text (preview): When setting up a production line, a manufacturing engineer starts by looking at the product's design carefully. They figure out what parts are needed...

         --- Submission 4 ---
         Label: Human
         Text (preview): To set up a new production line, a manufacturing engineer first learns about the product they are going to build. They look at drawings and talk with ...

         --- Submission 5 ---
         Label: Hybrid
         Text (preview): The process of setting up a production line involves both technical planning and practical foresight. First, the manufacturing engineer reviews the pr...

         --- Submission 6 ---
         Label: Hybrid
         Text (preview): Setting up a basic production line combines detailed technical design with real-world testing and adaptation. After the product design is reviewed, th...

   2. *Feedback AI Generation Output:* 

      **Feedback Generation Output 1:**
      Evaluation Output:
         **Criterion Scores:**
         * Correctness: 3
         * Clarity: 4
         * Tone: 5
         * Actionability: 2
         * Coherence: 4]
         * Emotion: 5
         **Overall Rating：**k 3.8
         **Reasoning：**
         * **Correctness (3):** The feedback is accurate in identifying
         the essay's weaknesses: lack of specific examples and references.
         However, it's somewhat unhelpful as it only points out
         the problems without suggesting *which* specific examples would be beneficial or *what kind* of references are needed (e.g., peer-reviewed articles, government reports). More precise f
         eedback would improve the score.
         * **Clarity (4):** The feedback is to the assignment.
         easy to understand. The language is straightforward and the criticisms are concise. The points are easily identifiable and directly relate
         Phrases like "provides a good overview" offer positive reinforcement before pointing out areas for improvement. This c
         * **Actionability (2):** While the feedback identifies weaknesses, it's low on actionability.
         The student knows what needs improvement, but lacks guidance on *how* to improve. The feedback needs more specificity regarding the type and quality of examples and references needed. Suggesting specific resources or research strategies would significantly enhance the actio
         * **Coherence (4):** The feedback is coherent and flows logically. It directly addresses the assignment prompt and rubric criteria implicitly (although explicit mention would be better)
         The points made are consistent and interconnected.
         * **Emotion (5):** The feedback demonstrates high emotional intelligence and sensitivity. The positive opening ("This essay provides a good overview...") creates a supportive environmen t before delivering constructive criticism. The overall tone is encouraging, avoiding judgmental language. 
         
         To improve the feedback, the assessor could provide specific examples: "For instance, discussing the impact of rising sea levels on specific coastal communities, or citing data from the IPCC reports to support claims about temperature increases, would strengthen your argument." This would significantly increase the actionability and correctness scores.

      **Feedback Generation Output 2:**
      Evaluation Output:
         **Criterion Scores (each 1-5):**
         1. Correctness: 4
         2. Clarity: 5
         3. Tone: 5
         4. Actionability: 4
         5. Coherence: 5
         6. Emotion: 5
         **Overall Rating:** 4.5
         **Reasoning:**
         1. **Correctness (4):** The
         feedback is accurate in identifying a key weakness of the essay - the lack of examples. A good overview needs supporting evidence. However,
         it could be more helpful by specifying *what kind* of examples would strengthen the essay. For instance, it could suggest examples of specific climate change impacts, mitigation strategies, or scient
         This lack of specificity slightly diminishes the helpfulness.
         2. **Clarity (5):** The feedback is exceptionally clear and concise. The sentence structure is simple and direct, making the meaning immediately understandable. There is no ambiguity supportive phrasing
         is polite and avoids criticism.
         constructive. The phrase "good overview" acknowledges the positive aspects of the essay before pointing out the for improvement.
         **Actionability (4):** The feedback clearly points to a specific area needing improvement. The student knows they need to add examples. However, as mentioned in the Correctness sec
         more specific guidance on the *type* of examples needed would increase the actionability score. The student might struggle to identify suitable examples without further direction.
         **Coherence (5):** The feedback is entirely consistent and flows logically. The statement about the overview smoothly leads to the identified weakness. There are no contradictions o r inconsistencies.
         **Emotion
         (5):** The feedback demonstrates
         emotional intelligence and sensitivity. It avoids harsh language or judgmental tones. The positive opening ("good overview") creates a rece
         ptive atmosphere for receiving the constructive criticism.

1. **Observation**

- **Structured Output:** Each response contained clear sections (Detection Result, Confidence Level, Justification, Recommendations). The model reliably followed the role-based prompting.
- **AI Detection:**
- Output Structure (AI Detection):
- Result: Correct / Incorrect (based on comparison of label vs. prediction).
- Criteria-based Analysis: Detailed reasoning using the markers above.
- Confidence Level: Probability estimate (%) of correct classification.
- Correctly flagged AI-like phrasing and admissions of hybrid use.
- Provided probabilistic confidence levels.
- Recommended verification methods (plagiarism checks, stylistic analysis).
- **Feedback Generation:**
- Output Structure (Feedback Evaluation):
- Criterion Scores: Each scored 1–5.
- Overall Rating: Average of scores (or adjusted in edge cases).
- Reasoning: Written justification for each score with references to text.
- Rubric-aligned, constructive, supportive.
- Direct mapping to clarity, evidence, critical thinking, and writing quality.
- **Language and Style:**
- Professional, coherent, and grammatically sound.
- Tone supportive, avoiding harsh or accusatory framing.


