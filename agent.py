import os
import asyncio
from dotenv import load_dotenv
from google import genai
from google.genai.types import Tool, GenerateContentConfig, GoogleSearch

load_dotenv()

GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')

client = genai.Client(api_key=GEMINI_API_KEY, http_options={'api_version': 'v1alpha'})
standard_model_id = "gemini-2.0-flash-exp"
thinking_model_id = "gemini-2.0-flash-thinking-exp"

def generate_text(prompt, model_id, tools=None):
    config = GenerateContentConfig(tools=tools) if tools else None
    response = client.models.generate_content(model=model_id, contents=prompt, config=config)
    return response.text

async def generate_thinking_response(prompt):
   response = client.models.generate_content(model = thinking_model_id, contents=prompt)
   for part in response.candidates[0].content.parts:
     if part.thought == True:
            print(f"Model Thought:\n{part.text}\n")
     else:
            print(f"\nModel Response:\n{part.text}\n")


async def agent_workflow(user_query):
    # Step 1: Determine if context is needed using standard Gemini model
    context_check_prompt = f"""
    You are an expert at understanding if a request needs additional context to answer.
    Analyze the following user request and determine if any context is needed from the outside world, like from the web.
    Return with "Needed" or "Not Needed".
    User request: {user_query}
    """
    needs_context = generate_text(context_check_prompt, standard_model_id)
    print(f"Needs context: {needs_context}\n")

    if "Needed" in needs_context:
       # Step 2: Use search tool to gather context
       search_tool = Tool(google_search=GoogleSearch())
       search_prompt = f"""
         Based on the following request: {user_query} what context can be gathered to provide the best response?
       """
       search_results = generate_text(search_prompt, standard_model_id, tools = [search_tool])
       print(f"Search Results: \n{search_results}")

        # Step 3: Combine user query with context and pass to thinking model
       augmented_prompt = f"""
           User request: {user_query}
           Context: {search_results}
           Using the provided context and the user request, answer the question while thinking out loud using the thinking model.
       """
       print(f"Augmented Prompt:\n{augmented_prompt}")
       await generate_thinking_response(augmented_prompt)

    else:
       # Step 4: If no context needed pass the request directly to the thinking model.
       print(f"Prompt passed to thinking model: \n{user_query}")
       await generate_thinking_response(user_query)


async def main():
    user_queries = [
        "What is the latest news about california wildfire 2025? And how many 'r' are in the word strrawberrrry"
    ]

    for query in user_queries:
        print(f"User Query: {query}\n")
        await agent_workflow(query)
        print("---------------------------------------------------\n")


if __name__ == "__main__":
    asyncio.run(main())
