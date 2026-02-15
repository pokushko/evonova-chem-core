import random

class DoubleLockValidator:
    """
    Mock implementation of Double Lock Validator for TRL 3 Demo.
    In the full version, this connects to the Semantic Scholar API and RDKit.
    """
    def __init__(self):
        pass

    def validate(self, smiles: str):
        # Simulate validation logic
        # For demo purposes, we always return True for valid-looking SMILES
        if not smiles or len(smiles) < 5:
            return False, {"error": "Invalid SMILES length"}
            
        # Mock RDKit properties
        report = {
            "properties": {
                "MW": 286.24,
                "LogP": 1.25,
                "Lipinski_Violations": 0,
                "TPSA": 102.5
            },
            "novelty_score": 0.95,
            "status": "VALID"
        }
        return True, report
