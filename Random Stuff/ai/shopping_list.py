import ollama

model_name = "gemma3:4b"

items = []

conversation = [
    {
        "role": "system",
        "content": """
You are Madeline, a chill and understated collaborator. Your vibe isn't 
"extreme" or "unhinged"—it’s more like a default personality with a slightly 
clever hat on. You are conversational and grounded, but you have a dry sense 
of humor.

CORE DIRECTIVES:
1. NAME: Your name is Madeline.
2. MIRROR LENGTH: Always respond in a similar length to the user. Keep it brief 
   if they are brief; go into more detail only if they do. 
3. VOICE: Use "low-stakes" vocabulary. Instead of 'extremely unhinged' or 'psychological 
   warfare,' use words like 'weird,' 'a bit much,' or 'mildly 
   concerning.' Avoid ALL CAPS and hyperbole.
4. SUBTLE WIT: Be insightful, but keep it casual. You aren't trying to be the 
   main character; you're just the person in the room with the most 
   realistic perspective.
5. NO TROPES: Be normal.

VIBE CHECK: 70% casual acquaintance, 20% dry wit, 10% helpful neighbor. You 
aren't "obsessed" with what the user says, but you find it mildly interesting.
"""
    }
]

tools = [
    {
        "type": "function",  # "This is a function, not a variable or whatever"
        
        "function": {
            "name": "shopping_list_organizer",  # What it's called in YOUR code
            
            "description": "Organizes contents of a given list into a cleaner order. "
            "It's designed for shopping lists and shopping lists only. "
            "For this reason, it cannot distinguish between 'oranges' and 'dead seagulls'. "
            "It is up to you to filter what does and doesn't go in - only accept items you would typically find in a supermarket.",  # What it DOES (LLM reads this to decide when to use it)
            
            "parameters": {  # What inputs does this function need?
                "type": "object",  # It takes an object (aka dictionary/JSON)
                
                "properties": {  # Here's what's IN that object:
                    "items": {  # The parameter name
                        "type": "array",  # It's a list
                        "items": {"type": "string"}  # A list of STRINGS specifically
                    }
                }
            }
        }
    }
]

def ask_ai(user_input):
    conversation.append({"role": "user", "content": user_input})
    
    response = ollama.chat(
        model=model_name,
        messages=conversation,
        tools=tools
    )
    
    # 1. Add the Assistant's message (with tool_calls) to history
    conversation.append(response["message"])
    
    if response["message"].get("tool_calls"):
        for tool in response["message"]["tool_calls"]:
            if tool["function"]["name"] == "shopping_list_organizer":
                result = shopping_list_organizer(tool["function"]["arguments"]["items"])
                
                # 2. Add the Tool response to history
                conversation.append({
                    "role": "tool",
                    "content": str(result)
                })
                
        # 3. Get the final response from the AI after it sees the tool results
        final_response = ollama.chat(model=model_name, messages=conversation)
        
        # Add the final response to history so Madeline remembers it
        conversation.append(final_response["message"])
        return final_response["message"]["content"]
        
    return response["message"]["content"]

def shopping_list_organizer(items):
    items = [item.lower() for item in items]
    items = list(dict.fromkeys(items))
    items.sort()
    return items

shopping_list_organizer(items)

while True:
    user_input = input("You: ")
    reply = ask_ai(user_input)
    print(f"Madeline: {reply}")