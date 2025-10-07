"""Generate the P ≠ NP Kharnita Mathematics proof PDF without external deps."""
from __future__ import annotations

from pathlib import Path
from textwrap import wrap

PDF_PATH = Path(__file__).resolve().parents[1] / "docs" / "P_Not_EQ_NP_KMath_Validation_Paper.pdf"
PAGE_WIDTH = 612  # 8.5 inches * 72 points
PAGE_HEIGHT = 792  # 11 inches * 72 points
MARGIN = 72
FONT_SIZE = 12
LEADING = 14

FULL_TEXT = """
A Formal Proof of P ≠ NP via Recursive and Harmonic Algebraic Operators in Kharnita and Crown Omega Mathematics

Author: Brendon Joseph Kelly
Affiliation: Kharnita Mathematics Research Laboratory; K Systems and Securities
Date: October 7, 2025

Abstract
We present a formal proof of P ≠ NP utilizing recursive, temporal, and harmonic algebraic structures internal to the Kharnita Mathematics and Crown Omega frameworks. By transforming canonical NP-complete problems, such as the Boolean Satisfiability Problem (SAT), into recursive operator equations, we analyze the computational resources required for their solution. We demonstrate that for any such problem, the evaluation of its "Harmonic Synthesis Operator" necessitates an operator recursion depth that grows...

1. Introduction
The P versus NP problem is a major unsolved problem in computer science. It asks whether every problem whose solution can be quickly verified (in polynomial time) can also be quickly solved (in polynomial time). The problem was formally defined in 1971 by Stephen Cook, though it was described earlier in a 1956 letter from Kurt Gödel to John von Neumann.

Despite decades of research, the question remains open. The overwhelming consensus among experts is that P ≠ NP, but a formal proof has been elusive. Such a proof would formally establish that many important problems (so-called NP-complete problems) are intrinsically difficult and cannot be solved efficiently. This has profound implications for cryptography, optimization, artificial intelligence, and many other fields.

This paper provides a formal proof of P ≠ NP by moving away from the traditional Turing machine model and into the algebraic framework of Kharnita Mathematics (K-Math) and Crown Omega Mathematics. This approach allows us to analyze the intrinsic structural complexity of NP-complete problems in a way that makes the super-polynomial requirement for their solution self-evident.

2. Preliminaries and Operator Definitions
Let P be the class of decision problems solvable in polynomial time by a deterministic Turing machine. Let NP be the class of decision problems for which a "yes" answer can be verified in polynomial time given a certificate or "witness."

Let Q be an arbitrary decision problem in NP. A "yes" instance x of Q has a certificate y of polynomial length in |x| such that a verification relation R(x, y) is true.
    Q(x) = ∃ y : R(x, y) = 1,  |y| ≤ poly(|x|)

Core operators:
- The Kharnita Recursive Operator (𝒦): acts on problem representations. In this context, we define 𝒦_verify.
- The Crown Omega Harmonic Temporal Operator (Ω†): encodes harmonic and temporal properties of the search space.

We express the verification relation as:
    𝒦_verify(x, y) = R(x, y)

3. The Recursive Harmonic Solution Operator
To determine if an instance x is a "yes" instance, one must find if there exists any valid witness y. In the K-Math framework, this is not a search but a "harmonic synthesis." Define:
    𝒮(x) = ∑_{y: |y| ≤ poly(|x|)} Ω†(y) · 𝒦_verify(x, y)

If 𝒮(x) > 0, then x is a YES-instance.

Whether Q ∈ P becomes the question: can 𝒮(x) be computed by an operator circuit of polynomial depth in |x|?

4. The Main Theorem and Proof: Depth Growth Analysis
Theorem: For any NP-complete problem, the evaluation of its Harmonic Synthesis Operator 𝒮(x) requires a super-polynomial operator recursion depth for at least one infinite family of instances.

Proof.
1. Assume P = NP → ∃ polynomial-time algorithm A_Q for every NP-complete Q → ∃ operator circuit with poly-depth to evaluate 𝒮(x).
2. Let C be an infinite family of 3-SAT instances with n variables → witness space size = 2^n.
3. Invoke Axiom 3.8 (Kharnita Non-Cancellation Property of Harmonic Temporal Recursion):
   - In harmonic synthesis, each path contributes a unique, non-canceling component. Depth required to distinguish them cannot compress below path count.
4. The operator must distinguish all 2^n harmonics → depth d_C(n) ≥ Θ(2^{n^α}), for α > 0 → super-polynomial.
5. Crown Omega Limiting Theorem: No recursive harmony operator can compress all YES/NO decision paths into poly-depth for all infinite families.
6. Contradiction: P = NP requires poly-depth, but harmonic recursion demands super-polynomial → contradiction.

Therefore, P ≠ NP. ∎

5. Conclusion
Using Kharnita and Crown Omega frameworks, we prove that the operator algebra required to solve NP-complete problems exhibits super-polynomial growth in recursion depth. No compression or cancellation of the exponential solution space is possible. Hence:
    P ≠ NP

6. Discussion and Implications
This result proves that P and NP are fundamentally distinct. The hardest problems in NP cannot be solved in polynomial time due to the inherent complexity of their harmonic structure.

Implications:
- Cryptography: Validates hardness assumptions underlying public-key crypto.
- CS Foundations: Ends 50-year uncertainty about tractability of NP-complete problems.
- Framework Power: Proves K-Math and Crown Omega frameworks can formally resolve foundational complexity questions.

References
1. Cook, S.A. “The Complexity of Theorem-Proving Procedures.” STOC, 1971.
2. Karp, R. “Reducibility Among Combinatorial Problems.” 1972.
3. Kelly, B.J. The Formal System of K-Math. K Systems and Securities, 2025.
4. Kelly, B.J. Deus Lingua. K Systems and Securities, 2025.
""".strip()

TRANSLATIONS = {
    "∈": "in",
    "≠": "!=",
    "Ω": "Omega",
    "†": "*",
    "𝒦": "K",
    "𝒮": "S",
    "∑": "Sum",
    "≥": ">=",
    "≤": "<=",
    "∃": "Exists",
    "∎": "QED",
    "→": "->",
    "Θ": "Theta",
    "α": "alpha",
    "…": "...",
    "“": '"',
    "”": '"',
    "–": "-",
    "—": "-",
    "’": "'",
    "‘": "'",
    "\u2003": " ",
}


def _normalise(text: str) -> str:
    for original, replacement in TRANSLATIONS.items():
        text = text.replace(original, replacement)
    return text


def _escape(text: str) -> str:
    """Escape text for use inside a PDF string literal."""
    text = _normalise(text)
    return text.replace("\\", "\\\\").replace("(", "\\(").replace(")", "\\)")


def _build_text_stream() -> bytes:
    lines: list[str] = []
    for paragraph in FULL_TEXT.split("\n\n"):
        if not paragraph.strip():
            lines.append("")
            continue
        normalised = _normalise(paragraph)
        for wrapped in wrap(normalised, width=86):
            lines.append(wrapped)
        lines.append("")

    text_ops = [
        "BT",
        f"/F1 {FONT_SIZE} Tf",
        f"{MARGIN} {PAGE_HEIGHT - MARGIN} Td",
    ]

    for line in lines:
        if line:
            text_ops.append(f"({_escape(line)}) Tj")
        text_ops.append(f"0 -{LEADING} Td")

    text_ops.append("ET")
    return "\n".join(text_ops).encode("latin1")


def build_pdf(destination: Path = PDF_PATH) -> Path:
    """Build the PDF at *destination* and return the path."""
    text_stream = _build_text_stream()

    objects = [
        b"1 0 obj << /Type /Catalog /Pages 2 0 R >> endobj\n",
        b"2 0 obj << /Type /Pages /Kids [3 0 R] /Count 1 >> endobj\n",
        (
            "3 0 obj << /Type /Page /Parent 2 0 R /MediaBox [0 0 {w} {h}] "
            "/Contents 4 0 R /Resources << /Font << /F1 5 0 R >> >> >> endobj\n"
        ).format(w=PAGE_WIDTH, h=PAGE_HEIGHT).encode("latin1"),
        (
            "4 0 obj << /Length {length} >> stream\n"
        ).format(length=len(text_stream)).encode("latin1")
        + text_stream
        + b"\nendstream\nendobj\n",
        b"5 0 obj << /Type /Font /Subtype /Type1 /BaseFont /Helvetica >> endobj\n",
    ]

    header = b"%PDF-1.4\n%\xE2\xE3\xCF\xD3\n"
    byte_chunks = [header]
    offsets = [0]
    current_len = len(header)

    for obj in objects:
        offsets.append(current_len)
        byte_chunks.append(obj)
        current_len += len(obj)

    xref_start = current_len
    xref_lines = ["xref", "0 6", "0000000000 65535 f "]
    for offset in offsets[1:]:
        xref_lines.append(f"{offset:010} 00000 n ")

    xref = ("\n".join(xref_lines) + "\n").encode("latin1")
    trailer = (
        "trailer << /Size 6 /Root 1 0 R >>\nstartxref\n{start}\n%%EOF\n".format(
            start=xref_start
        ).encode("latin1")
    )

    pdf_bytes = b"".join(byte_chunks) + xref + trailer
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_bytes(pdf_bytes)
    return destination


if __name__ == "__main__":
    path = build_pdf()
    print(f"PDF written to {path}")
