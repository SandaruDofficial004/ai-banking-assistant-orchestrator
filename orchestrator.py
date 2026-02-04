def is_banking_question(question):
    keywords = ["bank", "account", "loan", "deposit", "transfer"]
    return any(word in question.lower() for word in keywords)


def ai_response(question):
    return f"AI response for: {question}"


def orchestrator(question):
    if is_banking_question(question):
        decision = "AI_CALLED"
        response = ai_response(question)
    else:
        decision = "REJECTED"
        response = "Sorry, I can only answer banking-related questions."

    log_decision(question, decision)
    return response


def log_decision(question, decision):
    with open("logs.txt", "a") as file:
        file.write(f"{question} --> {decision}\n")


if __name__ == "__main__":
    q = input("Ask a question: ")
    print(orchestrator(q))
