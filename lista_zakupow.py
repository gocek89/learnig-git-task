shoping_list = {
    "piekarnia": ["chleb", "bułka tarta", "bułki", "kokosanki"],
    "warzywniak": ["pomidory", "ogórek", "ziemniaki"],
    "zabka": ["mleko", "masło orzechowe", "chipsy", "papierosy"]}
sum = 0
for kay, value in shoping_list.items():
    for v in range(len(value)):
        value[v] = value[v].capitalize()
    print(
        f"Idę do {kay.capitalize()} ,kupuję tu następujące rzeczy: {value}")

    x = len(value)
    sum += x

print(f"Suma wszystkich produktów wynosi {sum}")
