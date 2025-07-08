from aiogram.fsm.state import State, StatesGroup

class ContractForm(StatesGroup):
    contract_number = State()
    customer_name = State()
    director_name = State()
    contract_date = State()

    legal_address = State()
    postal_address = State()
    inn_kpp = State()
    ogrn = State()
    bank = State()
    bik = State()
    cor_account = State()
    checking_account = State()

    type_ts = State()
    number_ts = State()
    driver_info = State()
    cargo_name = State()
    cargo_weight = State()

    load_datetime = State()
    load_address = State()
    load_contact = State()

    unload_datetime = State()
    unload_address = State()
    unload_contact = State()

    danger_class = State()
    temp_mode = State()
    special_conditions = State()

    cost = State()
    penalties = State()

    phone_fax = State()
    email = State() 

    name_ip = State()
    name_director = State()