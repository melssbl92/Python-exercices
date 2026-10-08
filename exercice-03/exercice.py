def afficher_temp(temp):
    if isinstance(temp, int):
        return str(temp)
    if float(temp).is_integer():
        return str(int(temp))
    return str(temp).rstrip('0').rstrip('.')


def main():
    temperatures_c = [12.5, 14.0, 9.5, 12.0, 13.0, 14.0, 14.6, 18.7, 20.0, 21.0]

    moyenne = sum(temperatures_c) / len(temperatures_c)
    minimum = min(temperatures_c)
    maximum = max(temperatures_c)
    jours_plus_chauds = 0
    for temp in temperatures_c:
        if temp > 15:
            jours_plus_chauds += 1
    fahrenheit = [round(temp * 9 / 5 + 32, 1) for temp in temperatures_c]

    print(f"Moyenne : {moyenne:.2f}")
    print(f"Min : {afficher_temp(minimum)} / Max : {afficher_temp(maximum)}")
    print(f"Jours > 15 °C : {jours_plus_chauds}")
    print(f"Fahrenheit : {fahrenheit}")

    for index, temp in enumerate(temperatures_c, start=1):
        print(f"Jour {index} : {afficher_temp(temp)} °C")


if __name__ == "__main__":
    main()

