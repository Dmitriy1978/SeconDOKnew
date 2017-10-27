class names_log:
    email = "dmitriy222@i.ua"
    password1 = "12345678"
    password2 = "12345678"


    def __init__(self, email=None, password=None):
        self.email = email
        self.password = password

class info_user:

    firstname = "Testerq"
    lastname = "Qtester"
    avatar_file = "\\Doctor.jpg"
    country = "Ukr"
    city = "Kharkiv"
    phone = "123456789"

    def __init__(self, firstname=None, lastname=None, avatar_file=None, country=None, city=None, phone=None):
        self.firstname = firstname
        self.lastname = lastname
        self.avatar_file = avatar_file
        self.city = city
        self.country = country
        self.phone = phone

class info_education:
    country = "Ukraine"
    city = "khar"
    university_name = "Kharkiv national university of V. Karazin (KNU)"
    start_year = "1970"
    finished_year = "1978"
    diplom_file_1 = "\\diplom1.jpg"
    diplom_file_2 = "\\diplom2.jpg"
    specialization = "Toxicology"
    qualification = "Professor"

    def __init__(self, country=None, city=None, university_name=None, start_year=None, finished_year=None, diplom_file_1 = None, diplom_file_2 = None, specialization = None, qualification = None):

        self.diplom_file_1 = diplom_file_1
        self.diplom_file_2 = diplom_file_2
        self.city = city
        self.country = country
        self.university_name = university_name
        self.start_year = start_year
        self.finished_year = finished_year
        self.specialization = specialization
        self.qualification = qualification

class info_profession:
    country = "Ukraine"
    city = "Kiev"
    institution = "Branch of polyclinic №1 of Solomensky district of Kyiv"
    start_year = "1995"
    finished_year = "2001"
    speciality = "Triholog"
    speciality1 = "Trihology"
    Position = "Doctor"

    def __init__(self, country=None, city=None, institution=None, start_year=None, finished_year=None, speciality = None, speciality1 = None, Position = None):

        self.institution = institution
        self.country = country
        self.city = city
        self.country = country
        self.start_year = start_year
        self.finished_year = finished_year
        self.speciality = speciality
        self.speciality1 = speciality1
        self.Position = Position

class info_add:
    add = "— «Нимфа», туды её в качель, разве товар даёт? — смутно молвил гробовой мастер. — Разве ж она может покупателя удовлетворить? Гроб — он одного лесу сколько требует…"

    def __init__(self, add=None):
        self.add = add

class info_bill:
    bill = "1234567812345678"

    def __init__(self, bill=None):
        self.bill = bill

class info_mail:
    mail = "dmitriy222@i.ua"
    password = "dmitriy20"

    def __init__(self, mail=None, login=None):
        self.mail = mail
        self.login = login

class info_login:
    email = "dmitriy222@i.ua"
    password = "12345678"

    def __init__(self, email=None, password=None):
        self.email = email
        self.password = password

class info_db:
    email = "admin@secondok.com"
    password = "net46craft14"

    def __init__(self, email=None, password=None):
        self.email = email
        self.password = password
