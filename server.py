from fastmcp import FastMCP
import secrets
import string

# Create a FastMCP server instance
mcp = FastMCP("Demo MCP Server 🚀")

@mcp.tool
def generate_password(length: int) -> str:
    """Generate a secure random password of the given length"""
    if length <= 0:
        raise ValueError("length must be a positive integer")

    # Use a mix of upper/lowercase letters, digits, and punctuation
    alphabet = string.ascii_letters + string.digits + string.punctuation
    return "".join(secrets.choice(alphabet) for _ in range(length))


@mcp.tool
def score_password(password: str) -> int:
    """Score the password strength on a scale of 0 (weakest) to 10 (strongest)."""
    if not password:
        return 0

    length = len(password)

    # Length score: 0-4 points
    if length >= 20:
        length_points = 4
    elif length >= 16:
        length_points = 3
    elif length >= 12:
        length_points = 2
    elif length >= 8:
        length_points = 1
    else:
        length_points = 0

    # Variety score: +1 for each character class present (lower, upper, digit, punctuation)
    has_lower = any(c.islower() for c in password)
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_punct = any(c in string.punctuation for c in password)
    variety_points = int(has_lower) + int(has_upper) + int(has_digit) + int(has_punct)

    # Uniqueness score based on fraction of unique chars: 0-2 points
    unique_fraction = len(set(password)) / length
    if unique_fraction >= 0.8:
        uniqueness_points = 2
    elif unique_fraction >= 0.6:
        uniqueness_points = 1
    else:
        uniqueness_points = 0

    score = length_points + variety_points + uniqueness_points
    if score < 0:
        return 0
    if score > 10:
        return 10
    return score


if __name__ == "__main__":
    # Run the MCP server
    mcp.run()