import hashlib

#Ввод количества элементов
num = int(input('Напишите количество элементов\n'))

arrayTXT = []
#Заполняем массив
for i in range (num):
  arrayTXT.append("txt"+str(i+1))

#Хеширование
for i in range(num):
  a = hashlib.sha256(arrayTXT[i].encode()).hexdigest()
  arrayTXT[i] = a


need_to_create=num #Сколько элементов осталось обработать
already_gone=0 #Сколько элементов уже обработано (Избегаем повтора хэширования)

#Цикл пока не придем к единственному элементу
while need_to_create > 1:
  #Проверка на четность оставшихся элементов
  if(need_to_create%2==0):
    for i in range(already_gone,already_gone+need_to_create,2):
      a=hashlib.sha256((arrayTXT[i]+arrayTXT[i+1]).encode()).hexdigest()
      arrayTXT.append(a)

  else:
    for i in range(already_gone,already_gone+need_to_create-1,2):
      a=hashlib.sha256((arrayTXT[i]+arrayTXT[i+1]).encode()).hexdigest()
      arrayTXT.append(a)
    #Хэшируем запись повтора осташегося элемента
    a=hashlib.sha256((arrayTXT[already_gone+need_to_create-1]+arrayTXT[already_gone+need_to_create-1]).encode()).hexdigest()
    arrayTXT.append(a)

  #Обновляем данные, чтобы не перехэшировать
  already_gone+=need_to_create
  need_to_create=len(arrayTXT)-already_gone

#Вывод корневого хэша (Всегда находится на последнем элементе)
print(arrayTXT[len(arrayTXT)-1])