#%% Question 1
def long_word(word_list):
    longest = ""
    tied_longest = ""
    for i in word_list:
        if len(i) > len(longest):
            longest = i
        elif len(i) == len(longest):
            tied_longest = i
    print("The longest word(s): " + longest + " and " + tied_longest)
long_word(["apple", "chestnut", "gargoyle", "pandas", "sheep", "raptor"])
#%% Question 2
import random
new_list = []
def word_generator():
    with open("/Users/emilyshaw/Documents/HARP 151/Practice/words.txt") as readfile:
        words = readfile.readlines()
        readfile.close()
        return random.choice(words).strip()
for i in range(0,7):
    word = word_generator()
    if word not in new_list:
        new_list.append(word)
long_word(new_list)
#%% Question 3- Library Book Prep dictionary
def process_books(book_prep):
    books_ready.update(book_prep)

circ_books = {"The Grapes of Wrath" : "John Steinbeck", "The Catcher in the Rye" : "J. D. Salinger", "To Kill a Mockingbird" : "Harper Lee", "Fahrenheit 451" : "Ray Bradbury", "1984" : "George Orwell"}
new_books = {"Spare" : "Prince Harry", "Fair Lady Fortune" : "Chloe Gong", "Chain of Thorns" : "Cassandra Clare"}
books_ready = {}
print("There are " + str(len(new_books)) + " new books ready for book prep.")
new_titles = new_books.keys()
print(circ_books)
process_books(new_books)
print("There are " + str(len(books_ready)) + " books ready for circulation.")

#%% Question 4
#Parent class could be a student and a child class could be student employee, since it would have the same parameters only adding parameters related to working
#Methods could determine gpa, bmail, and standing. Child method could calculate weekly salary.
class Student():
    def __init__(self, first_name, last_name, credits, grades):
        self.first_name = first_name
        self.last_name = last_name
        self.credits = credits
        self.grades = grades
    
    def bmail(self):
        Bmail = self.first_name[0].lower() + self.last_name[0:6].lower() + "@binghamton.edu"
        print(Bmail)

    def standing(self): 
        if self.credits <= 30:
            standing = "Freshman"
        elif 30 < self.credits <= 60:
            standing = "Sophomore"
        elif 60 < self.credits < 90:
            standing = "Junior"
        else:
            stand = "Senior"
        print(self.first_name + " " + self.last_name + " is a " + standing + " with " + str(self.credits) + " credits.")
    
    def gpa(self):
        grade_sum = sum(self.grades.values())
        average = grade_sum/len(self.grades)
        print(average)
    
class Student_Employee(Student):
    def __init__(self, first_name, last_name, credits, grades, hourly_wage, hours_per_week):
        super().__init__(first_name, last_name, credits, grades)
        self.hourly_wage = hourly_wage
        self.hours_per_week = hours_per_week

    def weekly_salary(self):
        week = self.hourly_wage * self.hours_per_week
        print(week)

S1 = Student_Employee("Emily", "Shaw", 72, {"CHEM 443" : 95, "HARP 151" : 100, "CHEM 221" : 85, "CHEM 397" : 95}, 14.20, 5)
S1.bmail()
S1.standing()
S1.gpa()
S1.weekly_salary()
#%% Question 5
import random 
worddict = {}
def word_dict(word):
    for i in word:
        if i not in worddict.keys():
            worddict[i] = 1
        else:
            worddict[i] +=1


words = ["lop", "bowl", "trunk", "bed", "not"]
game = input("Would you like to play Hangman? (y/n)")
word_letters = []
if game == "n":
    print("Ok! Goodbye!")
elif game == "y":
    while game == "y":
        word_choice = random.choice(words)
        word_dict(word_choice)
        for i in word_choice:
                word_letters.append(i)
        playing = 1
        while playing == 1:
            alphabet = ["q","w","e","r","t","y","u","i","o","p","a","s","d","f","g","h","j","k","l","z","x","c","v","b","n","m"]
            guess = input("Pick a letter: ")
            if guess in alphabet:
                if guess in word_choice:
                    print("Yes! there is/are "+ str(worddict[guess]) + " " + guess + "(s) in the word")
                    word_letters.remove(guess)
                    if len(word_letters) == 0:
                        print("Nice! You win!")
                        playing = 2
                    else:
                        alphabet.remove(guess)
                else:
                    print("Womp womp :( guess again!")
                    alphabet.remove(guess)
            else:
                print("You've already guessed that! Guess again!")
        while playing == 2:
            game = input("Would you like to play again? (y/n)")
            playing = 3
        while playing == 3:
            if game == "n":
                print("Ok! Goodbye!")
                playing = 0
            else:
                if len(words) == 0:
                    print("Sorry! No more words to play with! Goodbye!")
                    playing = 0
                else:
                    playing = 1

    # %%
