# input = kkkiiiaaaak
# output = 3k3i4a1k

def count_letters(string:str):
    i = 0
    lista = list(string)
    new_lista = []
    last_index = len(lista) - 1
    while i < last_index:
        counter = 1
        while lista[i] == lista[i + 1]:
            counter += 1
            i += 1
        new_lista.append(str(counter) + lista[i])
        if (i + 1) == (len(lista) - 1):
            new_lista.append("1" + lista[i+1])
        i += 1
    return "".join(new_lista)

if __name__ == "__main__":
    string = "kkkiiiaaaak"
    print(count_letters(string))