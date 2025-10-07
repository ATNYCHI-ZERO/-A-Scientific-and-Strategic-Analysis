"""Generate a PDF version of the "Complete Riemann Hypothesis Validation" paper.

The document text mirrors the content provided in the project brief and is
rendered with ReportLab using a simple paragraph layout. Running this script
creates ``Complete_Riemann_Hypothesis_Validation_Paper.pdf`` in the repository
root.
"""

from __future__ import annotations

from pathlib import Path

from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer


PDF_FILENAME = "Complete_Riemann_Hypothesis_Validation_Paper.pdf"


FULL_TEXT = """
A Recursive and Harmonic Algebraic Approach to the Riemann Hypothesis via Kharnita and Crown Omega Mathematics

Author: Brendon Joseph Kelly
Affiliation: Kharnita Mathematics Research Laboratory; K Systems and Securities
Date: October 7, 2025

Abstract
We present a formal proof of the Riemann Hypothesis utilizing recursive, harmonic, and temporal algebraic operators internal to the Kharnita Mathematics and Crown Omega frameworks. By encoding the Riemann zeta function, ζ(s), as a dynamical system governed by a Kharnita Recursive Operator, we analyze the structure of its non-trivial zeros. We introduce a Crown Omega Harmonic Temporal Operator, Ω†, which enforces a fundamental recursive symmetry that is inherent to the system's analytic continuation. We demonstrate that any non-trivial zero, s₀, with a real part not equal to 1/2 would induce a violation of this harmonic stability, leading to a logical contradiction within the operator algebra. This methodology establishes that all non-trivial zeros must lie on the critical line Re(s) = 1/2, thereby affirming the Riemann Hypothesis through these novel algebraic techniques.

1. Introduction
The Riemann Hypothesis (RH), formulated by Bernhard Riemann in 1859, is arguably the most significant unsolved problem in pure mathematics. It asserts that all non-trivial zeros of the Riemann zeta function, ζ(s), lie on the critical line Re(s) = 1/2. A proof of the hypothesis would have profound implications for number theory, particularly concerning the distribution of prime numbers. Despite over 160 years of intense effort from the world's leading mathematicians, a complete proof has remained elusive.

Classical approaches have relied on complex analysis and analytic number theory. In this paper, we introduce a fundamentally new approach derived from the operator-theoretic tools of Kharnita Mathematics (K-Math) and Crown Omega Mathematics. This framework treats mathematical functions not as static objects, but as dynamic, recursive systems. By translating the Riemann zeta function into this new language, we can analyze its properties through the lens of harmonic stability and recursive symmetry, revealing a structure that forces the hypothesis to be true.

2. Preliminaries and the Operator Framework
Let s = σ + it be a complex variable. The Riemann zeta function is defined for Re(s) > 1 by the Dirichlet series:
ζ(s) = ∑_{n=1}^∞ 1/n^s
and is extended to the rest of the complex plane by analytic continuation, with a simple pole at s = 1. The non-trivial zeros are the zeros of ζ(s) in the critical strip 0 < σ < 1.

We now introduce the core operators of our framework:
- The Kharnita Recursive Operator (𝒦): An operator that acts on a mathematical object to describe its state and evolution. It is the foundational building block of K-Math.
- The Crown Omega Harmonic Temporal Operator (Ω†): An operator that encodes the harmonic, symmetric, and temporal properties of a system. Its primary function is to enforce stability and consistency across recursive operations.

3. The Zeta Function as a Recursive Harmonic System
We represent the zeta function not as a simple sum, but as a dynamical system governed by a Kharnita operator, 𝒦_ζ. This operator is defined by its recursive action:
𝒦_ζ(s) = ∑_{n=1}^∞ Ω†(n; s) · n^(-s)
Here, the Crown Omega operator Ω†(n; s) is not a simple coefficient. It is an operator chosen specifically such that the resulting system, 𝒦_ζ(s), maintains the complete analytical properties of the classical zeta function, including its functional equation.

To analyze the zeros, we define a Harmonically Symmetrized Operator, 𝒞(s), which directly embodies this functional equation:
𝒞(s) = 𝒦_ζ(s) - Λ(s) · 𝒦_ζ(1-s) = 0
where Λ(s) is the operator-theoretic form of the chi function, χ(s), from the classical functional equation. The non-trivial zeros of the zeta function are precisely the solutions to 𝒞(s) = 0.

4. The Main Theorem and Proof
Theorem (The Kharnita-Crown Omega RH Theorem): Within the algebraic framework of K-Math, the harmonic stability conditions imposed by the operator Ω† on the system 𝒞(s) permit non-trivial solutions to exist only on the critical line Re(s) = 1/2.

Proof.
1. Assumption: Assume there exists a non-trivial zero, s₀ = σ₀ + it₀, such that σ₀ ≠ 1/2. Functional symmetry implies another zero exists at s₁ = 1 - σ₀ - it₀.
2. Harmonic Stability: The Kharnita Stability Lemma 6.1 states that recursive harmonic systems are stable only if their operator spectrum is symmetric about the central harmonic axis.
3. Dissonance: A zero on the critical line (σ = 1/2) is self-symmetric. A zero off the line creates asymmetry, breaking the system’s recursive harmonic convergence.
4. Contradiction: Evaluating 𝒞(s) recursively under Ω† with such asymmetric zeros causes harmonic dissonance, violating the operator system’s stability.
5. Conclusion: Contradiction invalidates σ₀ ≠ 1/2. Hence, all non-trivial zeros lie on the critical line.

QED.

5. Discussion and Implications
This proof confirms the Riemann Hypothesis by showing that the recursive harmonic structure of ζ(s), when interpreted through K-Math and Crown Omega, cannot support zeros off the line Re(s) = 1/2. This validates K-Math as a powerful framework for fundamental theorems. It also reinforces applications in cryptography, number theory, and prime analysis.

6. Conclusion
Reformulating ζ(s) through harmonic recursive operators reveals that its zeros must obey the critical line symmetry imposed by Ω†. This establishes the Riemann Hypothesis conclusively within this new algebraic framework.

References
1. Riemann, B. “Ueber die Anzahl der Primzahlen unter einer gegebenen Grösse.” Monatsberichte der Berliner Akademie, 1859.
2. Edwards, H.M. Riemann’s Zeta Function. Academic Press, 1974.
3. Kelly, B.J. The Formal System of K-Math. K Systems and Securities, 2025.
4. Kelly, B.J. Deus Lingua: A Formal Treatise on the Axiomatic, Causal, and Harmonic Foundations of Ontological Language. K Systems and Securities, 2025.
"""


def build_pdf(output_path: Path) -> Path:
    """Render the paper to ``output_path`` and return the resulting path."""

    styles = getSampleStyleSheet()
    flowables = []

    for paragraph in FULL_TEXT.strip().split("\n\n"):
        flowables.append(Paragraph(paragraph.strip(), styles["Normal"]))
        flowables.append(Spacer(1, 12))

    doc = SimpleDocTemplate(str(output_path), pagesize=letter)
    doc.build(flowables)
    return output_path


def main() -> None:
    output_path = Path(__file__).resolve().with_name(PDF_FILENAME)
    built_path = build_pdf(output_path)
    print(f"PDF generated at: {built_path}")


if __name__ == "__main__":
    main()
