#!/usr/bin/env python3
"""
Example usage of Aegis Core PII scrubbing
"""

from aegis_core.server import scrub_pii

print("=" * 70)
print("Aegis Core - PII Scrubbing Demo")
print("=" * 70)
print()

# Example 1: Simple name scrubbing
print("Example 1: Person Name Detection")
print("-" * 70)
text1 = "Contact John Smith for more information"
print(f"Original: {text1}")
print(f"Scrubbed: {scrub_pii(text1)}")
print()

# Example 2: TFN scrubbing
print("Example 2: Australian TFN Detection")
print("-" * 70)
text2 = "The tax file number on record is 123456782"
print(f"Original: {text2}")
print(f"Scrubbed: {scrub_pii(text2)}")
print()

# Example 3: Combined PII
print("Example 3: Combined Name and TFN")
print("-" * 70)
text3 = "Application from Sarah Johnson, TFN: 876543210"
print(f"Original: {text3}")
print(f"Scrubbed: {scrub_pii(text3)}")
print()

# Example 4: Multiple names
print("Example 4: Multiple Persons")
print("-" * 70)
text4 = "Meeting attendees: Michael Brown, Emily Davis, and Robert Wilson"
print(f"Original: {text4}")
print(f"Scrubbed: {scrub_pii(text4)}")
print()

# Example 5: No PII
print("Example 5: Text Without PII")
print("-" * 70)
text5 = "This is a general message about company policies"
print(f"Original: {text5}")
print(f"Scrubbed: {scrub_pii(text5)}")
print()

print("=" * 70)
print("All examples completed successfully!")
print("=" * 70)
