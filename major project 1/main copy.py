import flet as ft
import json

# two json files are needed, login_info with {} and storage with []

# to do list
# finish questionaire button to collect data (more questions and stuff)
# figure out algorithm stuff
# compress the retrive data function

#Major Project 1: The Haunted Dates

#Abstract:
#	You are to create a simple app that can collect 
# and store inputs from different users regarding their 
# age, gender, personality information, hobbies, and a few well 
# designed questions that you think are crucial to a successful date. 
# Then, based on different users’ input, your app will generate date 
# matches for all existing users. 

#Basic Requirements (Not in order):

#Your app should have multiple distinctive pages for this program. Log-in and register, 
# main menu, answer questions, and generating matches. 
#When collecting user info, your app must ask at least 10 survey-like 
# questions for each user including their first name, last name, age, 
# gender, personality traits, hobbies, and other key questions. The 
# questions should all be in multiple choices or true or false. All 
# the information for a single user should be stored inside a python dictionary/list. 

#Your app should be able to write all the stored user info into a json or text file to store 
# it. Your app should also be able to read all the stored user info 
# from a text file to load all the stored information. Make sure your 
# program can run based on the stored information. 
#The challenging part of this project is for you to figure out a reasonable/functioning 
# algorithm which can match different users based on the information they provided. You 
# should not match users with conflicting personalities or interests. And your app should 
# always try to generate the best match for each person. (Hint: you might want to create 
# some kind of score system to mathematically keep track of how well the two users match 
# each other. This score system can be based on how many similar answers they give from 
# the user's questions. 

people = []
valid_logins = {}

# probably could move this into a dictionary, or json file
questions_labels_values = [
    ["How much do you like video games?", "Strongly Agree", "Agree", "Neutral", "Disagree", "Strongly Disagree"],
    ["How much do you like books?", "Strongly Agree", "Agree", "Neutral", "Disagree", "Strongly Disagree"],
    ["How much do you like The outside?", "Strongly Agree", "Agree", "Neutral", "Disagree", "Strongly Disagree"],
    ["How much do you like School?", "Strongly Agree", "Agree", "Neutral", "Disagree", "Strongly Disagree"],
    ["What is your Favorite Subject?", "Math", "Comp Sci", "Physiscs", "Chemistry", "English"],
    ["how much do you like sports?", "They are a cornerstone of my being", "alot", "Neutral", "They don't affect me", "I find them boring"],
    ["Do you like computers?", "Strongly Agree", "Agree", "Neutral", "Disagree", "Strongly Disagree"],
    ["how much do you like to sleep?", "Strongly Agree", "Agree", "Neutral", "Disagree", "Strongly Disagree"],
    ["Do you like to remeber?", "Strongly Agree", "Agree", "Neutral", "Disagree", "Strongly Disagree"],
    ["how much do you like comic books?", "Strongly Agree", "Agree", "Neutral", "Disagree", "Strongly Disagree"]
]

atributes = [
    "game", "book", "subject", "outdoor", "school", "sports", "computers", "sleep", "remember", "comic"
    ]


def rangel(x):
    return range(len(x))

class person:
    def __init__(self, 
                username, age = "", name = "", 
                f_game = None, f_book = None, school = None, f_subject = None, f_outdoor = None,
                sports = None, computers = None, sleep = None, remember = None, comic = None
                ):
        self.username = username
        self.age = age
        self.name = name
        self.stats = {
            "game": f_game,
            "book": f_book,
            "subject": f_subject,
            "outdoor": f_outdoor,
            "school": school,
            "sports": sports,
            "computers": computers,
            "sleep": sleep,
            "remember": remember,
            "comic": comic,
        }

        #.stats[atributes[]]

# these functions are for storing user data (age, name, etc)
def store_data():
    to_be_stored = []
    for x in rangel(people):
        compressed_object = {
            "username": people[x].username,
            "age": people[x].age,
            "name": people[x].name,
            atributes[0]: people[x].stats[atributes[0]],
            atributes[1]: people[x].stats[atributes[1]],
            atributes[2]: people[x].stats[atributes[2]],
            atributes[3]: people[x].stats[atributes[3]],
            atributes[4]: people[x].stats[atributes[4]],
            atributes[5]: people[x].stats[atributes[5]],
            atributes[6]: people[x].stats[atributes[6]],
            atributes[7]: people[x].stats[atributes[7]],
            atributes[8]: people[x].stats[atributes[8]],
            atributes[9]: people[x].stats[atributes[9]]
        }
        to_be_stored.append(compressed_object)
        compressed_object = None

    with open("storage.json", "w") as f:
        data = json.dump(to_be_stored, f, indent= 4)

def retrive_data():
    data = None
    with open("storage.json", "r") as f:
        data = json.load(f)

    for x in rangel(data):
        people.append(person(
            data[x]["username"],
            data[x]["age"], 
            data[x]["name"], 
            data[x][atributes[0]], 
            data[x][atributes[1]],
            data[x][atributes[2]], 
            data[x][atributes[3]], 
            data[x][atributes[4]], 
            data[x][atributes[5]],
            data[x][atributes[6]], 
            data[x][atributes[7]], 
            data[x][atributes[8]], 
            data[x][atributes[9]]))

# these functions are for storing user login information, they are connected to user data by the username
# don't ask why they are seperate, its for security
def load_logins():
    valid_logins = None
    with open("login_info.json", "r") as f:
        valid_logins = json.load(f)
    return valid_logins

def save_logins(to_be_saved = valid_logins):
    with open("login_info.json", "w") as f:
        json.dump(to_be_saved, f, indent= 4)

def main(page: ft.Page):
    page.title = "Haunted Dates Meeting Services"

    def login_page():
        page.controls.clear()

        username = ft.TextField(label= "put your username here")
        password = ft.TextField(label= "put your password here", 
                                password= True, 
                                can_reveal_password= True)
        result = ft.Text(value= "")

        page.floating_action_button = ft.FloatingActionButton(
            icon=ft.Icons.ACCESSIBILITY, 
            on_click= register_page, 
            content= "register"
        )

        def check_password(e):
            temp_var = load_logins()
            try:
                if temp_var[username.value] == password.value:
                    result.value = "Correct, Logging in"
                    for x in rangel(people):
                        if people[x].username == username.value:
                            main_page(x)
                else:
                    result.value = "Incorrect username or password"
            except:
                result.value = "Incorrect username or password"

        login_button = ft.Button("Log in", on_click= check_password)
        
        page.add(
            ft.Container(
                expand= True,
                content=ft.Column(
                    controls = [
                            username,
                            password,
                            login_button,
                            result
                        ]
                ),
                alignment = ft.Alignment.CENTER
            ),

        )

    def register_page():
        page.controls.clear()

        new_username = ft.TextField(label= "new username here")
        new_password = ft.TextField(label= "new password here",
                                hint_text= "don't use your username", 
                                password= True, 
                                can_reveal_password= True)
        new_name = ft.TextField(label= "display name(optional)")
        new_age = ft.TextField(label= "age (optional)")
        result = ft.Text(value= "")

        page.floating_action_button = ft.FloatingActionButton(
            icon=ft.Icons.ACCESSIBILITY_NEW,
            on_click= login_page, 
            content= "login",
            bgcolor= "green200"
        )

        def restore_user_information():
            restore_data = True
            for x in rangel(people):
                if people[x].username == new_username.value:
                    restore_data = False
            if restore_data:
                people.append(person(username= new_username.value, name= new_name.value, age= new_age.value))
            else:
                print("restored user data")

        def confirm_register(e):
            login_info = load_logins()
            y = True
            for x in login_info:
                if x == new_username.value:
                    result.value = "this username is taken" 
                    y = False
                    if login_info[x] == new_password.value:
                        result.value = "error, unable to register user"
            if y:
                login_info[new_username.value] = new_password.value
                result.value = "your account has been created"

                restore_user_information()

                store_data()
                save_logins(login_info)
                load_logins()
                main_page(-1)

        register_button = ft.Button("Register", on_click= confirm_register)

        page.add(
            ft.Container(
                expand= True,
                content= ft.Column(
                    controls = [
                        new_username,
                        new_password,
                        new_name,
                        new_age,
                        register_button,
                        result
                        ]
                    ),
                    alignment= ft.Alignment.CENTER
                )
            )

    def main_page(logged_in_account):
        page.controls.clear()
        page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

        user_name = ft.Text(value= "hello")

        if people[logged_in_account].name == "":
            user_name.value = f"hello {people[logged_in_account].username}!"
        else:
            user_name.value = f"hello {people[logged_in_account].name}!"

        page.floating_action_button = ft.FloatingActionButton(
            icon=ft.Icons.ACCESSIBILITY_NEW,
            on_click= login_page, 
            content= "Sign Out"
        )

        def go_to_answer_questions():
            answer_questions(logged_in_account)

        def go_to_generate_partners():
            generate_partners(logged_in_account)

        def go_to_update_personal_info():
            update_personal_info(logged_in_account)
        
        form_button = ft.Button("take questionaire", on_click= go_to_answer_questions)
        generate_matches = ft.Button("generate matches", on_click= go_to_generate_partners)
        personal_info = ft.Button("update info", on_click= go_to_update_personal_info)
        
        page.add(
            ft.Column(
                controls = [
                    user_name,
                    ft.Row(
                        controls = [
                        generate_matches,
                        form_button,
                        personal_info
                        ]
                    )
                    ]
                )
            )

    def answer_questions(logged_in_account):
        active_question = 0
        page.controls.clear()

        question_ask = ft.Text(questions_labels_values[active_question][0], data= 0)

        question_ans_1 = ft.Radio(value=1, label= "one")
        question_ans_2 = ft.Radio(value=2, label= "one")
        question_ans_3 = ft.Radio(value=3, label= "one")
        question_ans_4 = ft.Radio(value=4, label= "one")
        question_ans_5 = ft.Radio(value=5, label= "one")

        question_radio_group = ft.RadioGroup(
            content= ft.Column([question_ans_1,
                                question_ans_2,
                                question_ans_3,
                                question_ans_4,
                                question_ans_5])
        )

        def next_question(current_question):
            if current_question <= 0 or current_question >= 10:
                current_question = 0

            people[logged_in_account].stats[atributes[current_question]] = question_radio_group.value

            current_question += 1

            if current_question >= len(questions_labels_values):
                got_to_main_page()

            question_ask.data += 1
            update_question(current_question)
            store_data()

        def update_question(current_question):
            if current_question <= 9:
                question_ask.value = questions_labels_values[current_question][0]
                question_ans_1.label = questions_labels_values[current_question][1]
                question_ans_2.label = questions_labels_values[current_question][2]
                question_ans_3.label = questions_labels_values[current_question][3]
                question_ans_4.label = questions_labels_values[current_question][4]
                question_ans_5.label = questions_labels_values[current_question][5]

        def got_to_main_page():
            main_page(logged_in_account)
        
        def go_to_next_question():
            next_question(question_ask.data)

        next_button = ft.Button("next", on_click= go_to_next_question)
        return_button = ft.Button("Back to main page", on_click= got_to_main_page)

        update_question(question_ask.data)

        page.add(
            ft.Container(
                expand= True,
                content= ft.Column(
                controls = [
                    question_ask,
                    question_radio_group,
                    next_button,
                    return_button
                    ]
                ),
                alignment= ft.Alignment.CENTER
            )
        )
     
    def update_personal_info(logged_in_account):
        page.controls.clear()

        collect_name = ft.TextField(label= "What is your name?",
                                    hint_text= "This doesn't change your username")
        collect_age = ft.TextField(label= "What is your age?")

        def got_to_main_page():
            people[logged_in_account].name = collect_name.value
            people[logged_in_account].age = collect_age.value
            store_data()
            main_page(logged_in_account)

        return_button = ft.Button("Save and Return", on_click= got_to_main_page)

        page.add(
            ft.Container(
                expand= True,
                content= ft.Column(
                controls = [
                    collect_name,
                    collect_age,
                    return_button
                    ]
                ),
                alignment= ft.Alignment.CENTER
            )
        )
   
    def generate_partners(logged_in_account):
        page.controls.clear()

        if logged_in_account < 0:
            logged_in_account += len(people)
        possile_dates = len(people) - 1
        
        print(possile_dates) #temp
        print(logged_in_account) #temp
        print("today i will giv u a flet tire") #temp

        for x in rangel(people):
            if x != logged_in_account:
                print("hello! match made in location_6231_bad")
               # similarity(people[logged_in_account], people[x])
            else:
                print("this account is currently active")

        def got_to_main_page():
            main_page(logged_in_account)

        #def similarity(active_user, non_active_user):
        #    score = []
         #   if active_user.f_game <= non_active_user.f_game:
         #       score.append(non_active_user.f_game - active_user.f_game)
          #  else:
         #       score.append(active_user.f_game - non_active_user.f_game)
#
          #  return score
        
        return_button = ft.Button("Back to main page", on_click= got_to_main_page)
        page.add(
            ft.Container(
                expand= True,
                content= ft.Column(
                controls = [
                        return_button
                    ]
                ),
                alignment= ft.Alignment.CENTER
            )
        )

    login_page()
'''
load_logins()
retrive_data()

ft.run(main)
'''