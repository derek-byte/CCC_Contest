def arranging_books(books):
  book = list(books)
  swaps = 0
  j = 0
  while j < len(book):
    i = len(book) - 1

    lowest_value = "S"
    lowest_value_index = i

    while i > j:
      if book[i] < book[j]:
        if book[i] < lowest_value:
          lowest_value = book[i]
          lowest_value_index = j
        book.insert(j, book[i])
        book.pop(i+1)
        book.insert(i+1, book[j+1])
        book.pop(j+1)
        swaps += 1
      else:
        i -= 1
    j += 1

  return swaps

books = input()
print(arranging_books(books))