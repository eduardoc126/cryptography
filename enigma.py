#////////////////////////////////

def letra_codficada(letter, shift_amount):
    if letter.isalpha():
        letter_code = ord(letter.lower())
        a_ascii = ord('a')
        alphabet_size = 26
        true_letter_code = a_ascii + (((letter_code - a_ascii) + shift_amount) % alphabet_size)
        decoded_letter = chr(true_letter_code)
    elif letter.isdigit():
        decoded_letter = str((int(letter) + shift_amount) % 10)
    else:
        decoded_letter = letter
    return decoded_letter

#////////////////////////////////

def lasso_word(word, shift_amount):
    decoded_word = ""
    for letter in word:
        decoded_letter = letra_codficada(letter, shift_amount)
        decoded_word += decoded_letter
    return decoded_word

#////////////////////////////////

print("Padrão: 4002892240028922400289222")

texto = input("Digite uma senha pra criptografar: ")

if len(texto) >= 1 and len(texto) <= 26:
    shifts = [4, 0, 0, 2, 8, 9, 2, 2, 4, 0, 0, 2, 8, 9, 2, 2, 4, 0, 0, 2, 8, 9, 2, 2, 2]
    decoded_texto = ""
    for i, letter in enumerate(texto):
        shift_amount = shifts[i % len(shifts)]
        decoded_letter = letra_codficada(letter, shift_amount)
        decoded_texto += decoded_letter
    print(f"Senha codificada: {decoded_texto}")
else:
    print("A senha deve ter entre 8 e 26 caracteres!")
