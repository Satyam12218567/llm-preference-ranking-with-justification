# LLM Preference Ranking with Justification

This project is a realistic simulation of my work under **Scale AI (Outlier)**, where I contributed to training and refining Large Language Models (LLMs) via **OpenAI’s internal Feather platform**.

The objective of this simulation is to replicate the **pairwise ranking + justification workflow** — a critical step in aligning LLMs to human intent through Reinforcement Learning with Human Feedback (RLHF).

---

## 🧠 Real-World Context

- Worked as an LLM evaluator under **Outlier**, contributing to **OpenAI’s RLHF pipelines**
- Performed **preference ranking tasks** using detailed rubrics: instruction-following, helpfulness, coherence, factuality, tone, and harmlessness
- Gave **concise and analytical justifications** for model performance
- Contributed to **STEM-focused tasks**, evaluating model responses for accuracy and clarity in scientific domains

---

## 📌 What This Project Simulates

This repo demonstrates a simplified version of the actual task:

- Presents a real-like prompt (e.g., explain entropy in thermodynamics)
- Loads two LLM-generated responses
- Asks the evaluator to:
  - Choose the better one (A or B)
  - Provide a **justification**
- Prints the evaluation result

---

## 🧪 Sample Evaluation Flow

```bash
$ python compare_and_justify.py

PROMPT:
Explain the concept of entropy in thermodynamics to a high school student.

--- RESPONSE A ---
Entropy is a measure of disorder or randomness in a system...

--- RESPONSE B ---
Entropy can be defined as something that always increases...

--- Evaluation ---
Which response do you prefer? (A/B): A
Why do you prefer this response? Provide justification: Response A follows the instruction more completely and uses accurate scientific terms.

Preferred: Response A
Justification: Response A follows the instruction more completely and uses accurate scientific terms.
```

---

## 🔧 Files Included

| File | Description |
|------|-------------|
| `compare_and_justify.py` | Main script to simulate human evaluation |
| `prompt.txt` | A high-school level STEM prompt |
| `response_a.txt` | First model response |
| `response_b.txt` | Second model response |
| `README.md` | Project documentation |

---

## 🚀 Future Scope

- Integrate OpenAI API to automate evaluation pipeline
- Apply rubric scoring to responses instead of simple A/B
- Add multiple prompt categories (STEM, ethics, logic)

---

## 👨‍💻 Author

**Satyam Raj**  
LLM Trainer | AI Evaluator  
- Annotator at Outlier (Scale AI)  
- Contributor to OpenAI’s internal training via Feather  
- Experienced in STEM-focused LLM evaluation  
- Email: rsatyam950@gmail.com
