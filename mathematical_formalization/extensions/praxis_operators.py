"""
PRAXIS OPERATORS EXTENSION
Extends core operators with praxis/context dependence.

PRINCIPLES:
1. ALL praxis operators REQUIRE praxis context
2. Praxis is treated FORMALLY (as context parameter)
3. NO implementation of praxis, NO subjectivism
"""

from typing import Set, Tuple
from dataclasses import dataclass, field
from enum import Enum, auto

from core_formal.operators_axiomatic import (
    OperatorSignature, OperatorCategory, OperatorArity
)

# ============================================================================
# 1. PRAXIS CATEGORIES
# ============================================================================

class PraxisCategory(Enum):
    """Categories of praxis operators - structural only"""
    CONDITIONING = auto()      # ◉ (praxis conditions truth)
    MEDIATION = auto()         # Praxis mediates between positions
    TRANSFORMATION = auto()    # Praxis transforms truth
    
    @property
    def is_conditioning(self) -> bool:
        return self == PraxisCategory.CONDITIONING

# ============================================================================
# 2. PRAXIS OPERATOR SIGNATURES
# ============================================================================

PRAXIS_CONDITIONING = OperatorSignature(
    symbol="◉",
    name="praxis_conditioning",
    category=OperatorCategory.DIALECTICAL,
    arity=OperatorArity.UNARY,
    input_types={"TruthPosition"},
    output_type="TruthPosition",
    preserves_contradiction=True,  # Praxis may preserve contradiction
    resolves_contradiction=False,
    axioms={
        "◉(P) depends on praxis context",
        "Different praxis forms yield different ◉(P)",
        "◉ expresses truth as praxis-emergent"
    }
)

PRAXIS_MEDIATION = OperatorSignature(
    symbol="↔️",
    name="praxis_mediation",
    category=OperatorCategory.DIALECTICAL,
    arity=OperatorArity.BINARY,
    input_types={"TruthPosition", "TruthPosition"},
    output_type="TruthPosition",
    preserves_contradiction=False,
    resolves_contradiction=True,
    axioms={
        "P ↔️ Q means praxis mediates between P and Q",
        "↔️ involves practical synthesis",
        "↔️ requires concrete activity, not just thought"
    }
)

PRAXIS_TRANSFORMATION = OperatorSignature(
    symbol="↻",
    name="praxis_transformation",
    category=OperatorCategory.DIALECTICAL,
    arity=OperatorArity.UNARY,
    input_types={"TruthPosition"},
    output_type="TruthPosition",
    preserves_contradiction=False,
    resolves_contradiction=True,
    axioms={
        "↻(P) transforms P through praxis",
        "↻ involves active changing of truth position",
        "↻ is practical counterpart of becoming"
    }
)

# ============================================================================
# 3. PRAXIS CONTEXT STRUCTURE (FORMAL ONLY)
# ============================================================================

@dataclass(frozen=True)
class PraxisContextSignature:
    """
    Formal signature of praxis context.
    
    Defines WHAT praxis context is (structurally),
    not HOW it works.
    """
    name: str
    dimensions: Set[str]  # e.g., {"social", "historical", "material"}
    
    # Structural properties
    is_collective: bool = False
    is_historical: bool = False
    is_material: bool = False
    
    def __str__(self) -> str:
        return f"PraxisContext({self.name})"

# Example praxis contexts (formal signatures only)
REVOLUTIONARY_PRAXIS = PraxisContextSignature(
    name="revolutionary_praxis",
    dimensions={"social", "historical", "political", "material"},
    is_collective=True,
    is_historical=True,
    is_material=True
)

SCIENTIFIC_PRAXIS = PraxisContextSignature(
    name="scientific_praxis",
    dimensions={"methodological", "theoretical", "experimental"},
    is_collective=True,
    is_historical=True,
    is_material=False  # Primarily conceptual
)

ARTISTIC_PRAXIS = PraxisContextSignature(
    name="artistic_praxis",
    dimensions={"aesthetic", "expressive", "material"},
    is_collective=False,  # Often individual
    is_historical=True,
    is_material=True
)

# ============================================================================
# 4. PRAXIS OPERATOR RELATIONS
# ============================================================================

@dataclass(frozen=True)
class PraxisRelation:
    """Praxis relation between operators - FORMAL ONLY"""
    operator_A: OperatorSignature
    operator_B: OperatorSignature
    praxis_relation: str  # "requires_context", "mediated_by", "transforms"
    
    # Praxis context required
    required_context: PraxisContextSignature = None
    
    # Formal constraints
    constraints: Set[str] = field(default_factory=set)

PRAXIS_OPERATOR_RELATIONS = [
    PraxisRelation(
        operator_A=PRAXIS_CONDITIONING,
        operator_B=PRAXIS_TRANSFORMATION,
        praxis_relation="precedes",
        required_context=REVOLUTIONARY_PRAXIS,
        constraints={
            "In Marxist dialectics",
            "When praxis aims at transformation"
        }
    ),
    PraxisRelation(
        operator_A=PRAXIS_MEDIATION,
        operator_B=PRAXIS_CONDITIONING,
        praxis_relation="requires",
        required_context=SCIENTIFIC_PRAXIS,
        constraints={
            "In scientific practice",
            "When mediation requires methodological context"
        }
    )
]

# ============================================================================
# 5. PRAXIS COMPOSITIONS WITH CORE OPERATORS
# ============================================================================

@dataclass(frozen=True)
class PraxisComposition:
    """Praxis composition of operators - FORMAL ONLY"""
    praxis_operator: OperatorSignature
    core_operator: OperatorSignature
    composition_type: str  # "praxis_prefix", "praxis_suffix", "praxis_wrap"
    
    # Required praxis context
    required_context: PraxisContextSignature = None
    
    # Validity conditions
    is_valid: bool
    validity_conditions: Set[str]
    
    # Resulting operator signature
    resulting_signature: OperatorSignature

from core_formal.operators_axiomatic import DIALECTICAL_NEGATION, AUFHEBUNG

PRAXIS_COMPOSITIONS = [
    # Praxis conditioning of negation
    PraxisComposition(
        praxis_operator=PRAXIS_CONDITIONING,
        core_operator=DIALECTICAL_NEGATION,
        composition_type="praxis_prefix",
        required_context=REVOLUTIONARY_PRAXIS,
        is_valid=True,
        validity_conditions={
            "When negation is praxis-dependent",
            "When social context mediates opposition"
        },
        resulting_signature=OperatorSignature(
            symbol="◉¬ᴰ",
            name="praxis_conditioned_negation",
            category=OperatorCategory.DIALECTICAL,
            arity=OperatorArity.UNARY,
            input_types={"TruthPosition"},
            output_type="TruthPosition",
            preserves_contradiction=True,
            axioms={
                "◉¬ᴰP depends on how praxis mediates negation",
                "◉¬ᴰP ≠ ¬ᴰ◉P in general (non-commutative)"
            }
        )
    ),
    
    # Praxis mediation of aufhebung
    PraxisComposition(
        praxis_operator=PRAXIS_MEDIATION,
        core_operator=AUFHEBUNG,
        composition_type="praxis_suffix",
        required_context=SCIENTIFIC_PRAXIS,
        is_valid=True,
        validity_conditions={
            "When synthesis requires practical mediation",
            "When theoretical contradictions need practical resolution"
        },
        resulting_signature=OperatorSignature(
            symbol="⤊↔️",
            name="praxis_mediated_synthesis",
            category=OperatorCategory.DIALECTICAL,
            arity=OperatorArity.BINARY,
            input_types={"TruthPosition", "TruthPosition"},
            output_type="TruthPosition",
            preserves_contradiction=False,
            resolves_contradiction=True,
            axioms={
                "⤊↔️(P, Q) requires practical activity for synthesis",
                "⤊↔️ involves both theoretical and practical moments"
            }
        )
    )
]

# ============================================================================
# 6. PRAXIS FAMILIES
# ============================================================================

@dataclass(frozen=True)
class PraxisFamily:
    """Family of praxis operators"""
    name: str
    members: Set[OperatorSignature]
    praxis_properties: Set[str] = field(default_factory=set)

PRAXIS_FAMILIES = [
    PraxisFamily(
        name="conditioning_family",
        members={PRAXIS_CONDITIONING},
        praxis_properties={"context-dependent", "truth-modifying"}
    ),
    PraxisFamily(
        name="mediation_family",
        members={PRAXIS_MEDIATION, PRAXIS_TRANSFORMATION},
        praxis_properties={"relational", "transformative", "active"}
    )
]

# ============================================================================
# 7. EXPORTS
# ============================================================================

__all__ = [
    # Praxis categories
    'PraxisCategory',
    
    # Praxis operators
    'PRAXIS_CONDITIONING',
    'PRAXIS_MEDIATION',
    'PRAXIS_TRANSFORMATION',
    
    # Praxis contexts
    'PraxisContextSignature',
    'REVOLUTIONARY_PRAXIS',
    'SCIENTIFIC_PRAXIS',
    'ARTISTIC_PRAXIS',
    
    # Praxis relations
    'PraxisRelation',
    'PRAXIS_OPERATOR_RELATIONS',
    
    # Praxis compositions
    'PraxisComposition',
    'PRAXIS_COMPOSITIONS',
    
    # Praxis families
    'PraxisFamily',
    'PRAXIS_FAMILIES'
]
