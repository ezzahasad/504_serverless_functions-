import json
import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    """Azure Function HTTP trigger to classify serum potassium."""
    try:
        data = req.get_json()
    except ValueError:
        data = {}

    # Missing field
    if "potassium" not in data:
        return func.HttpResponse(
            json.dumps({"error": "Field 'potassium' is required."}),
            status_code=400,
            mimetype="application/json"
        )

    # Type check
    try:
        value = float(data["potassium"])
    except (TypeError, ValueError):
        return func.HttpResponse(
            json.dumps({"error": "'potassium' must be a number."}),
            status_code=400,
            mimetype="application/json"
        )

    # Apply rule
    status = "normal" if 3.5 <= value < 5.1 else "abnormal"
    category = "Normal (3.5–5.0 mmol/L)" if status == "normal" else "Abnormal (≤3.4 or ≥5.1 mmol/L)"

    body = {
        "potassium": value,
        "status": status,
        "category": category
    }

    return func.HttpResponse(json.dumps(body), mimetype="application/json")
