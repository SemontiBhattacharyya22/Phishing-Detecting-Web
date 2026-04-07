import re

def analyze_url(url):
    reasons = []

    if re.search(r'\d+\.\d+\.\d+\.\d+', url):
        reasons.append("IP address used in URL")

    if "@" in url:
        reasons.append("Contains '@' symbol")

    if "-" in url:
        reasons.append("Hyphen in domain")

    if len(url) > 50:
        reasons.append("Long suspicious URL")

    return reasons


def analyze_email(text):
    text = text.lower()
    score = 0
    reasons = []

    keywords = ["urgent", "verify", "password", "bank", "click here"]

    for word in keywords:
        if word in text:
            score += 1
            reasons.append(f"Keyword: {word}")

    links = re.findall(r'https?://[^\s]+', text)

    for link in links:
        url_reasons = analyze_url(link)
        if url_reasons:
            score += len(url_reasons)
            reasons.extend(url_reasons)

    if links:
        score += 1
        reasons.append("Contains link")

    prediction = "Phishing" if score >= 3 else "Safe"

    return {
        "prediction": prediction,
        "confidence": round(score / 6, 2),
        "score": score,
        "reasons": reasons
    }