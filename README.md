# BrandGenius 🎨

A multi-agent AI system powered by Google's Agent Development Kit (ADK) and Gemini 2.5 Flash, designed to help with brand marketing tasks including image and video generation.

## Overview

BrandGenius is an intelligent marketing assistant that uses a hierarchical agent architecture to handle various creative tasks. The system features a Marketing Director agent that orchestrates specialized sub-agents for image and video generation, ensuring visual and tonal consistency across all brand assets.

## Features

- **🎯 Marketing Director Agent**: Central coordinator that maintains brand consistency
- **🖼️ Image Generation**: Create custom images using Stability.ai's SD3.5 Flash model
- **🎬 Video Agent**: Placeholder for future video generation capabilities
- **🤖 Multi-Agent Architecture**: Specialized agents working together seamlessly

## Architecture

```
MarketingDirector (Root Agent)
├── ImageAgent - Generates images via Stability.ai API
└── VideoAgent - Future video generation capabilities
```

## Prerequisites

- Python 3.8+
- Google ADK
- Stability.ai API key

## Installation

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd brandgenuis
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv myenv
   source myenv/bin/activate  # On Windows: myenv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install google-adk
   pip install requests
   ```

4. **Set up environment variables**
   ```bash
   export STABILITY_API_KEY="your_stability_api_key_here"
   ```

## Usage

### Starting the Agent

```bash
adk web
```

This will launch the web interface where you can interact with the Marketing Director agent.

### Example Interactions

**Generate an Image:**
```
User: Create a minimalist logo for a coffee brand with warm colors
Agent: [Generates image using Stability.ai and saves to generated_images/]
```

**Ask for Marketing Advice:**
```
User: What are some brand consistency tips?
Agent: [Provides expert marketing guidance]
```

## Project Structure

```
brandgenuis/
├── my_agent/
│   ├── __init__.py
│   └── agent.py           # Main Marketing Director agent
├── sub_agents/
│   ├── image_agent/
│   │   ├── __init__.py
│   │   └── agent.py       # Image generation sub-agent
│   └── video_agent/
│       ├── __init__.py
│       └── agent.py       # Video generation sub-agent (placeholder)
├── generated_images/      # Output directory for generated images
└── myenv/                 # Python virtual environment
```

## Agent Descriptions

### Marketing Director
- **Model**: Gemini 2.5 Flash
- **Role**: Orchestrates sub-agents and maintains brand consistency
- **Tools**: Image Agent, Video Agent

### Image Agent
- **Model**: Gemini 2.5 Flash
- **Role**: Generates images from text descriptions
- **Backend**: Stability.ai SD3.5 Flash
- **Output Formats**: JPEG, PNG, WebP

### Video Agent
- **Model**: Gemini 2.5 Flash
- **Status**: Placeholder for future development

## Configuration

### Image Generation

The image agent uses the following default settings:
- **Model**: SD3.5 Flash
- **Output Format**: JPEG (configurable to PNG or WebP)
- **Save Location**: `./generated_images/`

You can customize these settings in [sub_agents/image_agent/agent.py](sub_agents/image_agent/agent.py).

## API Keys

You'll need the following API keys:

1. **Stability.ai API Key**: Required for image generation
   - Get your key at: https://platform.stability.ai/
   - Set as environment variable: `STABILITY_API_KEY`

## Development

### Adding New Sub-Agents

1. Create a new directory in `sub_agents/`
2. Define your agent with appropriate tools
3. Register it with the Marketing Director in [my_agent/agent.py](my_agent/agent.py)

Example:
```python
from google.adk.agents.llm_agent import Agent
from google.adk.tools.agent_tool import AgentTool
from sub_agents import your_new_agent

marketing_agent = Agent(
    # ... existing config
    tools=[
        AgentTool(agent=image_agent),
        AgentTool(agent=video_agent),
        AgentTool(agent=your_new_agent)
    ]
)
```

## Troubleshooting

**Image generation fails:**
- Verify your `STABILITY_API_KEY` is set correctly
- Check your Stability.ai API quota and credits

**Agent not responding:**
- Ensure virtual environment is activated
- Verify all dependencies are installed
- Check that `adk web` command completed successfully

## Future Roadmap

- [ ] Implement video generation functionality
- [ ] Add text-to-speech capabilities
- [ ] Support for batch image generation
- [ ] Brand style guide integration
- [ ] Multi-language support

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

[Add your license here]

## Acknowledgments

- Built with [Google ADK](https://github.com/google/adk)
- Image generation powered by [Stability.ai](https://stability.ai/)
- LLM powered by Gemini 2.5 Flash

---

**Note**: This project uses Google's Agent Development Kit. Make sure you have the necessary credentials and permissions to use Google Cloud services.
