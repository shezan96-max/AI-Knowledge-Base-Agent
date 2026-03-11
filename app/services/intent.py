pricing_keywords = ["price","pricing","cost","charge","how much","fee","rate","package"]
lead_keywords = ["contact","email","phone","reach you","talk to you","connect"]
demo_keywords = ["demo","trial","test","try"]


def detect_intent(text):
    text = text.lower()

    if any(word in text for word in demo_keywords):
        return "demo"
    if any(word in text for word in lead_keywords):
        return "lead"
    if any(word in text for word in pricing_keywords):
        return "pricing"
    return "general"
