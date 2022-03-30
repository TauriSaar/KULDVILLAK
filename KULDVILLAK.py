def new_game():

    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("-------------------------")
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input("Sisesta (A, B või C): ")
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key), guess)
        question_num += 1

    display_score(correct_guesses, guesses)

def check_answer(answer, guess):

    if answer == guess:
        print("ÕIGE!")
        return 1
    else:
        print("VALE!")
        return 0

def display_score(correct_guesses, guesses):
    print("-------------------------")
    print("TULEMUSED")
    print("-------------------------")

    print("Õiged vastused: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("Arvatud: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()

    score = int((correct_guesses/len(questions))*100)
    print("Teie skoor on: "+str(score)+"%")

def play_again():

    response = input("Mängid uuesti? (jah või ei): ")
    response = response.upper()

    if response == "JAH":
        return True
    else:
        return False


questions = {
 "1) Mis reostavad vett? ": "A",
 "2) Millised majandusharud põhjustavad õlireostust? ": "C",
 "3) Veereostusele viitavad näiteks... ": "B",
 "4) Mida võivad sisaldada tööstuse heitveed? ": "C",
 "5) Kas õhusaaste all mõeldakse vaid õhku, mis sisaldab tervisele ohtlike osakesi? ": "B",
 "6) Mis on loodulskiud õhusaaste allikad? ": "A",
 "7) Milliseid tervisehädasid võib õhusaastus tekitada? ": "C",
 "8) Millised on peamised inimtekkelised õhusaaste allikad majandusharudest? " : "A",
 "9) Mis tekitab linnas kõige rohkem müra? ": "B",
 "10) Mida põhjustab müra inimestele? ": "B",
 "11) Millises Eesti linnas on kõige rohkem kaebusi müra kohta? ": "C",
 "12) Mitu aastat peab elama müra keskel, et tekiksid püsivad tervisekahjustused?" : "A",
 "13) Mis on valgusreostus? ": "C",
 "14) Valgusreostuse allikad linnas on... ": "B",
 "15) Kuidas mõjutab valgusreostus inimesi ja loomi? ": "A",
 "16) Millist teadusharu mõjutab valgusreostus? ": "C", 
}

options = [["A. Mitmesugused heitveed", "B. Metsapõlengud", "C. Müra"],
          ["A. Jäätmekäitlus", "B. Põllumajandus", "C. Tööstus ja transport"],
          ["A. Kalade muteerumine", "B. Veekogu kinnikasvamine ja ebameeldiv lõhn", "C. Ümberkaudsete loomade kadumine"],
          ["A. Puhastusvedelikke", "B. Ohtlikke gaase", "C. Raskemetallide ühendeid"],
          ["A. Jah", "B. Ei", "C. Ei tea"],
          ["A. Vulkaanid ja metsapõlengud", "B. Loomad", "C. Bakterid"],
          ["A. Kurtus, kuulmise halvenemine", "B. Silmanägemise järsk kehvenemine", "C. Hingamisteede ja südamehaigused"],
          ["A. Energiamajandus ja transport", "B. Riigikaitse ja ehitus", "C. Tervisehoid ja sotsiaalhooldus"],
          ["A. Teismelised pidu panemas", "B. Ehitus ning transpordisüsteemid", "C. Turistid"],
          ["A. Maksavähki", "B. Kuulmise kaotust ja stressi", "C. Liigesevalu"],
          ["A. Rakvere", "B. Tartu", "C. Tallinn"],
          ["A. 5-6 aastat", "B. 1-2 aastat", "C. 8-9 aastat"],
          ["A. Ebakvaliteetne valgus", "B. Liiga palju värvilisi tulesid koos", "C. Valguse sattumine kohta, kus see ei eaks olema"],
          ["A. Vilkuvad ketsid", "B. Hoonete sisevalgustus ja tänavavalgustid", "C. Sõiduautode tuled"],
          ["A. Segab nende ööpäevast tsüklit", "B. Nad harjuvad liiga ereda valgusega", "C. Nad ei näe öösel tähti"],
          ["A. Ornitoloogia", "B. Bioloogia", "C. Astroloogia"]]
print('Keskkonnaprobleemid: Reostus\nKoostajad: Tauri Saar, Pirko Vichmann, Lilii-Ann Older, Hanna Mägi')
new_game()

while play_again():
    new_game()

print("Head aega!")
