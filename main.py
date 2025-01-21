def count_characters(text):
    characters ={ }
    text = text.lower()
    
    for i in range (0,len(text)):
        if text[i] != ' ' and text[i] !='.' and text[i] !='#':
            if text[i] in characters:
                characters[text[i]] += 1 
            else:
                characters[text[i]] = 1
    return characters

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    length = len(file_contents.split())
    dictionary_of_characters = count_characters(file_contents)
    return length, dictionary_of_characters


len, dict = main()
print("--- Begin report of books/frankenstein.txt ---")
print (len ," words found in the document")
for element in dict:
    print(f"The '{element}' character was found {dict[element]} times")

