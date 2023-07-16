
def clean_text(text):
    """Extract the temperature data from"""
    output = float(text.split(": ")[1])
    return output