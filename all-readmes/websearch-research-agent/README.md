# Research Assistant Agent

A powerful research assistant built with Claude (Anthropic's AI) and LangChain that can search the web and answer questions based on current information.

## Features

- 🤖 Powered by Claude Sonnet 4 for intelligent reasoning
- 🔍 Web search capability using Tavily API
- 💬 Interactive chat interface
- 🎯 ReAct (Reasoning + Acting) agent pattern
- 📅 Date-aware for accurate current event searches
- 🛡️ Built-in error handling and rate limit management

## Prerequisites

- Python 3.8 or higher
- Anthropic API key (get one at https://console.anthropic.com/)
- Tavily API key (get one at https://tavily.com - free tier available)

## Installation

1. **Clone or download this project**

2. **Install required packages:**
   ```bash
   pip install langchain langchain-anthropic tavily-python python-dotenv langchainhub
   ```

3. **Create a `.env` file** in the project root with your API keys:
   ```
   ANTHROPIC_API_KEY=your_anthropic_key_here
   TAVILY_API_KEY=your_tavily_key_here
   ```

## Project Structure

```
.
├── research_agent.py    # Main agent implementation
├── example.py          # Example usage script
├── .env               # API keys (create this file)
└── README.md          # This file
```

## Usage

### Interactive Mode

Run the main agent for an interactive chat session:

```bash
python research_agent.py
```

This will start an interactive loop where you can ask questions. The agent will automatically search the web when needed.

Example interaction:
```
You: What were the top tech news stories this week?
Agent: [searches and provides current tech news]

You: Who won the latest Nobel Prize in Physics?
Agent: [searches and provides the answer]
```

Type `quit`, `exit`, or `q` to stop.

### Programmatic Usage

Use `example.py` to see how to use the agent programmatically:

```bash
python example.py
```

Or integrate it into your own code:

```python
from research_agent import create_research_agent

# Create the agent
agent = create_research_agent()

# Ask a question
response = agent.invoke({"input": "Your question here"})
print(response['output'])
```

## How It Works

The agent uses a **ReAct (Reasoning + Acting)** pattern:

1. **Thought**: The agent thinks about what it needs to do
2. **Action**: It decides which tool to use (web search)
3. **Observation**: It processes the tool's output
4. **Repeat**: Until it has enough information to answer

The agent is date-aware and knows it's currently in 2026, so it will search for current information appropriately.

## Key Components

### Web Search Tool
- Uses **Tavily API** for reliable web searches
- Returns up to 5 relevant results per search
- Includes title, content snippet, and URL for each result

### Claude Model
- Uses **Claude Sonnet 4** (`claude-sonnet-4-20250514`)
- Configured with current date context
- Temperature set to 0 for consistent, factual responses

### Agent Configuration
- Maximum 5 iterations to prevent infinite loops
- Verbose mode enabled to see the agent's reasoning
- Automatic error handling for robustness

## Configuration Options

You can customize the agent in `research_agent.py`:

- **Model**: Change the Claude model version
- **Temperature**: Adjust creativity (0 = deterministic, 1 = creative)
- **Max iterations**: Change the iteration limit
- **Verbose**: Toggle to see/hide agent reasoning
- **Max results**: Adjust number of search results (in `web_search` function)

## Troubleshooting

### API Key Errors
```
Error: ANTHROPIC_API_KEY not found in environment variables.
```
**Solution**: Make sure your `.env` file exists and contains valid API keys.

### Rate Limit Errors (Old DuckDuckGo Implementation)
If you're using the old DuckDuckGo implementation and seeing rate limits, upgrade to Tavily as shown in this version.

### Import Errors
```
ModuleNotFoundError: No module named 'X'
```
**Solution**: Install missing packages:
```bash
pip install langchain langchain-anthropic tavily-python python-dotenv langchainhub
```

### Search Not Working
Make sure:
1. Your `TAVILY_API_KEY` is correctly set in `.env`
2. You have an active internet connection
3. You haven't exceeded Tavily's free tier limits (1000 searches/month)

## Example Queries

The agent works best with questions that require current information:

✅ **Good queries:**
- "What were the top tech news stories this week?"
- "Who is the current CEO of Microsoft?"
- "What are the latest developments in AI?"
- "What's the weather forecast for this weekend?"

✅ **Also works for:**
- "What is the capital of France?" (answers without searching)
- "Explain quantum computing" (answers from knowledge)

## API Cost Considerations

- **Anthropic API**: Charges per token used (input + output)
- **Tavily API**: Free tier includes 1,000 searches/month
- The agent limits iterations to 5 to control costs

## Recent Updates

- 📅 Added date context so agent knows current year (2026)
- 🔧 Improved error handling and rate limit management
- 📝 Enhanced search result formatting



## Resources

- [Anthropic Claude Documentation](https://docs.anthropic.com/)
- [LangChain Documentation](https://python.langchain.com/)
- [Tavily API Documentation](https://docs.tavily.com/)
- [ReAct Paper](https://arxiv.org/abs/2210.03629)

## Support

For issues related to:
- **Claude API**: Check [Anthropic's support](https://support.anthropic.com/)
- **LangChain**: See [LangChain docs](https://python.langchain.com/)
- **Tavily**: Visit [Tavily's documentation](https://docs.tavily.com/)

---

**Note**: This agent requires active API keys and internet connection to function. Make sure to keep your `.env` file secure and never commit it to version control.
