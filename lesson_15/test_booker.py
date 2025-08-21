from lesson_15.booker_api import BookerApi

base_url = "https://restful-booker.herokuapp.com"
api = BookerApi(base_url)


def test_get_token():
    resp = api.get_token("admin", "password123")
    assert resp["token"] != "", f"Токен пустой"


def test_get_booking_ids():
    api.get_booking_ids()


# def test_get_booking_list():
#     resp = api.get_booking_list()
#     assert all(d.get("bookingig") for d in resp)


def test_create_booking():
    booking = {
        "firstname": "Jim",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }

    resp = api.create_booking(booking)
    assert resp["bookingid"] != "", "Нет id"


def test_get_booking():
    booking = {
        "firstname": "Jil",
        "lastname": "White",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }

    new_booking = api.create_booking(booking)
    booking_id = new_booking["bookingid"]

    resp = api.get_booking(booking_id)
    assert resp["firstname"] == "Jil"
