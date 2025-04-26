# ✅ Day 14 of #gfg160 - String to Integer (atoi)
## 🧠 Problem:
Implement the atoi function, which converts a string into an integer following these rules:

1. Ignore leading whitespaces.

2. An optional '+' or '-' sign should be handled.

3. Read digits until a non-digit character is encountered.

4. If the result exceeds the 32-bit signed integer range, clamp it within the limits.

## 📜 Steps to Solve:
1. Trim leading whitespace using .strip().

2. Detect sign (+ or -) and adjust accordingly.

3. Extract digits and build the number.

4. Clamp the result between -2³¹ and 2³¹ - 1 for 32-bit signed integers.

## ✅ Edge Cases Handled:

1. Empty strings

2. Only whitespace

3. Strings without numbers

4. Overflow/Underflow cases

---
## 🔖 Hashtags:
#Day14 #gfg160 #geekstreak2025 #python #dsa #leetcode #100DaysOfCode #stringprocessing #atoi #cleanCode #devcommunity #codingjourney #vscode #coderlife

## ✨ Forward-looking suggestion:
