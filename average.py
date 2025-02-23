class CipherMaster:
    # Не изменяйте и не перемещайте эту переменную
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

    def cipher(self, original_text, shift):
        shift_index = 33
        # Метод должен возвращать зашифрованный текст
        # с учетом переданного смещения shift.
        result = []
        hz = []
        for letter in original_text:
            if letter == ' ' or letter == ',':
                result.append(letter)
            else:
                index = CipherMaster.alphabet.find(letter.lower())  # Получаем индекс буквы 
                new_index = (index + shift) % len(CipherMaster.alphabet)  # Закольцовываем индекс
                result.append(new_index)
        for res in result:
            if res == ' ' or res == ',':
                hz.append(res)
            else:
                hz.append(CipherMaster.alphabet[res % len(CipherMaster.alphabet)])     
        return ''.join(hz)

    def decipher(self, cipher_text, shift):
        # Метод должен возвращать исходный текст
        # с учётом переданного смещения shift.
        result = []
        for letter in cipher_text:
            ...  # здесь ваш код
        return ''.join(result)


cipher_master = CipherMaster()
print(cipher_master.cipher(
    original_text='Однажды ревьюер принял проект с первого раза, с тех пор я его боюсь',
    shift=2
))
print(cipher_master.decipher(
    cipher_text='Олебэи яфвнэ мроплж сэжи — э пэй рдв злййвкпш лп нвящывнэ',
    shift=-3
))
