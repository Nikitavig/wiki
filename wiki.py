import wikipedia
import re

# Число предложений, для выгрузки данных с wiki
limit = 5


def preprocess_text(text):
	"""
		Функция для форматирвоания текста
		Args:
			test(str):
	"""


	# Убрать описание в скобках
	text = re.sub(r'\([^()]*\)', '', text)
	text = re.sub(f'=', '', text)
	return text.strip()
	


def wiki(text, sentences=3):
	"""
		Функция для получения данных статьи с wiki
		Args:
			text(str): запрок к источнику
			sentences(int): сколько предложений запрашивать для выдачи результата
		Return:
			response(str): статья с wiki
	"""


	wikipedia.set_lang('ru')
	response = wikipedia.summary(text, sentences=sentences)
	return response

def main():
	while True:
		request = input('Введите запрос(ru): ')
		try:
			res = wiki(request, sentences=limit)
			print(res)
		except Exception as e:
			print("Ошибка запроса")
			print(f"Error: {e}")
		



if __name__ == '__main__':
	main()