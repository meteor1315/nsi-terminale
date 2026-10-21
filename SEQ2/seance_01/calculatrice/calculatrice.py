G = 0
D = 1
OP = 2


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


def nettoyer(expression):
    n = len(expression)
    priorite = 0

    for c in expression:
        if c == "(":
            priorite += 1
        elif c == ")":
            priorite -= 1

        # On rencontre un caractère hors des parenthèses extérieures
        # avant la dernière position : elles ne sont donc pas inutiles.
        if priorite == 0 and c != expression[n - 1]:
            return expression

    # Les parenthèses entourent toute l'expression :
    # on les retire, puis on recommence si nécessaire.
    return nettoyer(expression[1:n - 1])


def decoupage_selon_operateur(expression, operateur):
    priorite = 0

    for i in range(len(expression)):
        c = expression[i]

        if c == "(":
            priorite += 1
        elif c == ")":
            priorite -= 1

        if c == operateur and priorite == 0:
            pass



def calculer(s):
    pass


def main():
    expression = input("Entrez l'expression à calculer : ")
    expression_formatee = decoupage(expression)
    print("Le résultat est", calculer(expression_formatee))


if __name__ == "__main__":
    main() 
    
