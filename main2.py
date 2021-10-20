def show_menu():
    print('1.Citire liste')
    print('2.Afisare a celor doua liste daca au acelasi nr de elemente pare')
    print('3.Intersectia celor doua liste')
    print('4.Palindroamele obtinute prin concatenarea elem de pe aceleasi pozitii')
    print('5.Citirea unei liste si inlocuirea elem cu oglinditul lor daca sunt divizibile cu toate elem din lista citita')
    print('x.Inchidere')


def read_list():
    floats_as_str = input('Dati o lista de int-uri separate prin spatiu: ')
    floats_as_list_of_str = floats_as_str.split(' ')
    floats = []
    for float_str in floats_as_list_of_str:
        floats.append(int(float_str))


def show_list_if_even(lst1,lst2):
    """
    Afiseaza mesajul DA daca cele doua liste au acelasi nr de elem pare,NU in caz contrar
    :param lst1: lst1
    :param lst2: lst2
    """
    nr1=0
    nr2=0
    for i in lst1:
        if i%2==0: nr1=nr1+1
    for j in lst2:
        if j%2==0: nr2=nr2+1

    if nr1==nr2:
        return True
    return False


def intersection(lst1, lst2):
    """
    Face intersectia celor doua liste
    :param lst1: lst1
    :param lst2: lst2
    :return: result
    """
    result=[]
    result = [value for value in lst1 if value in lst2]
    return result


def show_intersection(lst1,lst2):
    print(f'Intersectia listei {lst1} cu lista {lst2} este: {intersection(lst1, lst2)}')


def concatenate_elements(lst1,lst2):
    """
    Concateneaza doua liste.
    :param lst1: lst1
    :param lst2: lst2
    :return: res
    """
    res=[]
    res = [i + j for i, j in zip(lst1, lst2)]


def palindrome(lst1,lst2):
    """
    Creeaza o noua lista cu palindroamele obtinute prin concatenarea a doua liste
    """
    res=concatenate_elements(lst1, lst2)
    result=[]
    for i in res:
       if i == i[::-1]: result.append(i)
    return result



def show_palindrome(lst1,lst2):
    print(f'Din intersectia listei {lst1} cu {lst2} obtinem lista de palindroame: {palindrome(lst1,lst2)}')

def inlocuire_cu_oglindit(lst1,lst2):
    """
    Citeste o a treia lista si inlocuieste elementele  din lst1 si lst2  care sunt divizibile cu toate elem din lst 3 cu oglinditul lor
    :param lst1:lst1
    :param lst2:lst2
    :return:new_lst1 si new_lst2
    """
    c=input('Dati o lista de numere citite de la tastatura: ')
    new_lst1=[]
    new_lst2=[]
    for  elem in lst1:
        ok=1
        for j in c:
            if elem%j!=0: ok=0
        if ok==1:  new_lst1.append(str(elem)[::-1])

    for elem in lst2:
        ok=1
        for j in c:
            if elem%j!=0: ok=0
        if ok==1:  new_lst2.append(str(elem)[::-1])

    return new_lst1 and new_lst_2


def show_inlocuire_cu_oglindit(lst1,lst2):
    print(f'Noile liste vor fi: {inlocuire_cu_oglindit(lst1,lst2)}')


def main():
    lst1=[]
    lst2=[]
    while True:
        show_menu()
        option=input('Alegeti optiunea: ')
        if option=='1':
            lst1=read_list()
            lst2=read_list()
        elif option=='2':
            show_list_if_even(lst1, lst2)
        elif option=='3':
            show_intersection(lst1, lst2)
        elif option=='4':
            show_palindrome(lst1, lst2)
        elif option=='5':
            show_inlocuire_cu_oglindit(lst1, lst2)
        elif option=='x':
            break


if __name__ == '__main__':
    main()
