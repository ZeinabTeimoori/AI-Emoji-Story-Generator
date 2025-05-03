import random
import google.generativeai as genai
genai.configure(api_key="")

# Emoji bank
emoji_bank = {
    "character1": ["🐱", "👾", "🦊", "🐉"],
    "character2": ["🤖", "🦸", "👻", "🦓"],
    "place": ["🌳", "🏰", "🌌", "🏝️"],
    "action": ["🎉", "🍕", "🎨", "🚀"]
}
# Keyword bank (general words to guide the story)
keyword_bank = ["friendship", "mystery", "bravery", "challenge", "journey", "discovery", "legend"]
# Generate a random selection of emojis and keywords
def generate_emoji_and_keywords():
    emoji_selection = {
        "character1": random.choice(emoji_bank["character1"]),
        "character2": random.choice(emoji_bank["character2"]),
        "place": random.choice(emoji_bank["place"]),
        "action": random.choice(emoji_bank["action"])
    }
    selected_keywords = random.sample(keyword_bank, 3)  # Pick 3 random keywords
    return emoji_selection, selected_keywords
# Use LLM to generate a story with emojis and keywords
def generate_story():
    emoji_selection, selected_keywords = generate_emoji_and_keywords()    
    prompt = (
        f"Write a creative short story that includes these elements:\n\n"
        f"Emojis: {emoji_selection['character1']} {emoji_selection['character2']} {emoji_selection['place']} {emoji_selection['action']}\n"
        f"Keywords: {', '.join(selected_keywords)}\n\n"
        f"short story, no more than 20 words.\n\n"
        f"Make sure the story is fun, engaging, and naturally incorporates both the emojis and the keywords."
    )
    # Make the request to Gemini API
    response = genai.GenerativeModel("gemini-1.5-flash").generate_content(prompt)
    return response.text
# Run the generator
print("Welcome to the Emoji Story Generator!\n")
print("Here’s a story just for you:\n")
My_story = generate_story()
print(My_story)
#Save a story to a file
with open("story.txt", "w", encoding="utf-8") as file:
    file.write(My_story)
print("Story saved!")



