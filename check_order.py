import configuration
import requests
import data

#Создание заказа
def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.USER_ORDER,
                         json=body)

response = post_new_user(data.user_body);

#Получаем номер заказа и сохраняем в переменной
track_number = response.json()['track']

#Запрос заказа по номеру
def get_order(track_number):
    return requests.get(configuration.URL_SERVICE + configuration.ORDER_GET + str(track_number))

order_response = get_order(track_number)

#Проверяем, что код ответа равен 200
def test_code():
    assert order_response.status_code == 200