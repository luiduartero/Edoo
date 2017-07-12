#Edoo- Task 2
suma=1000
mitad=suma/2
def num_rectangulares():
    #buscamos el numero a
    for a in range(int(mitad)):
        #buscamos el numero b
        for b in range(a+1,int(mitad)):
            #calculamos el valor de c, conociendo a y b, con esto validamos la suma
            c=suma-(a+b)
            #verificamos que cumpla con ser un num rectangular
            if (a**2+b**2==c**2):
                print ("a: "+str(a)+" b: "+str(b)+" c: "+str(c))


#num_rectangulares()

#--------------------------------------------------------------------------------------------
#Edoo- Task 3
#limite superior de busqueda
limiteS=10000
#limite inferior de busqueda
limiteI=1
#cantidad de iteraciones
iteraciones=50
def num_machetes():
    #lista de numeros
    machetes=[]
    #recorremos los limites
    for a in range(limiteI,limiteS):
        num_actual=a;
        #realizamos las iteraciones
        for i in range(iteraciones):
            #sacamos el inverso del numero
            num_inverse=list(str(num_actual))[::-1]
            #sumamos el numero y su inverso
            result=num_actual + int("".join(num_inverse))
            #verificamos si es palindromo
            if(list(str(result))==list(str(result))[::-1]):
                #si es paramos
                break
            #si no asiganamos el result como nuevo valor a calcular
            else:
               num_actual=result
               #estamos en ultima iteracion es num machete
               if(i==iteraciones-1):
                   machetes.append(a)
    print ("Total Num: "+str(len(machetes))+ " Nums: ")
    print (machetes)

num_machetes()
            
    
