def reverse(text):
    return text[::-1]
def is_palindrome(text):
    return text == reverse(text)

forbidden = (".","?","!",":",";","-","—","()","[]","...","'","\"\"","/",","," ")

something = input('Введите текст: ')
something = something.lower()
something = "".join(symbol for symbol in something if symbol not in forbidden)

if (is_palindrome(something)):
    print("Да, это палиндром")
else:
    print("Нет, это не палиндром")
