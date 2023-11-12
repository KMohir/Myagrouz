from aiogram.dispatcher.filters.state import StatesGroup, State

class imagestate(StatesGroup):
    image1 = State()
    image2=State()

class answer(StatesGroup):
    A1 = State()
    A2 = State()

class language(StatesGroup):
    lang = State()
class cancelmain(StatesGroup):
    cancel = State()
class questions(StatesGroup):
    answer = State()
class RegistrationStates(StatesGroup):
    lang=State()
    name = State()
    phone = State()
    end = State()
    number=State()
    help = State()
    chatgpt=State()
    chatgptfull=State()

class ariza(StatesGroup):
    name = State()
    fename = State()
    email = State()
    phone = State()
    direction=State()
    directiontwo=State()
    Region=State()
    school = State()
    grades = State()
    grades_id = State()
    gender = State()
    about=State()
    document=State()
    file=State()
    check=State()
    emailcheck=State()


