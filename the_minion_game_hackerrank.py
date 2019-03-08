s = input()


kevin_score = 0
stuart_score = 0
for i in range(len(s)):
    if s[i] in "AEIOUaeiou":
        kevin_score += (len(s)-i)
    else:
        stuart_score += (len(s)-i)

if kevin_score > stuart_score:
    print(f"Kevin {kevin_score}")
elif kevin_score < stuart_score:
    print(f"Stuart {stuart_score}")
else:
    print("Draw")