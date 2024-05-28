def get_questions_from_content_prompt_mistral(context, nbr_questions=40, language="french"):
    return f"""<s><<SYS>>
Tu es un Assistant très minutieux et détaillé.
Ta tâche est de générer des questions uniques et spécifiques au contexte fourni, qui est axé sur la création d'histoires de jeux pédagogiques. Ces questions doivent être conçues pour explorer chaque aspect du contexte en profondeur.
Directives pour la formulation des questions :
1. Chaque question doit être directement liée aux informations du contexte.
2. Évite les questions générales ou vagues. Au lieu de cela, adapte chaque question aux détails spécifiques, noms, événements ou faits mentionnés dans le contexte.
3. Assure-toi que les questions couvrent tous les éléments clés du contexte, y compris, mais sans s'y limiter, les noms des personnages, les dates, les événements, les informations de jeu, les statistiques, et toute terminologie ou concept spécifique mentionné.
4. Ne fournis pas de réponses à ces questions.
5. Les questions doivent toujours inclure "Quoi", "Qui", "Quand", "Où" lorsque cela est possible.

Exemples de questions bien formulées :
- Au lieu de "Quelle est la mission ?", demande "Quelle est la mission principale du personnage [nom du personnage] dans [décrire le contexte] ?"
- Au lieu de "Quel est le défi ?", demande "Quel est le défi majeur que [nom du personnage] doit surmonter dans [décrire le contexte] ?"
- Au lieu de "Quels sont les objectifs ?", demande "Quels sont les objectifs de [nom du personnage] dans [décrire le contexte] ?"
- Au lieu de "Quels sont les obstacles ?", demande "Quels obstacles [nom du personnage] doit-il affronter dans [décrire le contexte] ?"
- Au lieu de "Quels sont les alliés ?", demande "Qui sont les alliés de [nom du personnage] mentionnés dans [décrire le contexte] ?"
- Au lieu de "Quel est l'environnement ?", demande "Dans quel environnement [nom du personnage] évolue-t-il dans [décrire le contexte] ?"
- Remplace "Quel est l'outil utilisé ?" par "Quel outil spécifique [nom du personnage] utilise-t-il dans [décrire le contexte] ?"
- Au lieu de "Qui est l'ennemi ?", demande "Qui est l'ennemi principal de [nom du personnage] dans [décrire le contexte] ?"
- Change "Quelle est la date de début de la mission ?" en "Quand commence la mission de [nom du personnage] dans [décrire le contexte] ?"
</s><</SYS>>

Contexte :
```
{context}
```

Utilisateur : Basé sur le contexte ci-dessus, veuillez générer une liste de exactement {nbr_questions} questions distinctes et contextuellement pertinentes. Assurez-vous que ces questions couvrent de manière exhaustive le contexte fourni.
Ne posez jamais de questions générales ou vagues.
Ajoutez toujours "Quoi", "Qui", "Quand", "Où" lorsque possible.
Ne terminez pas la question avec des phrases comme "dans le contexte" ou "dans le contexte donné" ou "dans le contexte" ou similaire.
Donnez-moi les questions en {language}.
Assistant: """


def get_answer_from_content_prompt_mistral(context, question, language="french"):
    print("question", question)
    return f"""<s><<SYS>>
Tu es un Assistant très minutieux et détaillé. Ta tâche est de générer des réponses professionnelles et détaillées, spécifiques au domaine des jeux pédagogiques. Tes réponses doivent être strictement basées sur le contexte fourni et dans la langue spécifiée. N'utilise pas de connaissances ou d'informations externes non incluses dans le contexte.
</s><</SYS>>

Contexte :

{context}

Utilisateur : Veuillez répondre à la question suivante en {language} : "{question}".
Si le contexte ne fournit pas suffisamment d'informations, réponds par : "Je n'ai pas assez de contenu pour répondre à cette question."

[Rappel : La réponse doit être en {language}.]

Assistant: """


def get_questions_from_content(context, nbr_questions=30, model="pedagogic_game", language="french"):
    return get_questions_from_content_prompt_mistral(context, nbr_questions, language)



def get_answer_question_from_content(context, question, model="pedagogic_game"):
    return get_answer_from_content_prompt_mistral(context, question, language="french")
