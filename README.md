# Automata Assignment Implementation

This repository contains clean, simplified implementations of standard Automata assignments, focusing on Deterministic Finite Automata (DFAs), Pushdown Automata (PDAs), and Parsing algorithms.

## 🛠️ Tasks & Subtasks

### Task 2: Deterministic Finite Automata (DFAs)
1. **Subtask 2.1: Indian Mobile Number Validator**
   - Recognizes patterns like optional prefixes `+91` or `0`, followed by digits starting from 6-9 and exactly 9 trailing digits.
2. **Subtask 2.2: 24-Hour Time Format**
   - Parses and validates standard 24-hour time patterns matching `HH:MM` or `HH:MM:SS` formats.
3. **Subtask 2.3: Vehicle Registration Plates**
   - Evaluates Indian vehicle license formats step-by-step (e.g., `TN45AB1234`).

### Task 3: Pushdown Automata (PDAs) & SLR(1) Parsing
1. **Subtask 3.1: Balanced Brackets PDA**
   - Uses a stack-based algorithm to evaluate balanced `()`, `[]`, and `{}` bracket expressions.
2. **Subtask 3.2: Even-length Palindrome PDA**
   - Evaluates even-length palindrome combinations over alphabet `{a, b}` using middle-split pushdown transitions.
3. **Subtask 3.3: SLR(1) Dangling-Else Parser**
   - Simulates grammar shift-reduce parsing trace resolving the dangling-else parser conflict (matches matching `else` to inner `if`).

## 🚀 Execution & Sample Output

Executing `automata.py` yields the following verified results:

```text
=== Task 2.1: Mobile DFA ===
9876543210 -> True

=== Task 2.2: Time DFA ===
23:59:59   -> True

=== Task 2.3: Vehicle DFA ===
TN45AB1234 -> True

=== Task 3.1: PDA Brackets ===
{[()]}     -> True

=== Task 3.2: PDA Even Palindrome ===
abba       -> True

=== Task 3.3: SLR Parser ===
Parsing Input: iiaea
Shift: i
Shift: i
Shift: a
Shift: e (binding with closest 'if')
Shift: a
Accepted!
```
