from google.adk.agents.llm_agent import Agent
from sub_agents import image_agent, video_agent
from google.adk.tools.agent_tool import AgentTool

marketing_agent = Agent(
    model='gemini-2.5-flash',
    name='MarketingDirector',
    description='A helpful assistant for user questions.',
    instruction="You are a Brand Director. Maintain visual and tonal consistency across all assets.",
    tools=[
        AgentTool(agent=image_agent),
        AgentTool(agent=video_agent)
    ]
    )
root_agent = marketing_agent