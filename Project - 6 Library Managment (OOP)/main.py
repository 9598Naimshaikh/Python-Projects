# Library Management System


class Library(object):

  def __init__(self):
    self.no_of_books = 0
    self.books = []

  def add_books(self, books):
    self.books.append(books)
    self.no_of_books += 1

  def get_no_books(self):
    return f'Total books in the library are: {self.no_of_books}'

  def show_books(self):
    print('\nAvailable books in this Library...')
    for index, book in enumerate(self.books, start=1):
      print(index, book)


lib1 = Library()

if __name__=='__main__':
  # add some books allready in library class..
  lib1.add_books("Harry Potter")
  lib1.add_books('Jonsen Story')
  lib1.add_books('Clean Code')

  user_name = input("Enter Your Name: ")
  print(f'....Welcome to this LIBRARY...{user_name}.')
  while True:
    print('\nWhat do you want to do ?\nOptions..')
    options = ['(a). Add Books', '(b). Show Books', '(c). Get the Number of Books', '(d). Quit the program.']
    for option in options:
      print(option)

    user_choice = input("Please choose (a, b, c, d) $$: ")
    if user_choice.lower() == 'a':
      user_add_book = input('\nEnter a book which do you want to add $$: ')
      lib1.add_books(user_add_book)
      print('🥳Congratulations your books successful added this library.')

    elif user_choice.lower() == 'b':
      lib1.show_books()

    elif user_choice.lower() == 'c':
      print(lib1.get_no_books())
    
    elif user_choice.lower() == 'd':
      print('Thanks for quiting the program...')
      break
