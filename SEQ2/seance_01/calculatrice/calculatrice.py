G = 0
D = 1
OP = 2


# Vérifie si la chaîne peut être convertie en nombre.

def isnumber(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


# Supprime les parenthèses qui entourent toute l'expression.
def nettoyer(expression):
    n = len(expression)
    priorite = 0
    if expression =="":
                return expression
    for c in expression:
        if c == "(":
            priorite += 1
        elif c == ")":
            priorite -= 1

    # Si le niveau revient à zéro avant la fin, les parenthèses
    # n'entourent pas toute l'expression.
    if expression[0] == "(" and expression[n - 1] == ")":
        return nettoyer(expression[1:n - 1])
    return expression
    # Les parenthèses entourent toute l'expression.
    # On les retire, puis on recommence si nécessaire.
    


# Recherche un opérateur situé en dehors des parenthèses.
def decoupage_selon_operateur(expression, operateur):
    priorite = 0

    # Parcourt l'expression caractère par caractère.
    for i in range(len(expression)):
        c = expression[i]

        # Modifie le niveau de parenthèses rencontré.
        if c == "(":
            priorite += 1
        elif c == ")":
            priorite -= 1
        
        # Un opérateur au niveau zéro n'est pas placé dans des parenthèses.
        if c == operateur and priorite == 0:
            # Sépare l'expression à gauche et à droite de l'opérateur.
            gauche = nettoyer(expression[:i])
            droite = nettoyer(expression[i+1:])

            # Retourne les deux parties ainsi que l'opérateur trouvé.
            return [gauche, droite, operateur] 
        
            
    # Aucun opérateur utilisable n'a été trouvé dans l'expression.
    return [expression, None, "noop"] 


# Transforme une expression texte en structure récursive de calcul.
def decoupage(expression):
    # Un nombre est un cas terminal : il ne contient pas de sous-expression.
    # "num" indique à calculer qu'il faut simplement utiliser cette valeur.
    if isnumber(expression):
        return [float(expression), None, "num"]
    
    # Recherche un opérateur au niveau principal de l'expression.
    for operateur in ["+", "-", "*", "/", "^"]: 
        gauche, droite, op = decoupage_selon_operateur(expression, operateur)
        
        # "noop" signifie qu'aucun opérateur de ce type n'a été trouvé.
        if op != "noop": 
            # Chaque partie est à son tour découpée récursivement.
            # La structure obtenue est [gauche, droite, operateur].
            return [decoupage(gauche), decoupage(droite), op] 

    # L'expression n'est ni un nombre ni une opération reconnue.
    raise Exception("Aucun operateur trouve, ERREUR SYNTAX")
    
# Évalue l'expression fournie.
def calculer(s):
    pass


def main():
    # Demande une expression à l'utilisateur.
    expression = input("Entrez l'expression à calculer : ")
    expression_formatee = decoupage(expression)
    print("Le résultat est", calculer(expression_formatee))


if __name__ == "__main__":
    main() 
    
