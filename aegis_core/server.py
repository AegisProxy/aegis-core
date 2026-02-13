"""
MCP Server implementation with PII scrubbing capabilities
"""

from fastmcp import FastMCP
from presidio_analyzer import AnalyzerEngine, RecognizerRegistry
from presidio_anonymizer import AnonymizerEngine
from presidio_analyzer.predefined_recognizers import AuTfnRecognizer
import re

# Initialize FastMCP server
mcp = FastMCP("aegis-core")

# Initialize Presidio engines
analyzer = AnalyzerEngine()
anonymizer = AnonymizerEngine()

# Add Australian TFN recognizer
registry = RecognizerRegistry()
registry.add_recognizer(AuTfnRecognizer())


@mcp.tool()
def scrub_context(text: str) -> str:
    """
    Scrub Australian PII from the provided text.
    
    Identifies and pseudonymizes:
    - Australian Tax File Numbers (TFNs)
    - Person names
    
    Args:
        text: The text to scrub for PII
        
    Returns:
        The pseudonymized text with PII replaced
    """
    # Analyze the text for PII entities
    # Support Australian locale and look for TFNs and person names
    results = analyzer.analyze(
        text=text,
        language="en",
        entities=["AU_TFN", "PERSON"]
    )
    
    # Anonymize the detected PII
    anonymized = anonymizer.anonymize(
        text=text,
        analyzer_results=results
    )
    
    return anonymized.text


def run_server():
    """Run the MCP server"""
    mcp.run()
