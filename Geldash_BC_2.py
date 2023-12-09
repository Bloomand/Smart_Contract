import rsa

#Создание пар ключей
(alice_public, alice_private) = rsa.newkeys(512)
(bob_public, bob_private) = rsa.newkeys(512)

#Генерируем данные "транзакции"
message = "Example text for encoding"
bmessage = message.encode()

signature = rsa.sign(bmessage, alice_private, 'SHA-256')


#Nice
Verify = rsa.verify(bmessage, signature, alice_public)
print(Verify)

#Nice
Verify = rsa.verify(bmessage, signature, alice_private)
print(Verify)

#Fault
Verify = rsa.verify(bmessage, signature, bob_public)
print(Verify)

#Fault
Verify = rsa.verify(bmessage, signature[:-1], alice_public)
print(Verify)