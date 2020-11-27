list_a = [12, 13, 14, 15, 16, 17, 18, 19]
list_b = [98, 97, 96, 95, 94, 93, 92, 91]

list_a_odds = list(filter(lambda odd: (odd % 2 != 0), list_a))
list_b_evens = list(filter(lambda even: (even % 2 != 0), list_b))

if __name__ == "__main__":
    print(list_a_odds)
    print(list_b_evens)
