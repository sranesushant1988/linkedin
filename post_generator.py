import openai
import random

openai.api_key = openai.api_key = __import__('os').environ['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']

def generate_post(brand, topic, tone="professional"):
    prompt = f"""
You are a startup founder. Your brand is {brand}.
Write a LinkedIn post about "{topic}" in a {tone} tone.
Start with a hook, write 2–3 short paragraphs, and end with a call to action.
Add 3 relevant hashtags.
"""
    res = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role":"user","content":prompt}]
    )
    return res.choices[0].message.content

def idea_generator(brand):
    ideas = [
        f"How {brand} is solving a major industry pain point",
        f"Lessons learned during {brand}'s MVP launch",
        f"The story behind founding {brand}",
        f"A customer success story from using {brand}",
        f"Why building in public is important for {brand}",
        f"Day in the life as a founder at {brand}",
    ]
    return random.choice(ideas)
