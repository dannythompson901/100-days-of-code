def find(string):
    string = string.lower()
    letter_count = {} # empty dictionary
    for char in string:
        if char.isalpha(): # ignore any punctuation, numbers, etc
            if char in letter_count:
                letter_count[char] = letter_count[char] + 1
            else:
                letter_count[char] = 1
    
    keys = letter_count.keys()
    keys.sort()
    for char in keys:
        print(char, letter_count[char])

def main():
    string = input("Enter a sentence: ")
    find(string)
    
if __name__ == "__main__":
    main()
