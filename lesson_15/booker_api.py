import requests

class BookerApi:
    def __init__(self, url):
        self.url = url

    def get_token(self,username,password):
        data = {
        "username": username,
        "password": password
        }
        resp = requests.post(f"{self.url}/auth", json=data)

        assert resp.status_code == 200, f"Ошибка: ожидался статус 200, получен {resp.status_code}"
        return resp.json()

    def get_booking_ids(self):
        resp = requests.get(f"{self.url}/booking")
        assert resp.status_code == 200, f"Ошибка: ожидался статус 200, получен {resp.status_code}"
        json_data = resp.json()
        assert all("bookingid" in item for item in json_data), "Ошибка: не все элементы содержат 'bookingid'"
        booking_ids = [item["bookingid"] for item in json_data]
        print(f"Получены ID бронирований: {booking_ids}")
        return booking_ids

    # def get_booking_list(self):
    #     resp = requests.get(f"{self.url}/booking")
    #     assert resp.status_code == 200, f"Ошибка: ожидался статус 200, получен {resp.status_code}"
    #     return resp.json()

    def create_booking(self, booking):
        resp = requests.post(f"{self.url}/booking", json=booking)
        assert resp.status_code == 200, f"Ошибка: ожидался статус 200, получен {resp.status_code}"
        return resp.json()

    def get_booking(self, booking_id):
        resp = requests.get(self.url + f'/booking/{booking_id}')
        assert resp.status_code == 200, f"Ошибка: ожидался статус 200, получен {resp.status_code}"
        return resp.json()
