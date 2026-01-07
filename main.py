
from stats import word_count, char_count, sort_on
import sys
try:
    path = sys.argv[1]
except:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        
def main(path):
   print(f"============ BOOKBOT ============ \n Analyzing book found at {path}... \n ----------- Word Count ----------")
   word_count(path)
   print("--------- Character Count -------")
   char_count(path)
   print("============= END ===============")

main(path)

#print(path)
#print(sys.argv)
# path = "books/frankenstein.txt
