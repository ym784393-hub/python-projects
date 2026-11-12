#step 1
library=[]
wishlist=[]
#step 2 Adding
book_name=input("Enter the name of a book you own :")
library.append(book_name)
book_name=input("Enter the name of another book you own (or press 'Enter' to skip :)")

if book_name:
    library.append(book_name)
print("\n your library :", library)
# step3 : managing the wishlist
book_name=input("\n Enter the name of a book you wish to have in the future :")
wishlist.append(book_name)
book_name=input("\n Enter the name of a book you wish to have (or press 'Enter' to skip :)")
if book_name:
    wishlist.append(book_name)
    print("\n your wishlist ", wishlist)
# step 4 merging into library
book_1=input("\n Enter the name of a book from your wishlist that you've acquired (or press 'Enter' to skip :)")
if book_1 in wishlist :
    library.append(book_1)
    wishlist.remove(book_1)
print("\n updated library:", library)
print("\n updated wishlist :", wishlist)
#step5
book_2=input("\n Enter the name of a book from your library you  to donate ( or press 'Enter' to skip:)")
if book_2 in library:
    library.remove(book_2)
print("\n final library after Donations:", library)
