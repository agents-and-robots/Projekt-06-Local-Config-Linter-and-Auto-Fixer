def validate(config: dict) -> dict:
    """
    Baseline-Validator: markiert alles als gültig.
    """
    return {
        "valid": True,
        "errors": []
    }
