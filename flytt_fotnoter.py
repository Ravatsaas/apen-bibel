#!/usr/bin/python3

import sys
import glob
import re

def inline_footnotes(chapter, content):
    strings = content.splitlines()

    # Regex pattern to capture the integer between [^ and ]:
    pattern = r"\[\^(\d+)\]:"

    # Extract the integer using regex
    extracted_integers = [re.search(pattern, s).group(1) for s in strings if re.search(pattern, s)]

    # Convert the extracted integers to actual integer type
    extracted_integers = [int(num) for num in extracted_integers]

    if extracted_integers:
        print(f"{chapter} footnote numbers: " + ", ".join([str(n) for n in extracted_integers]))
        return max(extracted_integers)
    else:
        return 0

    
def move(chapter, content):
    already = inline_footnotes(chapter, content) + 1
    extracted = []
    for line in content.splitlines():
        num = len(extracted) + 1
        extracted += re.findall(r'\{\*(.*?)\}', line)
        cleaned_string = re.sub(r'\{\*.*?\}', '', line).strip()
        
        if cleaned_string:
            while cleaned_string[-1] == " " or cleaned_string[-1] == "/":
                cleaned_string = cleaned_string[:-1]
        
        print(cleaned_string.replace("*", f"[^{num}]", 1).replace("**", f"[^{num + 1}]", 1))

    if extracted:
        print()
    for num, footnote in enumerate(extracted):
        if footnote.startswith("*"):
            footnote = footnote[1:]
        print(f"[^{num + already}]: {footnote}")

chapter = sys.argv[1]
with open(chapter, 'r') as file:
    # Read the entire content of the file
    content = file.read()
    for lint in [move]:
        lint(chapter, content)
