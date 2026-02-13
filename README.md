# aegis-core

The core security engine and MCP (Model Context Protocol) server for AegisProxy. Secures developer IDEs and CLI workflows.

## Features

- **PII Detection & Scrubbing**: Automatically identifies and pseudonymizes Australian PII including:
  - Tax File Numbers (TFNs)
  - Person names
- **MCP Server**: FastMCP-based server for integration with AI coding assistants
- **CLI Interface**: Command-line tool built with Typer for easy interaction

## Installation

```bash
pip install -e .
```

Or install dependencies directly:

```bash
pip install -r requirements.txt
```

After installation, you'll need to download the spaCy language model:

```bash
python -m spacy download en_core_web_sm
```

## Usage

### Starting the MCP Server

```bash
aegis serve
```

### Using the CLI

```bash
# Check version
aegis version

# Start the server
aegis serve
```

### IDE Integration

The `.mcp.json` configuration file enables automatic discovery by:
- Cursor IDE
- VS Code with MCP extensions

The server exposes the `scrub_context` tool which can be called from your AI assistant to scrub PII from text.

### Example

```python
from aegis_core.server import scrub_pii

text = "John Smith's TFN is 123456782"
scrubbed = scrub_pii(text)
print(scrubbed)  # Output: "<PERSON>'s TFN is <AU_TFN>"
```

## Development

Install development dependencies:

```bash
pip install -e ".[dev]"
```

## License

MIT License - see LICENSE file for details.
