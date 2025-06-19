import datetime
import random
import pdfplumber

from random import choice
from string import printable
from gtts import gTTS




def find_answer():
  print("древняя загадка - бот задает загадку")

  answer_user = input("Что можно сломать даже не трогая? ")
  if answer_user == "тишина":
    print("ответ верный")
  else:
    print("отовет не верный")

  user_answer = input("висит груша нельзя скушать, что это? ")
  if user_answer == "мяу":
    print("ответ верный")
  else:
    print("отовет не верный")

  user = input("да? ")
  if user == "нет":
    print("ответ верный")
  else:
    print("отовет не верный")



def age_determination():
  print("бот спрашивает год рождения и выдает ваш возраст")

  year_user = int(input("в каком году вы родились? "))
  date_user = datetime.date(year_user, 1, 1)
  today = datetime.datetime.now().date()
  result = today - date_user
  year = result/ 365
  year = year.days
  print("вам", year, "лет")



def guess_number():
  print("бот загадывает число от 1-10")
  number = random.randint(1, 10)
  choice_user = input("угадай число загаданное ботом: ")
  if choice_user == number:
    print("вы отгдалали число")
  else:
    print("вы не отгадали число")




def generation_password():
  print("бот создает пароль из 6 символов")
  password = ''.join([random.choice(printable) for number in range(6)])
  password = password.replace('\t', random.choice(printable))
  password = password.replace('\n', random.choice(printable))
  password = password.replace('\x0b', random.choice(printable))
  password = password.replace('\x0c', random.choice(printable))
  print(password,)



def read_story():
  print("бот читает историю")
  language = "ru"
  file_path="pdf_file.pdf"
  with pdfplumber.PDF(open(file_path, mode='rb')) as pdf_file:
      number_pages = pdf_file.pages
      for page in number_pages:
          text_pages = page.extract_text()
          text_pages = text_pages.replace('\n',' ' )
          audio = gTTS(text=text_pages, lang=language)
          file_name = "af.mp3"
          audio.save(file_name)
          
      print(text_pages)






print("Привет я жертва которую заставили переписывать все проекты в ручную из за плохой политики реплита.")
number = 1
while number == True :
  choice_user = input("на выбор у меня есть 9 программ выбери одну из них. 1.загадки 2.определение вашего возраста 3.угадай число 4.генератор паролей 5.история вслух 6.остановить проект. для выбора программы напиши цифру ")
  if choice_user == "1":
    find_answer()
  elif choice_user == "2":
    age_determination()
  elif choice_user == "3":
    guess_number()
  elif choice_user == "4":
    generation_password()
  elif choice_user == "5":
    read_story()
  elif choice_user == "6":
    break
  