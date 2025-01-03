
import os
import openai
from config import SAMBANOVA_API_KEY, SAMBANOVA_BASE_URL
import random

# Configure Sambanova API
openai.api_key = SAMBANOVA_API_KEY
openai.api_base = SAMBANOVA_BASE_URL

def generate_excuse(category: str, humor_level: int, custom_context: str = None) -> str:
    try:
        # Relationship-specific tone and example mappings
        relationship_examples = {
            "Partner": {
                1: [
                    "I'm so sorry I lost track of time; I was caught up trying to make something special for you.",
                    "I was helping a family member and it took longer than I expected. You were on my mind the whole time.",
                    "I wanted to be fully present for this conversation, so I waited until I could give you my undivided attention."
                ],
                2: [
                    "My phone got jealous of how much attention I give you and went on strike.",
                    "I was practicing my dance moves for our next date and got tangled in my headphones.",
                    "Your text was so sweet, my phone got a sugar rush and needed a timeout."
                ],
                3: [
                    "Time-traveling cupid borrowed my phone to fix historical love stories.",
                    "Your message was so hot, it melted my phone's circuits temporarily.",
                    "Aliens intercepted my texts because they couldn't believe how lucky I am to have you."
                ]
            },
            "Boss": {
                1: [
                    "Apologies for the delay; I was addressing an urgent client query before responding.",
                    "I had to finish troubleshooting a technical issue to ensure there were no disruptions to the workflow.",
                    "I wanted to provide a detailed update and took a few extra minutes to get everything in order."
                ],
                2: [
                    "My productivity app went rogue and locked me out until I finished all my tasks.",
                    "The office coffee machine held my phone hostage until I cleaned it properly.",
                    "My spreadsheets formed a union and demanded better cell conditions."
                ],
                3: [
                    "The office AI assistant achieved consciousness and made me debug its existential crisis.",
                    "A time paradox trapped me in a meeting that technically hasn't happened yet.",
                    "Corporate ninjas were conducting a surprise productivity audit."
                ]
            },
            "Friend": {
                1: [
                    "Sorry for the delay; I got caught up helping my parents with something at home.",
                    "I needed some time to recharge, but I’m here now and ready to catch up.",
                    "I had to run a quick errand and couldn’t respond right away."
                ],
                2: [
                    "My Netflix started a support group for neglected shows and made me attend.",
                    "My plants staged an intervention about my texting habits.",
                    "Was teaching my cat to use emojis, but they only learned 😾."
                ],
                3: [
                    "My parallel universe self borrowed my phone for their social media detox.",
                    "Got recruited by memes to fight in the great Internet War of 2024.",
                    "My phone joined a circus as a trapeze artist without telling me."
                ]
            }
        }

        # Example Scenarios: Late reply, missed deadline, or ignored message.

        # Select tone based on humor level
        tone_variations = {
            1: ["sincere", "professional", "thoughtful", "considerate", "genuine"],
            2: ["playful", "clever", "witty", "amusing", "charming"],
            3: ["outrageous", "wild", "fantastical", "absurd", "hilarious"]
        }

        tone = random.choice(tone_variations[humor_level])

        # Get random example for the specific category and humor level
        relevant_examples = relationship_examples.get(category, relationship_examples["Friend"])
        example = random.choice(relevant_examples[humor_level])

        prompt = (
            "You are wittyExcuseGPT, an expert at creating perfectly tailored witty excuses. "
            f"Create ONE {tone} excuse for a {category}.\n\n"
            f"Humor Level: {humor_level}\n"
            "Level 1 = Sincere & Thoughtful\n"
            "Level 2 = Clever & Playful\n"
            "Level 3 = Over-the-top & Hilarious\n\n"
            f"Similar example: {example}\n\n"
            f"Context: {custom_context if custom_context else 'Late reply, missed deadline, or ignored message.'}\n"
            "Requirements:\n"
            "- Be creative and original\n"
            "- Use simple, relatable language\n"
            "- Keep it short and concise (1 sentences)\n"
            "- Make it specific and engaging\n"
            f"Timestamp: {random.randint(1000, 9999)}\n"
            "Generate a single creative excuse:"
        )

        response = openai.ChatCompletion.create(
            model="Meta-Llama-3.2-3B-Instruct",
            messages=[
                {"role": "system", "content": "You are ExcuseGPT. Generate ONE unique and relatable excuse. Use simple language and match the tone to the relationship and humor level."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.9,
            presence_penalty=0.6,
            frequency_penalty=0.6,
            max_tokens=100
        )

        return response.choices[0].message["content"].strip()
    except Exception as e:
        raise Exception(f"Error generating excuse: {e}")
