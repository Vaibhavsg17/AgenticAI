from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.duckduckgo import DuckDuckGo
from phi.tools.yfinance import YFinanceTools

from dotenv import load_dotenv

load_dotenv()

web_agent = Agent(
    name="Web Agent",
    role="Searches the web for information on a topic",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[DuckDuckGo()],
    instructions=["Always include sources"],
    show_tool_calls=True,
    markdown=True,
)

finance_agent = Agent(
    name="Finance Agent",
    role="Get Financial data",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[
        YFinanceTools(
            stock_price=True, analyst_recommendations=True, stock_fundamentals=True
        )
    ],
    show_tool_calls=True,
    markdown=True,
    instructions=["Use tables to display the data"],
)

agent_team = Agent(
    team=[web_agent, finance_agent],
    instructions=["Always include sources", "Use tables to display the data"],
    show_tools_calls=True,
    markdown=True,
)

agent_team.print_response(
    "Summerize and compare analyst recommendations and fundamentals for TSLA and NVDA",
    stream=True,
)
