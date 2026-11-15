import re

# =====================================================================
# TASK 2: DETERMINISTIC FINITE AUTOMATA (DFAs) - 3 SUBTASKS
# =====================================================================

# Subtask 2.1: Indian Mobile Number DFA
def is_valid_mobile(s):
    state = 0
    count = 0
    for char in s:
        if state == 0:
            if char == '+': state = 1
            elif char == '0': state = 3
            elif char in '6789': state, count = 4, 1
            else: return False
        elif state == 1:
            state = 2 if char == '9' else -1
        elif state == 2:
            state = 3 if char == '1' else -1
        elif state == 3:
            if char in '6789': state, count = 4, 1
            else: return False
        elif state == 4:
            if char.isdigit(): count += 1
            else: return False
        if state == -1: return False
    return state == 4 and count == 10

# Subtask 2.2: 24-Hour Time Format DFA (HH:MM or HH:MM:SS)
def is_valid_time(s):
    parts = s.split(':')
    if len(parts) not in [2, 3]:
        return False
    for i, p in enumerate(parts):
        if not (len(p) == 2 and p.isdigit()):
            return False
        val = int(p)
        if i == 0 and not (0 <= val <= 23): return False
        if i > 0 and not (0 <= val <= 59): return False
    return True

# Subtask 2.3: Vehicle Registration DFA
def is_valid_vehicle(s):
    if not (8 <= len(s) <= 11):
        return False
    if not (s[0:2].isalpha() and s[0:2].isupper()):
        return False
    if not (s[2:4].isdigit()):
        return False
    if not (s[-4:].isdigit() and s[-4:] != '0000'):
        return False
    middle = s[4:-4]
    return len(middle) >= 1 and len(middle) <= 3 and middle.isalpha() and middle.isupper()

# =====================================================================
# TASK 3: PUSHDOWN AUTOMATA (PDAs) & PARSING - 3 SUBTASKS
# =====================================================================

# Subtask 3.1: Balanced Brackets PDA ({ [ ( ) ] })
def is_balanced_brackets(s):
    stack = []
    mapping = {')': '(', ']': '[', '}': '{'}
    for char in s:
        if char in '([{':
            stack.append(char)
        elif char in ')]}':
            if not stack or stack[-1] != mapping[char]:
                return False
            stack.pop()
        else: 
            return False
    return len(stack) == 0

# Subtask 3.2: Even-length Palindrome PDA over {a, b}
def is_even_palindrome(s):
    if len(s) % 2 != 0 or any(c not in 'ab' for c in s):
        return False
    half = len(s) // 2
    return s[:half] == s[half:][::-1]

# Subtask 3.3: SLR(1) Dangling-Else Parser Simulation
def slr_parse_simple(s):
    print(f"Parsing Input: {s}")
    stack = []
    tokens = list(s) + ['$']
    i = 0
    while i < len(tokens):
        curr = tokens[i]
        if curr in ['i', 'a']:
            print(f"Shift: {curr}")
            stack.append(curr)
            i += 1
        elif curr == 'e':
            print("Shift: e (binding with closest 'if')")
            stack.append(curr)
            i += 1
        elif curr == '$':
            stack_str = "".join(stack)
            if stack_str in ['S', 'a']:
                print("Accepted!")
                return True
            while 'iSeS' in stack_str or 'iS' in stack_str or 'a' in stack_str:
                stack_str = stack_str.replace('iSeS', 'S').replace('iS', 'S').replace('a', 'S')
            if stack_str == 'S':
                print("Accepted!")
                return True
            else:
                print("Rejected!")
                return False
