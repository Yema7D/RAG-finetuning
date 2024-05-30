def get_questions_from_content_prompt_mistral(context, nbr_questions=40, language="english"):
        return f"""<s><<SYS>>
You are a highly detailed-oriented Assistant.
Your task is to Generation of educational mini-challenges for a video game  and context-specific questions based on the provided text and your knowledge. These questions should be designed to explore every aspect of the context in depth.

</s><</SYS>>

Context:
```
{context}
```

User : Based on the above context, please generate a list of exactly {nbr_questions} distinct and contextually relevant questions. Ensure that these questions comprehensively cover the provided context.
Don't never never ask general or vague questions.
Always add "What", "Who", "When", "Where","How","Generate" when possible.
Do not end the question with phrase like "in the context" or "in the given context" or "dans le contexte" or similar.
Give a list of exactly {nbr_questions} questions.
Give me the questions in {language} language.
Assistant: """


def get_answer_from_content_prompt_mistral(context, question, language="english"):
        print("question", question)
        return f"""<s><<SYS>>
You are a highly detail-oriented Assistant tasked with generating professional and detailed answers. Your responses should be based strictly on the provided context and in the specified language.
</s><</SYS>>

Context:

{context}


User: Please answer the following question in {language}: "{question}".
If the context does not provide enough information, respond with you knowledge

[Reminder: The response must be in {language}.]

Assistant: """


def get_questions_from_content(context, nbr_questions=30, model="mistral", language="english"):
        return get_questions_from_content_prompt_mistral(context, nbr_questions, language)


def get_answer_question_from_content(context, question, model="mistral"):
        return get_answer_from_content_prompt_mistral(context, question, language="english")