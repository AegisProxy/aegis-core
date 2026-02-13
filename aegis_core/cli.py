"""
CLI entry point for Aegis Core MCP server
"""

import typer
from aegis_core.server import run_server

app = typer.Typer(
    name="aegis",
    help="Aegis Core - MCP Server for PII Detection and Scrubbing"
)


@app.command()
def serve():
    """Start the MCP server"""
    typer.echo("Starting Aegis Core MCP server...")
    run_server()


@app.command()
def version():
    """Show version information"""
    from aegis_core import __version__
    typer.echo(f"Aegis Core version {__version__}")


if __name__ == "__main__":
    app()
