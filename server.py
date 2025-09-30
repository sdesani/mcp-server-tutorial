from fastmcp import FastMCP

# Create a FastMCP server instance
mcp = FastMCP("Demo MCP Server 🚀")

@mcp.tool
def greet(name: str) -> str:
    """Greet someone by name"""
    return f"Hello, {name}! Welcome to the MCP server demo."

@mcp.tool
def get_weather(city: str) -> str:
    """Get weather information for a city (demo function)"""
    return f"The weather in {city} is sunny with a temperature of 72°F (demo data)"


if __name__ == "__main__":
    # Run the MCP server
    mcp.run()
