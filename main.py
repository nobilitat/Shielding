from EmailSheilding import EmailSheilding
from PhoneNumberShielding import PhoneNumberShielding
from SkypeSheilding import SkypeSheilding


def main():
    # 1. Email
    email_service = EmailSheilding("aaaAA@mail.ru")
    print(email_service.shield())

    # 2. Phone number
    phone_number_service = PhoneNumberShielding('+7 666 777 888', 'x', 5)
    print(phone_number_service.shield())

    # 3. Skype
    skype_service = SkypeSheilding('<a href=\"skype:alex?call\">skype</a>')
    print(skype_service.shield())


if __name__ == "__main__":
    main()
