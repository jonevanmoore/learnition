import os
path = '/Users/jonmoore/Desktop/book_research'
os.chdir(path)
open("books.txt", "a").close()
try:
    os.mkdir("Topics"); os.mkdir("Books")
except:
    pass

starting = open("books.txt")
start = starting.read().split("\n")
start.pop()
if len(start) == 0:
    print("\nMemorizing is not enough.")
    print("If you can't articualte a subject in 10 different ways, you don't understand it")
    print("\nWelcome to Learnition")
    print("This app is designed to teach you how to:")
    print("""
    1. Express your ideas more clearly
    2. Have a better understanding of the books you read\n
    """)
    print("For now let's add some books")
    input("Press enter to start\n")
elif len(start) > 0:
    print("\nWelcome back to Learnition")
    input("Press enter to begin\n")
starting.close()

def study_book():
    global book
    book_list = open("books.txt")
    book_titles = book_list.read().split("\n")
    book_titles.pop()
    if len(book_titles) > 0:
        if len(book_titles) == 1:
            print("You already have a book saved.")
            print(f"1. {book_titles[0]}")
            print("\nWould you like to study this book or add a new one?")
        else:
            num = 0
            print("You already have some books saved\n")
            for bt in book_titles:
                num += 1
                print(f"{num}. {bt}")
            print("\nWould you like to study one of these or add a new book?")
        study_add = input("""
1. Study
2. Add
> """)
        while study_add not in ("1", "2", "study", "Study", "add", "Add"):
            print("\nThat is not one of the options")
            study_add = input("> ")
        if study_add in ("study", "Study", "1"):
            print("\nPlease choose one of the following books:")
            num = 0
            for bt in book_titles:
                num += 1
                print(f"{num}. {bt}")
            while True:
                try:
                    choose_book = book_titles[int(input("> ")) - 1]
                    break
                except:
                    print("That's not an option")
                    continue
            book = choose_book
            print(f"\nOpening {book}\n")
            begin_studying()
        elif study_add in ("add", "Add", "2"):
            print("\nWhat is the title of your new book?\n")
            new_book = input("> ")
            book = new_book
            os.makedirs(os.path.join("Books", f"{book}"))
            book_list = open("books.txt", "a")
            book_list.write(f"{book}\n")
            book_list.close()
            open(f"Books/{book}/passages.txt", "a").close(); open(f"Books/{book}/reworded.txt", "a").close(); os.makedirs(os.path.join('Books', f"{book}", 'Topics'))
            print(f"\nOpening {book}\n")
            print("Just a reminder that every new book added automatically comes with 2 text files.")
            print("One for saving passages and the other for writing them in your own words.\n")
            begin_studying()
    elif len(book_titles) <= 0:
        print("Enter as many titles as you want")
        print("When you're done, type \"done\"\n")
        while True:
            new_book = input("> ")
            if new_book in ("done", "Done"):
                break
            book = new_book
            os.makedirs(os.path.join("Books", f"{book}"))
            book_list = open("books.txt", "a")
            book_list.write(f"{book}\n")
            book_list.close()
            book_list = open("books.txt")
            book_titles = book_list.read().split("\n")
            book_titles.pop()
            open(f"Books/{book}/passages.txt", "a").close(); open(f"Books/{book}/reworded.txt", "a").close(); os.makedirs(os.path.join('Books', f'{book}', 'Topics'))
        print("Now that you have your books, please pick one to study\n")
        num = 0
        for bt in book_titles:
            num += 1
            print(f"{num}. {bt}")
        choose_book = book_titles[int(input("> ")) - 1]
        book = choose_book
        print(f"\nOpening {book}\n")
        print("Just a reminder that every new book added automatically comes with 2 text files.")
        print("One for saving passages and the other for writing them in your own words.\n")
        begin_studying()

def begin_studying():
    global chosen_passage
    global new_chosen_passage
    global topic
    global page_number
    print("Let's begin by adding a new passage.")
    print("Or you can choose one that you have previously added.")
    add_choose = input("""
1. Add
2. Choose
""").lower()
    while add_choose not in ("add", "Add", "choose", "Choose", "1", "2"):
        print("\nThat's not an option")
        add_choose = input("> ")
    if add_choose in ("add", "Add", "1"):
        passages = open(f"Books/{book}/passages.txt", "a")
        print("Begin writing")
        print("(Feel free to use multiple line. Press return on empty line when finished)")
        new_passage = []
        passage_lines = input("")
        while passage_lines not in "":
            new_passage.append(passage_lines)
            passage_lines = input("")
        topic = input("\nTopic: ").lower()
        page_number = input("Pager number: ")

        new_passage.insert(0, f"p.{page_number} | Topic: {topic}")

        #Add passage to passage file
        for np in new_passage:
            passages.write(f"{np}\n")
        passages.write("_______________________________________\n")
        passages.close()
        new_chosen_passage = new_passage
        #Add passage under chosen topic file
        topic_file = open(f"Books/{book}/Topics/{topic}.txt", "a")
        for ncp in new_chosen_passage:
            topic_file.write(f"{ncp}\n")
        topic_file.write("_______________________________________\n")
        topic_file.close()
        paraphrase()
    elif add_choose in ("choose", "Choose", "2"):
        passages = open(f"Books/{book}/passages.txt")
        passage_list = passages.read().split("_______________________________________\n")
        passage_list.pop()
        if len(passage_list) == 0:
            passages.close()
            passages = open(f"Books/{book}/passages.txt", "a")
            print("You do not have any passages yet.")
            print("Write a new one to get started.")
            print("(Feel free to use multiple line. Press return on empty line when finished)")
            new_passage = []
            passage_lines = input("")
            while passage_lines not in "":
                new_passage.append(passage_lines)
                passage_lines = input("")
            topic = input("\nTopic: ").lower()
            page_number = input("Pager number: ")
            #Add passage to passage file
            passages.write(f'p.{page_number} | topic: {topic}\n')
            for np in new_passage:
                passages.write(f"{np}\n")
            passages.write("_______________________________________\n")
            passages.close()
            chosen_passage = new_passage
            #Add passage under chosen topic file
            topic_file = open(f"Books/{book}/Topics/{topic}.txt", "a")
            for cp in chosen_passage:
                topic_file.write(f"{cp}\n")
            topic_file.write("_______________________________________\n")
            topic_file.close()
            paraphrase()
        elif len(passage_list) > 0:
            #CREATE PAGE NUMBER
            print("")
            num = 0
            for pl in passage_list:
                num += 1
                pl.split("\n")
                print(f"{num}.) \n{pl}")
            while True:
                try:
                    chosen_passage = passage_list[int(input("> ")) - 1]
                    break
                except:
                    print("That's not an option")
                    continue
            print(f"\n{chosen_passage}")
            global temp_var
            temp_var = chosen_passage.split("\n")
            page_and_topic = temp_var[0].split(" | ")
            page = page_and_topic[0].split("p."); page.pop(0)
            page_number = page[0]
            topic = page_and_topic[1].split(": "); topic.pop(0)
            topic = topic[0]
            del temp_var[0], temp_var[-1]
            paraphrase()

def paraphrase():
    print("\nNow that we have the passage, it's time to write it in your own words")
    print("10 different times")
    input("\nPress enter when you're ready")
    try:
        chosen_passage_list = temp_var
    except:
        chosen_passage_list = new_chosen_passage
        del chosen_passage_list[0]
    print("\nParaphrase:\n\"", end='')
    for cpl in chosen_passage_list:
        if cpl != chosen_passage_list[-1]:
            print(cpl)
        else:
            print(f"{cpl}\"\n\n")
    num = 0
    pick_fav = [[] for i in range(10)]
    my_paraphrasing = []
    for i in range(10):
        num += 1
        print(f"{num}. ")
        while True:
            reworded = input("")
            if reworded != "":
                my_paraphrasing.append(reworded)
                continue
            elif reworded == "":
                pick_fav[num - 1].append(my_paraphrasing)
                my_paraphrasing = []
                break

    print("\nNow it's time to pick your favorite one\n")
    input("Press enter when you're ready")
    own_words = open(f"Books/{book}/reworded.txt", "a")
    own_words.write(f"""Original passage:
Page {page_number} | Topic: {topic}\n\n""")
    for cpl in chosen_passage_list:
        if cpl == chosen_passage_list[0]:
            print(f"\"{cpl}\n")
        elif cpl != chosen_passage_list[-1]:
            own_words.write(f"{cpl}\n")
        else:
            own_words.write(f"{cpl}\"\n\n")
    own_words.write("Reworded 10x:\n\n")
    num = 0
    for pf in pick_fav:
        for f in pf:
            num += 1
            if num == 1:
                own_words.write(f"{num}. ")
                print(f"{num}.")
            else:
                own_words.write(f"\n{num}.")
                print(f"\n{num}.")
            for p in f:
                own_words.write(f"{p}\n")
                print(f"{p}")
    own_words.write("\n------------------------------------\n\n")
    while True:
        try:
            fave = pick_fav[int(input("> ")) - 1]
            break
        except:
            print("Numerical options only")
            continue
    faveL = []
    for f in fave:
        for p in f:
            faveL.append(p)
    myTopic = open(f"Topics/{topic}.txt", "a")
    myTopic.write(f"""Paraphrased from: {book} | Page: {page_number}\n""")
    for f in faveL:
        myTopic.write(f"{f}\n")
    myTopic.write("\n------------------------------------\n\n")
    print("Great work!")
    print("Now that you're done, you still have some options.")
    options = input("""
1. I'm done writing
2. Let's add a new passage
3. Write a shorter version of a passage
4. Turn a passage into an essay""")
    #CONTINUE HERE

study_book()
