from google.adk.agents.llm_agent import Agent

video_agent = Agent(
    model='gemini-2.5-flash',
    name='video_agent',
    description='A helpful assistant for user questions.',
    instruction='Answer user questions to the best of your knowledge',
)
