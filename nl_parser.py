import re

def nl_to_dsl(text):
    text = text.lower()

    entry_rules = []
    exit_rules = []

    if "buy" in text or "enter" in text:
        if "moving average" in text:
            period = int(re.search(r'(\d+)[- ]?day', text).group(1))
            entry_rules.append(f"close > sma(close,{period})")

        if "volume" in text and "million" in text:
            entry_rules.append("volume > 1000000")

    if "exit" in text or "rsi" in text:
        if "rsi" in text:
            period = int(re.search(r'rsi\((\d+)\)', text).group(1))
            exit_rules.append(f"rsi(close,{period}) < 30")

    dsl = "ENTRY: " + " AND ".join(entry_rules) + "\n"
    dsl += "EXIT: " + " AND ".join(exit_rules)

    return dsl
