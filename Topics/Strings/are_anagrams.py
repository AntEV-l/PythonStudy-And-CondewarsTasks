def are_anagrams(s1, s2):
    s1 ="".join(sorted(s1)).lower().split()
    s2 ="".join(sorted(s2)).lower().split()
    return True if s1 == s2 else False

print(are_anagrams("listen", "silent"))