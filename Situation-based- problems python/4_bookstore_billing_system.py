books=[20, 50, 10, 30, 100]
final_amount=0
for each_book in books:
    if each_book>=50:
        each_book-=10
        final_amount+=each_book
    else:
        final_amount+=each_book

print(f"Cost of all 5 books:{final_amount}.rs")