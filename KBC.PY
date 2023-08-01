
print("WELCOM TO KAUN BANEGA CARODPATI")
questions = [
    ["1. Which one of the following river flows between Vindhyan and Satpura ranges?","(a) Narmada","(b) Mahanadi","(c) Son","(d) Netravati","a"],
    ["2. The Central Rice Research Station is situated in?","(a) Chennai","(b) Cuttack","(c) Bangalore","(d) Quilon","b"],
    ["3. Who among the following wrote Sanskrit grammar?","(a) Kalidasa","(b) Charak","(c) Panini","(d) Aryabhatt","c"],
    ["4. Which among the following headstreams meets the Ganges in last?","(a) Alaknanda","(b) Pindar","(c) Mandakini","(d) Bhagirathi","d"],
    ["5. The metal whose salts are sensitive to light is?","(a) Zinc","(b) Silver","(c) Copper","(d) Aluminum","b"],
    ["6. Patanjali is well known for the compilation of –","(a) Yoga Sutra","(b) Panchatantra","(c) Brahma Sutra","(d) Ayurveda","a"],
    ["7. River Luni originates near Pushkar and drains into which one of the following?","(a) Rann of Kachchh","(b) Arabian Sea","(c) Gulf of Cambay","(d) Lake Sambhar","a"],
    ["8. Which one of the following rivers originates in Brahmagiri range of Western Ghats?","(a) Pennar","(b) Cauvery","(c) Krishna","(d) Tapti","b"],
    ["9. The country that has the highest in Barley Production?","(a) China","(b) India","(c) Russia","(d) France","c"],
    ["11. Chambal river is a part of –","(a) Sabarmati basin","(b) Ganga basin","(c) Narmada basin","(d) Godavari basin","c"],
    ["12. D.D.T. was invented by?","(a) Mosley","(b) Rudolf","(c) Karl Benz","(d) Dalton","a"],
    ["13. Volcanic eruption do not occur in the","(a) Baltic sea","(b) Black sea","(c) Caribbean sea","(d) Caspian sea","a"],
    ["14. Indus river originates in –","(a) Kinnaur","(b) Ladakh","(c) Nepal","(d) Tibet","d"],
    ["15. The hottest planet in the solar system?","(a) Mercury","(b) Venus","(c) Mars","(d) Jupiter","b"]

]
prize= [1000,2000,4000,8000,16000,32000,64000,128000,256000,512000,1028000,2156000,4312000,8624000,17248000]
#print(len(prize))
money = 0

for i in range(0,len(questions)):
    print(questions[i][0])
    print(questions[i][1])
    print(questions[i][2])
    print(questions[i][3])
    print(questions[i][4])
    answer = input("enter right option : ").lower()
    if questions[i][-1] == answer:
        print("Adbhoot,aapka uttar ek dum sahi hai")
        money += prize[i]
        print(f"you win {prize[i]}")
        print(f"your total balance is  {money}")
        print("Agla question aapki computer screen pe......")
        if i == 4:
            money = 100000
        elif i == 8:
            money = 500000
    else:
        print("shreeman aapka answer galat hai!!")
        money= prize[i-1]
        break

print(f"your money which you take home is {money} ")
