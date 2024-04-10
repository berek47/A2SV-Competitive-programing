no_english = int(input())
english_students = set(map(int, input().split()))

no_french = int(input())
french_students = set(map(int, input().split()))

unique_english_students = len(english_students.difference(french_students))
print(unique_english_students)
