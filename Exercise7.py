people_char = {"blue_eyed": {"Olivia", "Harry", "Lily", "Jack", "Amelia"},
               "blonde_haired": {"Harry", "Jack", "Amelia", "Mia", "Joshua"},
               "sensitive_smell": {"Harry", "Amelia"},
               "sensitive_taste": {"Harry", "Lily", "Amelia", "Lola"},
               "blood_type_o": {"Mia", "Joshua", "Lily", "Olivia"},
               "blood_type_b": {"Amelia", "Jack"},
               "blood_type_a": {"Harry"},
               "blood_type_ab": {"Joshua", "Lola"}
               }

if __name__ == "__main__":
    unique_people = set()
    for key, value in people_char.items():
        unique_people = unique_people.union(value)

    print("Unique List of People {}".format(unique_people))

    print("Blonde Hair, Blue Eyes or both {}".format(people_char['blonde_haired'].union(people_char['blue_eyed'])))

    print("Has sensitive Smell and Taste {}".format(
        people_char['sensitive_smell'].intersection(people_char['sensitive_taste'])))

    print("People who can donate to blood type B {}".format(people_char['blood_type_b']))

    print("Blonde haired people but not sensitive to odors {}".format(
        people_char['blonde_haired'].difference(people_char['sensitive_smell'])))
