import openai
import time
import sys
import random

# Replace YOUR_API_KEY with your OpenAI API key

# Set the model engine to use for text generation
model_engine = "text-davinci-002"

# Set the initial prompt for the story
#prompt = "Once upon a time, there was a brave knight named Sir John who lived in a kingdom far, far away."
#prompt = sys.argv[1]
prompt = "Who was Simba and why he killed Scar? Start you answer as: once there was a lion cub called Simba"

# Set the maximum number of tokens to generate for each response
max_tokens = 4000

# Set the number of lines we want to generate for the story
num_lines = 4

epic_ones =  ["Don Vito Corleone from the movie God Father", "Red (Morgan Freeman) from the movie Shawshank Redemption", "Forrest Gump from the movie Forrest Gump", "Rick Deckard from the movie Blade Runner", "the sentient computer named HAL 9000 movie A Space Odyssey", "Manny from the movie Ice Age"]

# Generate the story by repeatedly calling the OpenAI API and appending the responses to a list
numbers = []
for i in range(len(epic_ones)):
    my_random_number = random.randint(0, len(epic_ones) - 1)
    if my_random_number not in numbers:
        numbers.append(my_random_number)

story = []
print ("The Pasta Stroy is made of Lion King's Simba,")
for i in range(num_lines):
    # Generate the next line of the story
    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=max_tokens,
        n=1,
        stop=None,
        temperature=0.9
    )
    line = response.choices[0].text.strip()
    
    # Append the line to the story
    story.append(line)
    
    # Set the prompt to the current story so far
    prompt = "continue and mix the story by relating  " + epic_ones[numbers[i]] + " assuming this character also existed and interacted with Simba. Do not include any romantic text" 
    print (epic_ones[numbers[i]],",")
    
    # Wait a bit to avoid hitting the API rate limit
    time.sleep(1)
    
# Print the generated story
print("The Pasta is ready...\n")
print("\n".join(story))

