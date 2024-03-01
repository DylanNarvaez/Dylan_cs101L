def main():
    print("Welcome to the Text Processing Program!")
    text = input("Please input a text for analysis: ")
    print("Original input text:")
    print(text)

def word_count(text):
    word = text.split()
    return len(word)
def find_longest_word(text):
    word = text.split()
    longest_word = max(word, key = len)
    return longest_word
def count_substring(text, substring):
    count = text.count(substring)
    return count
def extract_unique_words(text):
     word = text.split()
     unique_words = list(set(word))
     return unique_words

while True:
    print("Text Analysis Options:")
    print("1. Word Count")
    print("2. Longest Word")
    print("3. Count of Substring")
    print("4. Unique Words")
    print("5. Exit")

    choice = input("Enter the number of the analysis option (1-5): ")

    if choice == '1':
        print("Word count:", word_count('word'))
    elif choice == '2':
        print("Longest Word", find_longest_word('word'))
    elif choice == '3':
        print("Count of Substring", count_substring(word, substring))
    elif choice == '4':
        unique_words = extract_unique_words('word')
        print("Unique Words", unique_words)
    elif choice == '5':
        print("Thank you for using the Text Processing Program!")
        break
    else :
        print("Invalid choice. Please choose again.")
       
    if __name__ == "__main__":
        main()
    
        
    
    
