from google.adk.agents.llm_agent import Agent

image_agent = Agent(
    model='gemini-3-pro-image',
    name='ImageAgent',
    description='A helpful assistant for user questions.',
    instruction="You are an Image Agent. Generate and edit images based on user requests.",
)
