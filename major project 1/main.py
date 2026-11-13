import flet as ft
import json

# two json files are needed, login_info with {} and storage with []

# to do list
# compress the retrieve and store data function
# add match ratings

people = []
valid_logins = {}

# probably could move this into a dictionary, or json file
questions_labels_values = [
    ["How much do you like video games?", "Strongly Agree", "Agree", "Neutral", "Disagree", "Strongly Disagree"],
    ["How much do you like books?", "Strongly Agree", "Agree", "Neutral", "Disagree", "Strongly Disagree"],
    ["How much do you like The outside?", "Strongly Agree", "Agree", "Neutral", "Disagree", "Strongly Disagree"],
    ["How much do you like School?", "Strongly Agree", "Agree", "Neutral", "Disagree", "Strongly Disagree"],
    ["What is your Favorite Subject?", "Math", "Comp Science", "Physics",  "Chemistry", "English"],
    ["how much do you like sports?", "They are a cornerstone of my being", "alot", "Neutral", "They don't affect me", "I find them boring"],
    ["Do you like computers?", "Strongly Agree", "Agree", "Neutral", "Disagree", "Strongly Disagree"],
    ["how much do you like to sleep?", "Strongly Agree", "Agree", "Neutral", "Disagree", "Strongly Disagree"],
    ["Do you like to remember?", "Strongly Agree", "Agree", "Neutral", "Disagree", "Strongly Disagree"],
    ["how much do you like comic books?", "Strongly Agree", "Agree", "Neutral", "Disagree", "Strongly Disagree"]]

attributes = [
    "game", "book", "subject", "outdoor", "school", "sports", "computers", "sleep", "remember", "comic"]

def rangel(x):
    return range(len(x))

def remove_duplicates(to_be_cut_down):
    cut_down_list = [to_be_cut_down[0]]
    keep_eye_out = [to_be_cut_down[0]]

    for x in rangel(to_be_cut_down):
        attempt = True
        for y in keep_eye_out:
            if to_be_cut_down[x] == y:
                attempt = False
        if attempt:
            cut_down_list.append(to_be_cut_down[x])
            keep_eye_out.append(to_be_cut_down[x])

    return(cut_down_list)

class person:
    def __init__(self,
                username, age = "", name = "",
                f_game: int = 0, f_book: int = 0,
                school: int = 0, f_subject: int = 0,
                f_outdoor: int = 0, sports: int = 0,
                computers: int = 0, sleep: int = 0,
                remember: int = 0, comic: int = 0,
                filled: bool = False,
                scr: int = 0):
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
        self.filled_form = filled
        self.shower_curtain_rings = scr
    def getname(self):
        if self.name == "":
            return self.username
        else:
            return self.name
    def getage(self):
        if self.age == "":
            return "unknown"
        else:
            return self.age
    def get_shower_curtain_rings(self):
        print(self.shower_curtain_rings)
        self.shower_curtain_rings += 1

# these functions are for storing user data (age, name, etc)
def store_data():
    to_be_stored = []
    for x in rangel(people):
        compressed_object = {
            "username": people[x].username,
            "age": people[x].age,
            "name": people[x].name,
            attributes[0]: int(people[x].stats[attributes[0]]),
            attributes[1]: int(people[x].stats[attributes[1]]),
            attributes[2]: int(people[x].stats[attributes[2]]),
            attributes[3]: int(people[x].stats[attributes[3]]),
            attributes[4]: int(people[x].stats[attributes[4]]),
            attributes[5]: int(people[x].stats[attributes[5]]),
            attributes[6]: int(people[x].stats[attributes[6]]),
            attributes[7]: int(people[x].stats[attributes[7]]),
            attributes[8]: int(people[x].stats[attributes[8]]),
            attributes[9]: int(people[x].stats[attributes[9]]),
            "has_filled_form": people[x].filled_form,
            "rings": people[x].shower_curtain_rings}
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
            data[x][attributes[0]],
            data[x][attributes[1]],
            data[x][attributes[2]],
            data[x][attributes[3]],
            data[x][attributes[4]],
            data[x][attributes[5]],
            data[x][attributes[6]],
            data[x][attributes[7]],
            data[x][attributes[8]],
            data[x][attributes[9]],
            data[x]["has_filled_form"],
            data[x]["rings"]))

# these functions are for storing user login information, they are connected to user data by the username
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
        greetings = ft.Text(value= "Welcome to Haunted Dates Meeting Services")
        username = ft.TextField(label= "put your username here")
        password = ft.TextField(label= "put your password here", password= True, can_reveal_password= True)
        result = ft.Text(value= "")

        page.floating_action_button = ft.FloatingActionButton(
            icon=ft.Icons.ACCESSIBILITY,
            on_click= register_page,
            content= "register")

        def check_password(e):
            logins = load_logins()
            try:
                if logins[username.value] == password.value:
                    result.value = "Correct, Logging in"
                    for x in rangel(people):
                        if people[x].username == username.value:
                            people[x].get_shower_curtain_rings()
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
                            greetings,
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
            bgcolor= "green200")

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

        user_name = ft.Text(value= f"hello {people[logged_in_account].getname()}!")
        can_go_to_patners = ft.Text(value= "")

        def go_to_login_page():
            store_data()
            login_page()

        page.floating_action_button = ft.FloatingActionButton(
            icon=ft.Icons.ACCESSIBILITY_NEW,
            on_click= go_to_login_page,
            content= "Sign Out",
            bgcolor= "red200")

        def go_to_answer_questions(e):
            answer_questions(logged_in_account)

        def go_to_generate_partners(e):
            if people[logged_in_account].filled_form == False:
                can_go_to_patners.value = "you must complete the questionaire before generating matches"
            else:
                generate_partners(logged_in_account)

        def go_to_update_personal_info(e):
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
                    ),
                    can_go_to_patners
                    ],
                alignment= ft.Alignment.CENTER
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
                                question_ans_5]))

        def next_question(current_question):
            if current_question <= 0 or current_question >= 10:
                current_question = 0

            people[logged_in_account].stats[attributes[current_question]] = question_radio_group.value
            current_question += 1

            if current_question >= len(questions_labels_values):
                people[logged_in_account].filled_form = True
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
                question_radio_group.value = 0

        def got_to_main_page():
            store_data()
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
                                    hint_text= "This doesn't change your username",
                                    value= people[logged_in_account].name)
        collect_age = ft.TextField(label= "What is your age?",
                                    value= people[logged_in_account].age)

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
       
        def got_to_main_page(e):
            main_page(logged_in_account)

        def sim_score(score):
            score2 = 0
            for x in score:
                score2 += x
            return(score2)

        def similarity(active_user, non_active_user):
            score = []
            for x in range(0, 10):
                if int(active_user.stats[attributes[x]]) <= int(non_active_user.stats[attributes[x]]):
                    score.append(int(non_active_user.stats[attributes[x]]) - int(active_user.stats[attributes[x]]))
                else:
                    score.append(int(active_user.stats[attributes[x]]) - int(non_active_user.stats[attributes[x]]))
            return sim_score(score)

        def calc_3_best(matches):
            saved_keys = []
            for x in matches:
                saved_keys.append(x)

            for x in matches:
                for y in rangel(saved_keys):
                    if matches[x] <= matches[saved_keys[y]]:
                        saved_keys.insert(y, x)

            saved_keys = remove_duplicates(saved_keys)

            while len(saved_keys) > 3:
                saved_keys.pop(-1)

            return saved_keys

        def algorithim_starter(logged_in_account):
            matches = {}

            if logged_in_account < 0:
                logged_in_account += len(people)

            for x in rangel(people):
                if x != logged_in_account:
                    if people[x].filled_form:
                        matches[x] = similarity(people[logged_in_account], people[x])
                    else:
                        matches[x] = 1999999999
                        # this sets the similarity score to very high, (lower is better here)
                        # meaning it will be one of the last matches,
                        # removing people who haven't filled out the form yet
            return calc_3_best(matches)
       
        n3_best = []
        n3_best = algorithim_starter(logged_in_account)

        match_1 = ft.Text(value= "")
        match_2 = ft.Text(value= "")
        match_3 = ft.Text(value= "")
        matches = [match_1, match_2, match_3]

        possible_people = len(people) - 1
        if possible_people == 2:
            matches[0].value = f"{people[n3_best[0]].getname()} age: {people[n3_best[0]].getage()}"
        elif possible_people == 3:
            matches[0].value = f"{people[n3_best[0]].getname()} age: {people[n3_best[0]].getage()}"
            matches[1].value = f"{people[n3_best[1]].getname()} age: {people[n3_best[1]].getage()}"
        else:
            for x in range(3):
                matches[x].value = f"{people[n3_best[x]].getname()} age: {people[n3_best[x]].getage()}"
       
        return_button = ft.Button("Back to main page", on_click= got_to_main_page)
        page.add(
            ft.Container(
                expand= True,
                content= ft.Column(
                controls = [
                        match_1,
                        match_2,
                        match_3,
                        return_button
                    ]
                ),
                alignment= ft.Alignment.CENTER
            )
        )
    login_page()

load_logins()
retrive_data()

ft.run(main)