import openai
import os

# The prompt we will send to the AI
def build_prompt(ingredient):
    return f"""
You are an expert herbalist. Explain what {ingredient} is in simple terms.

Include:
- What it is
- How it’s commonly used
- Any safety notes
- Where it’s usually grown

Keep it short (under 150 words) and easy to understand.
"""

# This function sends the prompt to OpenAI and returns the result
def get_answer(ingredient):
    prompt = build_prompt(ingredient)
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

# Ask the user for an herb name
ingredient = input("Enter an herb (like Ashwagandha): ")
openai.api_key = os.getenv("OPENAI_API_KEY")

answer = get_answer(ingredient)
print("\nHere’s what we found:\n")
print(answer)
