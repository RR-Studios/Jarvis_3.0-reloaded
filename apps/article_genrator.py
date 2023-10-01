import openai
import pyttsx3

# Set your OpenAI API key
api_key = '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'

def generate_article(prompt):
    openai.api_key = api_key

    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=300,  # Adjust the length of the generated article as needed
        stop=None,  # You can specify stop words if needed
        temperature=0.7,  # Adjust the temperature to control randomness
    )

    article = response.choices[0].text
    return article

if __name__ == "__main__":
    prompt = "Generate an article about artificial intelligence."
    article = generate_article(prompt)

    with open("generated_article.txt", "w") as file:
        file.write(article)
