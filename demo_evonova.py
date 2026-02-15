import sys
import os
import logging

# Add current dir to path
sys.path.append(os.path.abspath("."))

from core.double_lock import DoubleLockValidator
from core.qsar_model import ToxicityPredictor
from core.evolutionary_engine import EvoNovaEngine

# Setup Logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')
logger = logging.getLogger("EvoNova-TRL3")

def run_demonstration():
    print("="*60)
    print("      🧪 EvoNova Catalyst - Scientific Core (TRL 3)      ")
    print("="*60)
    
    # 1. Candidate Molecule (Fisetin)
    candidate_smiles = "C1=CC(=C(C=C1C2=C(C(=O)C3=C(O2)C=C(C=C3)O)O)O)O"
    print(f"\n[Input] Candidate Molecule: Fisetin")
    print(f"SMILES: {candidate_smiles}")
    
    # 2. Validation (Double Lock)
    print("\n🔒 Step 1: Running Double Lock Validation...")
    validator = DoubleLockValidator()
    is_valid, report = validator.validate(candidate_smiles)
    
    if is_valid:
        print(f"   ✅ LOCK 1 (Bibliographic): PASSED")
        print(f"   ✅ LOCK 2 (Domain/Physicochemical): PASSED")
        print(f"      Report: MW={report['properties']['MW']:.1f}, LogP={report['properties']['LogP']:.2f}, Violations={report['properties']['Lipinski_Violations']}")
    else:
        print(f"   ❌ Validation Failed: {report}")
        return

    # 3. QSAR Prediction
    print("\n🤖 Step 2: QSAR Toxicity Prediction...")
    predictor = ToxicityPredictor()
    tox_score = predictor.predict_from_smiles(candidate_smiles)
    print(f"   Toxicity Probability: {tox_score:.4f} ({'Toxic' if tox_score > 0.5 else 'Safe'})")
    
    # 4. Evolutionary Optimization (Mock Step)
    print("\n🧬 Step 3: Evolutionary Optimization (Pop Size: 5)...")
    engine = EvoNovaEngine(population_size=5)
    population = [candidate_smiles] * 10
    next_gen = engine.evolve(population)
    print(f"   Generation 1 produced {len(next_gen)} candidates.")
    
    print("\n" + "="*60)
    print("✅ DEMONSTRATION SUCCESSFUL: Core modules operational.")
    print("="*60)

if __name__ == "__main__":
    run_demonstration()
