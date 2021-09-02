import os
# input = CH4 + 2O2 -> CO2 + 2H2O
def isInt(string):
    try:
        int(string)
        return True
    except:
        return False

def space_splitter(input):
    return input.split(" ")

def compound_coeffiencient(compound):
    coefficient = []
    for i in range(len(compound)):
        molecule = compound[i].strip()
        coeffe = ""
        j = 0
        while True:
            if isInt(molecule[j]) == True:
                coeffe += str(molecule[j])
                j += 1
            else:
                break
        try:
            coefficient.append(int(coeffe))
        except ValueError:
            coefficient.append(1)
    
    return coefficient

def func1(compound, no):
    noOfElement = ""
    if isInt(compound[no]) == False:
        return 1
    while True:
        if isInt(compound[no]):
            noOfElement += str(compound[no])
        else:break
        no+=1
    
    return int(noOfElement)

def multiplier(compound, coefficient):
    new_compound = ""
    for i in range(len(compound)):
        molecule = compound[i].strip()
        j = 0
        while True:
            if j == len(molecule):
                break
            if isInt(molecule[j]):
                j+=1
                continue
            else: break
        for k in range(j, len(molecule)):
            if isInt(molecule[k]): new_compound += str(int(molecule[k])*int(coefficient[i]))
            else: new_compound += molecule[k]
        new_compound += " "
    return new_compound

def plus_splitter(input):
    coumpond = input.split("+")
    return coumpond

def equilised(reactant, product):
    # Some basic things about ALPHABETS and Chemical Elements
    ALPHABETS = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    DOUBLE_LETTER_ELEMENTS = ["He", "Li", "Be",  "Ne", "Na", "Mg", "Al", "Si", "Cl", "Ar", "Ca", "Sc", "Ti", "Cr", "Mn", "Fe", "Co", "Ni", "Cu", "Zn", "Ga", "Ge", "As", "Se", "Br", "Kr", "Rb", "Sr", "Zr", "Nb", "Mo", "Tc", "Ru", "Rh", "Pd", "Ag", "Cd", "In", "Sn", "Sb", "Te", "Xe", "Cs", "Ba", "La", "Ce", "Pr", "Nd", "Pm", "Sm", "Eu", "Gd", "Tb", "Dy", "Ho", "Er", "Tm", "Yb", "Lu", "Hf", "Ta",  "Re", "Os", "Ir", "Pt", "Au", "Hg", "Tl", "Pb", "Bi", "Po", "At", "Rn", "Fr", "Ra", "Ac", "Th", "Pa", "Np", "Pu", "Am", "Cm", "Bk", "Cf", "Es", "Fm", "Md", "No", "Lr", "Rf", "Db", "Sg", "Bh", "Hs", "Mt", "Ds", "Rg", "Cn", "Nh", "Fl", "Mc", "Lv", "Ts", "Og"]
    SINGLE_LETTER_ELEMENTS = ["H", "B", "C", "N", "O", "F", "P", "S", "K", "V", "Y", "I", "U", "W"]

    # No of elements in equation
    noOfDoubleLetterElementsInReactant= [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    noOfDoubleLetterElementsInProduct= [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    noOfSingleLetterElementsInReactant = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    noOfSingleLetterElementsInProduct = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    
    reactant_elements = reactant.split(" ")
    for i in range(len(reactant_elements)): # CH4 O2
        element1 = reactant_elements[i] # CH4
        for j in range(len(element1)):
            if isInt(element1[j]):
                continue
            for k in range(len(DOUBLE_LETTER_ELEMENTS)):
                if element1[j:j+2] == DOUBLE_LETTER_ELEMENTS[k]:
                    noOfDoubleLetterElementsInReactant[k] += func1(element1, j+2)
                else: pass
            
            for l in range(len(SINGLE_LETTER_ELEMENTS)):
                if element1[j:j+2].isupper() == True:
                    if element1[j] == SINGLE_LETTER_ELEMENTS[l]:
                        # if j == len(element1)-1 and isInt(element1[j])==False:
                        #     noOfSingleLetterElementsInReactant[l] += 1
                        # else:
                        noOfSingleLetterElementsInReactant[l] += func1(element1, j)
                else : break
 
    product_elements = product.split(" ")
    for i in range(len(product_elements)): # CH4 O2
        element2 = product_elements[i] # CH4
        for j in range(len(element2)):
            if isInt(element2[j]):
                continue
            for k in range(len(DOUBLE_LETTER_ELEMENTS)):
                if element2[j:j+2] == DOUBLE_LETTER_ELEMENTS[k]:
                    noOfDoubleLetterElementsInProduct[k] += func1(element2, j+2)
                else: pass
            
            for l in range(len(SINGLE_LETTER_ELEMENTS)):
                if element2[j:j+2].isupper() == True:
                    if element2[j] == SINGLE_LETTER_ELEMENTS[l]:
                        noOfSingleLetterElementsInProduct[l] += func1(element2, j)
                else : break

    if noOfDoubleLetterElementsInProduct == noOfDoubleLetterElementsInReactant and noOfSingleLetterElementsInProduct == noOfSingleLetterElementsInReactant: return True
    return False

# input = CH4 + 2O2 -> CO2 + 2H2O

def final_touch(reactant, product, reactant_coefficient, product_coefficient):
    final_reactant = ""
    final_product = ""

    reactant = plus_splitter(reactant)
    # CH4 2O2
    reactant = space_splitter(reactant)
    # 'CH4', '2O2'
    product = plus_splitter(product)
    # CO2 2H20
    product = space_splitter(product)
    for i in range(len(reactant)):
        if isInt(reactant[i][0]) == True:
            final_reactant += (str(reactant_coefficients[i]) + reactant[i][1:])
        else:
            final_reactant += str(reactant[i])
        final_reactant += " "

    for i in range(len(product)):
        if isInt(product[i][0]) == True:
            final_product += (str(product_coefficients[i]) + product[i][1:])
        else:
            final_product += str(product[i])
        final_product += " "
        
    return "Answer is : " + str(final_reactant) + "->" + str(final_product)
    # for i in range(len(reactant)):
    #     if isInt(reactant[0]) == True and i == 0: continue
    #     elif reactant[i].isupper() == True:
    #         coefficient_index.append(i-1)
    #     else: pass

def equiliser():
    # Input of equation 
    os.system("clear")
    reactant_original = input("Enter the Reactant : ")
    reactant = plus_splitter(reactant_original)
    os.system("clear")
    print("Reactant : " + str(reactant_original))
    product_original = input("Enter the product : ")
    product = plus_splitter(product_original)
    os.system("clear")
    print("Product : " + str(product_original))
    
    for i in range(1, 10):
        reactant_coefficients = compound_coeffiencient(reactant) # Reactant molecule coefficient
        reactant_coefficients_original = reactant_coefficients.copy()

        product_coefficients = compound_coeffiencient(product) # Product molecule coefficient
        product_coefficients_original = product_coefficients.copy()

        new_reactant = multiplier(reactant, reactant_coefficients)

        new_product = multiplier(product, product_coefficients)

        if equilised(new_reactant, new_product) == True:
            print(f"You have given a solved equations\nAnswers : {reactant_original} -> {product_original}")
            return 0
        
        reactant_coefficients_for_product = reactant_coefficients.copy()
        for j in range(len(reactant_coefficients)):
            product_coefficients_for_reactant = product_coefficients.copy()
            if j == 0:
                reactant_coefficients[j] = str(int(reactant_coefficients[j])+1)
            elif j == len(reactant_coefficients):
                for k in range(len(reactant_coefficients)):
                    if k == len(reactant_coefficients):
                        pass
                    reactant_coefficients[k] = str(int(reactant_coefficients)+1)
            elif j>0:
                reactant_coefficients[j] = str(int(reactant_coefficients[j])+1)
                reactant_coefficients[j-1] = str(int(reactant_coefficients[j-1])-1)

            reactant_new = multiplier(reactant_original, reactant_coefficients)
            product_new = multiplier(product_original, product_coefficients_for_reactant)

            if equilised(reactant_new, product_new) == True:
                print(final_touch(reactant_original, product_original, reactant_coefficients, product_coefficients_for_reactant))
                return 0
            
            if j == 0:
                product_coefficients[j] = str(int(product_coefficients[j])+1)
            elif j == len(product_coefficients):
                for k in range(len(product_coefficients)):
                    if k == len(product_coefficients):
                        pass
                    product_coefficients[k] = str(int(product_coefficients)+1)
            elif j>0:
                product_coefficients[j] = str(int(product_coefficients[j])+1)
                product_coefficients[j-1] = str(int(product_coefficients[j-1])-1)

            reactant_new = multiplier(reactant_original, reactant_coefficients_for_product)
            product_new = multiplier(product_original, product_coefficients)
            
            if equilised(reactant_new, product_new) == True:
                print(final_touch(reactant_original, product_original, reactant_coefficients_for_product, product_coefficients))
                return 0
            
            reactant_coefficients_for_product = reactant_coefficients.copy()

    print("Not Found, Bi-yot-ch")
            
equiliser()
