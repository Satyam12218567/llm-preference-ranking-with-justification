# compare_and_justify.py

def load_response(file_path):
    with open(file_path, 'r') as f:
        return f.read().strip()

def evaluate_responses(prompt, a, b):
    print("PROMPT:")
    print(prompt)
    print("\n--- RESPONSE A ---")
    print(a)
    print("\n--- RESPONSE B ---")
    print(b)
    print("\n--- Evaluation ---")
    preferred = input("Which response do you prefer? (A/B): ").strip().upper()
    justification = input("Why do you prefer this response? Provide justification: ")
    print(f"\nPreferred: Response {preferred}")
    print(f"Justification: {justification}")

if __name__ == "__main__":
    prompt = load_response("prompt.txt")
    response_a = load_response("response_a.txt")
    response_b = load_response("response_b.txt")
    evaluate_responses(prompt, response_a, response_b)
