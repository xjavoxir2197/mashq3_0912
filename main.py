# 1 - misol
reversed_words = [w[::-1] for w in ["car", "bike", "bus"]]
print(reversed_words)

# 2 - misol
double_nums = [n*2 for n in [1,2,3,4]]
print(double_nums)

# 3 - misol
high_scores = [s for s in [65, 85, 45, 95, 70] if s > 70]
print(high_scores)

# 4 - misol
letters_only = [w for w in ["hello","123","world","456"] if w.isalpha()]
print(letters_only)

# 5 - misol
mod1_numbers = [n for n in range(1,21) if n % 3 == 1]
print(mod1_numbers)

# 6 - misol
even_odd = ["juft" if n % 2 == 0 else "toq" for n in [1, 2, 3, 4, 5]]
print(even_odd)
