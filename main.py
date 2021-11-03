import gspread
import telebot
from datetime import datetime


def getCell(machine):
	alph = {1: 'C', 2: 'D', 3: 'E', 4: 'F', 5: 'G', 6: 'H', 7: 'I', 8: 'J', 9: 'K', 10: 'L', 11: 'M', 12: 'N', 13: 'O',
			14: 'P', 15: 'Q', 16: 'R', 17: 'S', 18: 'T', 19: 'U', 20: 'V', 21: 'W', 22: 'X', 23: 'Y', 24: 'Z', 25: 'AA',
			26: 'AB', 27: 'AC', 28: 'AD', 29: 'AE', 30: 'AF', 31: 'AG'}
	row = alph[datetime.now().day]
	strNum = machine + 3
	strNum.__str__()
	cell = row + str(strNum)
	return cell


def color(inp):
	if "готов" in inp:
		color = {"backgroundColor": {"red": 0, "green": 1}}
	else:
		color = {"backgroundColor": {"red": 1, "green": 0}}
	return color

try:
	def main():
		bot = telebot.TeleBot("1572706532:AAHVOtALqAkxdlf9BmaB_17OCuSE4cvc08Q")


		@bot.message_handler(func=lambda message: True)
		def echo_all(message):
			name = message.from_user.first_name
			gc = gspread.service_account(filename='test1-330905-670f39e71bf8.json')  # авторизация в гугл через данные в файле
			sh = gc.open_by_key('1BnWadiih6ZwCHuvXsV8VT9fCNYsbmP1fNssYGk0FgNA')  # открываем нужную таблицу
			worksheet = sh.worksheet('Ноябрь2021')
			a = message.text
			b = a.split(' ', maxsplit=1)
			machine = int(b[0])
			cell = getCell(machine)
			cellRange = cell + ":" + cell
			oldNote = worksheet.get_note(cellRange)  # забираем старый комментарий
			note = oldNote + "\n" + name + ": " + b[1]  # добавляю новый комментарий к старому
			worksheet.format(cellRange, color(b[1]))  # изменение цвета ячейки на красный
			worksheet.update_note(cell, note)  # добавление комментария к ячейке "ячейка","коммент"

		bot.polling()

	if __name__ == "__main__":
		main()
except Exception as e:
	f = open('log.txt', 'a')
	try:
		f.write("\n"+str(e)) # Write a string to a file
	finally:
		f.close()
	pass
main()

