import json

def potassium_classifier(request):
    """HTTP Cloud Function to classify serum potassium as normal or abnormal."""
    try:
        data = request.get_json(silent=True)
    except Exception:
        return (json.dumps({"error": "Invalid JSON."}), 400, {"Content-Type": "application/json"})

    # Missing field
    if not data or "potassium" not in data:
        return (json.dumps({"error": "Field 'potassium' is required."}), 400, {"Content-Type": "application/json"})

    # Type check
    try:
        value = float(data["potassium"])
    except (TypeError, ValueError):
        return (json.dumps({"error": "'potassium' must be a number."}), 400, {"Content-Type": "application/json"})

    # Apply rule
    status = "normal" if 3.5 <= value < 5.1 else "abnormal"
    category = "Normal (3.5–5.0 mmol/L)" if status == "normal" else "Abnormal (≤3.4 or ≥5.1 mmol/L)"

    body = {
        "potassium": value,
        "status": status,
        "category": category
    }
    return (json.dumps(body), 200, {"Content-Type": "application/json"})
