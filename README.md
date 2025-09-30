## MCP Server Tutorial

This project contains a simple MCP server using `fastmcp`.

### Available Tools

- **generate_password(length: int) -> str**: Generate a secure random password of the given length using a mix of uppercase, lowercase, digits, and punctuation.
  - **length**: Positive integer specifying the desired password length.
  - Returns: A securely generated password string.
  - Errors: Raises `ValueError` if `length <= 0`.

- **score_password(password: str) -> int**: Score the provided password on a scale from 0 (weakest) to 10 (strongest).
  - **password**: The password string to evaluate.
  - Returns: Integer score in the range 0–10 based on length, character variety, and uniqueness.

### Example

Request a 16-character password:

```json
{
  "tool": "generate_password",
  "arguments": { "length": 16 }
}
```

Score a password's strength:

```json
{
  "tool": "score_password",
  "arguments": { "password": "S3cure!Passw0rd#2025" }
}
```

### Notes

- Previous demo tools (`greet`, `get_weather`) were removed in favor of the password tools.