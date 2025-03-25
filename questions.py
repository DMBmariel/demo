import random
 # Preguntas para el juego
questions = ["¿Qué función se usa para obtener la longitud de una cadena en Python?",
    "¿Cuál de las siguientes opciones es un número entero en Python?",
    "¿Cómo se solicita entrada del usuario en Python?",
    "¿Cuál de las siguientes expresiones es un comentario válido en Python?",
    "¿Cuál es el operador de comparación para verificar si dos valores son iguales?",]
 # Respuestas posibles para cada pregunta, en el mismo orden que las preguntas
answers = [
 ("size()", "len()", "length()", "count()"),
 ("3.14", "'42'", "10", "True"),
 ("input()", "scan()", "read()", "ask()"),
 (
 "// Esto es un comentario",
 "/* Esto es un comentario */",
 "-- Esto es un comentario",
 "# Esto es un comentario",
 ),
 ("=", "==", "!=", "==="),
 ]
 # Índice de la respuesta correcta para cada pregunta, el el mismo orden que las preguntas
correct_answers_index = [1, 2, 0, 3, 1]
# inicializamos el puntaje obtenido
score = 0
# El usuario deberá contestar 3 preguntas
questions_to_ask = random.sample(list(zip(questions,
 answers, correct_answers_index)), k=3)
for i in range(3):
    print(questions_to_ask[i][0])
    for j, answer in enumerate(questions_to_ask[i][1]):
        print(f"{j+1}.{answer}")
    correct_answer = False
# El usuario tiene 2 intentos para responder correctamente
    for intento in range(2):
        user_answer = input("Respuesta: ")
# verifico que el numero ingresado sea valido 
        if user_answer.isdigit():
            user_answer = int(user_answer)
            if (user_answer >= 1 and user_answer <= 4):
                user_answer -= 1
            else:
                print('Respuesta no valida')
        else:
            print('Respuesta no valida')
 # Se verifica si la respuesta es correcta
        if user_answer == questions_to_ask[i][2]:
               print("¡Correcto!")
               score += 1
               correct_answer = True
               break
        else:
            score -= 0.5  
    # Si el usuario no responde correctamente después de 2 intentos,
    # se muestra la respuesta correcta
    if correct_answer == False:
        question, answer, correct_index = questions_to_ask[i]
        print(f"Incorrecto. La respuesta correcta es: {answer[correct_index]}")
          
 # Se imprime un blanco al final de la pregunta
    print()
# Se imprime el puntaje obtenido del juego
print (f" El puntaje obtenido es: {score}") 

