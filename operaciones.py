#prueba traductores e interpretes
#jesus rondon ci: 17063376
#seccion 2 
#operaciones.py

operacion = raw_input('Ingrese la operacion a realizar (suma,resta,multiplicacion,division \n raiz,exponencial): ')

if operacion == 'suma' :
        num1 = float(raw_input('Ingrese el primer numero: '))
        num2 = float(raw_input('Ingrese el primer numero: '))
	result = num1 + num2
	print 'El resultado de la suma es: result=%4.3f' %result

if operacion == 'resta' :
        num1 = float(raw_input('Ingrese el primer numero: '))
        num2 = float(raw_input('Ingrese el primer numero: '))
	result = num1 - num2
	print 'El resultado de la resta es: result=%4.3f' %result

if operacion == 'multiplicacion' :
        num1 = float(raw_input('Ingrese el primer numero: '))
        num2 = float(raw_input('Ingrese el primer numero: '))
        result = num1 * num2
        print 'El resultado de la multiplicacion es: result=%4.3f' %result

if operacion == 'division' :
        num1 = float(raw_input('Ingrese el primer numero: '))
        num2 = float(raw_input('Ingrese el primer numero: '))
        if num2 == 0 :
                print 'no se puede dividir entre Cero'
        else:
                result = num1/num2
                print 'El resultado de la division es: result=%4.3f' %result

if operacion == 'raiz' :
        import math
        num1 = float(raw_input('Ingrese el numero a sacarle raiz cuadrada: '))
        result = math.sqrt(num1)
        print 'El resultado de la raiz cuadrada es: result=%4.3f' %result

if operacion == 'exponencial' :
        num1 = float(raw_input('Ingrese la base: '))
        num2 = float(raw_input('Ingrese el exponente: '))
        result = num1 ** num2
        print 'El resultado de la potencia es: result=%4.3f' %result
