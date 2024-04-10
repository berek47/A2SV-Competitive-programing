no_english = int(input())
english_students = set(map(int, input().split()))

no_french = int(input())
french_students = set(map(int, input().split()))

total_number = len(french_students.union(english_students))
print(total_number)
