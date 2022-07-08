birthday_dictionary = {
    "tata": "1978 06 20",
    "mama": "1980 10 25",
    "sofia": "2009 07 01",
}

nume = input("Te rog introdu numele: ")

if nume in birthday_dictionary:
    print(birthday_dictionary[nume])
else:
    print("Nu stiu data")