class WordCloudData(object):
    """ Problem: You want to build a word cloud, an infographic where the size of a word corresponds to how often it appears in the body of text.
        Example: 
        Input: "We came, we saw, we ate cake."
        Output: {"we": 3, "came": 1, "saw": 1, "ate": 1, "cake": 1}
        Complexity: O(n) space and time complexity

    """

    def __init__(self, input_string):
        self.words_to_counts = {}
        self.populate_words_to_counts(input_string)


    def populate_words_to_counts(self, input_string):
        """ iterates over each character in the input string, splits the words removing any punctuation
            and populate the words to counts dictionary """ 

        current_word = ""
        
        for i in xrange(len(input_string)):
            character = input_string[i]

            # Reached the end of the input string and add last word to dictionary
            if i == len(input_string) - 1:
                if self.is_letter(character):
                    current_word += character

                if current_word:    
                    self.add_word_to_dictionary(current_word) 

            # Reached a space or emdash which means its end of a word. We then add it
            # to our dictionary and reset the current word        
            elif character == " " or character == u'\u2014':
                if current_word:
                    self.add_word_to_dictionary(current_word)

                current_word = ""


            # if we get 2 periods in a row, add the current word to the dictionary and reset 
            # the current word    
            elif character == ".":
                if i < len(input_string) - 1 and input_string[i+1] == ".":
                    if current_word:
                        self.add_word_to_dictionary(current_word)
                    current_word = "" 


            # if the character is a letter or an apostrophe, we add it to our current word        
            elif self.is_letter(character) or character == "\'":
                current_word += character  


            # check if the character is a hyphen surrounded by letters, if so add it to our current word    
            elif character == "-":
                if i > 0 and self.is_letter(input_string[i-1]) and self.is_letter(input_string[i+1]):
                    current_word += character                 
                              


    def is_letter(self, character):
        """ Returns true if the character is an alphabet"""

        return character.lower() in "abcdefghijklmnopqrstuvwxyz"


    def add_word_to_dictionary(self, word):
        """ adds a word to dictionary along with its count """

        # if word already in dictionary, we increment its count
        if word in self.words_to_counts:
            self.words_to_counts[word] += 1

        # if a lowercase version of our word is in dictionary,
        # then we know our current word is uppercase, we just increment the 
        # count of the lowercase version    
        elif word.lower() in self.words_to_counts:
            self.words_to_counts[word.lower()] += 1

        # if a capitalized version of the word is already in dictionary,
        # current word is lowercase then remove the capital version and add its
        # count to the lower case version count in the dictionary    
        elif word.capitalize() in self.words_to_counts:
            self.words_to_counts[word] = 1
            self.words_to_counts[word] += self.words_to_counts[word.capitalize()]
            del self.words_to_counts[word.capitalize()] 

        # word is not in the dictionary at all and we add it    
        else:
            self.words_to_counts[word] = 1                 


# Tests and driver program
input_data = "We came, we saw, we ate cake."
wd = WordCloudData(input_data)
print wd.words_to_counts

new_data = "We came, we saw, we conquered...then we ate Bill's (Mille-Feuille) cake."
wd = WordCloudData(new_data)
print wd.words_to_counts


if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()

    if not result.failed:
        print "All tests passed. Good work!"

    print                 
                