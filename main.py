# AIM: Develop a Python program that reads a text file and 
# prints words of specified lengths (e.g., three, four, 
# five, etc.) found within the file.
# Coder: Aayan Khan
# Date:11-02-2026

print("--- Extracting Words from Text File ---")

n = int(input("\nEnter Length of Words: "))

f = open("story.txt", "r")
text = f.read()
f.close()

words = text.lower().split()
unique = []

for w in words:
    if len(w) == n and w not in unique:
        unique.append(w)

unique.sort()

print("\nWords with length", n, "are:", unique)



