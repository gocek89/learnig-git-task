shoping_list = {
    "piekarnia": ["chleb", "bułka tarta", "bułki"],
    "warzywniak": ["pomidory", "ogórek", "ziemniaki"],
    "zabka": ["mleko", "masło orzechowe", "chipsy"]}

for kay, value in shoping_list.items():
    print(
        f"Idę do {kay.capitalize()} ,kupuję tu następujące rzeczy: {value}")
