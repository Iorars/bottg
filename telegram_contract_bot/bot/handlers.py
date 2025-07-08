import os
from aiogram.types import Message, FSInputFile
from aiogram.fsm.context import FSMContext

from .states import ContractForm
from .contract_filler import fill_contract

# Пути к шаблону и выходному файлу
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
TEMPLATE_PATH = os.path.join(BASE_DIR, "templates", "contract_template.docx")
OUTPUT_PATH = os.path.join(BASE_DIR, "output", "contract_filled.docx")


async def start_contract(message: Message, state: FSMContext):
    await message.answer("📌 Введите номер договора:")
    await state.set_state(ContractForm.contract_number)

async def get_contract_number(message: Message, state: FSMContext):
    await state.update_data(contract_number=message.text)
    await message.answer("📌 Введите название заказчика:")
    await state.set_state(ContractForm.customer_name)

async def get_customer(message: Message, state: FSMContext):
    await state.update_data(customer_name=message.text)
    await message.answer("📌 Введите ФИО директора:")
    await state.set_state(ContractForm.director_name)

async def get_director(message: Message, state: FSMContext):
    await state.update_data(director_name=message.text)
    await message.answer("📌 Введите дату договора:")
    await state.set_state(ContractForm.contract_date)

async def get_date_and_generate(message: Message, state: FSMContext):
    await state.update_data(contract_date=message.text)
    await message.answer("📌 Введите юридический адрес:")
    await state.set_state(ContractForm.legal_address)

async def get_legal_address(message: Message, state: FSMContext):
    await state.update_data(legal_address=message.text)
    await message.answer("📌 Введите почтовый адрес:")
    await state.set_state(ContractForm.postal_address)

async def get_postal_address(message: Message, state: FSMContext):
    await state.update_data(postal_address=message.text)
    await message.answer("📌 Введите ИНН / КПП:")
    await state.set_state(ContractForm.inn_kpp)

async def get_inn_kpp(message: Message, state: FSMContext):
    await state.update_data(inn_kpp=message.text)
    await message.answer("📌 Введите ОГРН:")
    await state.set_state(ContractForm.ogrn)

async def get_ogrn(message: Message, state: FSMContext):
    await state.update_data(ogrn=message.text)
    await message.answer("📌 Введите название банка:")
    await state.set_state(ContractForm.bank)

async def get_bank(message: Message, state: FSMContext):
    await state.update_data(bank=message.text)
    await message.answer("📌 Введите БИК:")
    await state.set_state(ContractForm.bik)

async def get_bik(message: Message, state: FSMContext):
    await state.update_data(bik=message.text)
    await message.answer("📌 Введите корр. счёт:")
    await state.set_state(ContractForm.cor_account)

async def get_cor_account(message: Message, state: FSMContext):
    await state.update_data(cor_account=message.text)
    await message.answer("📌 Введите расчётный счёт:")
    await state.set_state(ContractForm.checking_account)

async def get_checking_account(message: Message, state: FSMContext):
    await state.update_data(checking_account=message.text)
    await message.answer("📌 Тип ТС:")
    await state.set_state(ContractForm.type_ts)

async def get_type_ts(message: Message, state: FSMContext):
    await state.update_data(type_ts=message.text)
    await message.answer("📌 Госномер ТС:")
    await state.set_state(ContractForm.number_ts)

async def get_number_ts(message: Message, state: FSMContext):
    await state.update_data(number_ts=message.text)
    await message.answer("📌 ФИО водителя:")
    await state.set_state(ContractForm.driver_info)

async def get_driver_info(message: Message, state: FSMContext):
    await state.update_data(driver_info=message.text)
    await message.answer("📌 Наименование груза:")
    await state.set_state(ContractForm.cargo_name)

async def get_cargo_name(message: Message, state: FSMContext):
    await state.update_data(cargo_name=message.text)
    await message.answer("📌 Масса груза:")
    await state.set_state(ContractForm.cargo_weight)

async def get_cargo_weight(message: Message, state: FSMContext):
    await state.update_data(cargo_weight=message.text)
    await message.answer("📌 Дата и время загрузки:")
    await state.set_state(ContractForm.load_datetime)

async def get_load_datetime(message: Message, state: FSMContext):
    await state.update_data(load_datetime=message.text)
    await message.answer("📌 Адрес загрузки:")
    await state.set_state(ContractForm.load_address)

async def get_load_address(message: Message, state: FSMContext):
    await state.update_data(load_address=message.text)
    await message.answer("📌 Контакт на месте загрузки:")
    await state.set_state(ContractForm.load_contact)

async def get_load_contact(message: Message, state: FSMContext):
    await state.update_data(load_contact=message.text)
    await message.answer("📌 Дата и время выгрузки:")
    await state.set_state(ContractForm.unload_datetime)

async def get_unload_datetime(message: Message, state: FSMContext):
    await state.update_data(unload_datetime=message.text)
    await message.answer("📌 Адрес выгрузки:")
    await state.set_state(ContractForm.unload_address)

async def get_unload_address(message: Message, state: FSMContext):
    await state.update_data(unload_address=message.text)
    await message.answer("📌 Контакт на месте выгрузки:")
    await state.set_state(ContractForm.unload_contact)

async def get_unload_contact(message: Message, state: FSMContext):
    await state.update_data(unload_contact=message.text)
    await message.answer("📌 Класс опасности:")
    await state.set_state(ContractForm.danger_class)

async def get_danger_class(message: Message, state: FSMContext):
    await state.update_data(danger_class=message.text)
    await message.answer("📌 Температурный режим:")
    await state.set_state(ContractForm.temp_mode)

async def get_temp_mode(message: Message, state: FSMContext):
    await state.update_data(temp_mode=message.text)
    await message.answer("📌 Особые условия:")
    await state.set_state(ContractForm.special_conditions)

async def get_special_conditions(message: Message, state: FSMContext):
    await state.update_data(special_conditions=message.text)
    await message.answer("📌 Стоимость перевозки:")
    await state.set_state(ContractForm.cost)

async def get_cost(message: Message, state: FSMContext):
    await state.update_data(cost=message.text)
    await message.answer("📌 Штрафы:")
    await state.set_state(ContractForm.penalties)

async def get_penalties(message: Message, state: FSMContext):
    await state.update_data(penalties=message.text)
    await message.answer("📌 Телефон/факс:")
    await state.set_state(ContractForm.phone_fax)

async def get_phone_fax(message: Message, state: FSMContext):
    await state.update_data(phone_fax=message.text)
    await message.answer("📌 Email:")
    await state.set_state(ContractForm.email)

async def get_email(message: Message, state: FSMContext):
    await state.update_data(email=message.text)
    await message.answer("📌 Введите название ИП:")
    await state.set_state(ContractForm.name_ip)

async def get_name_ip(message: Message, state: FSMContext):
    await state.update_data(name_ip=message.text)
    await message.answer("📌 Введите ФИО для подписи:")
    await state.set_state(ContractForm.name_director)

async def get_name_director(message: Message, state: FSMContext):
    await state.update_data(name_director=message.text)

    data = await state.get_data()

    replacements = {
        '{{contract_number}}': data['contract_number'],
        '{{customer_name}}': data['customer_name'],
        '{{director_name}}': data['director_name'],
        '{{contract_date}}': data['contract_date'],
        '{{legal_address}}': data['legal_address'],
        '{{postal_address}}': data['postal_address'],
        '{{inn_kpp}}': data['inn_kpp'],
        '{{ogrn}}': data['ogrn'],
        '{{bank}}': data['bank'],
        '{{bik}}': data['bik'],
        '{{cor_account}}': data['cor_account'],
        '{{checking_account}}': data['checking_account'],
        '{{type_ts}}': data['type_ts'],
        '{{number_ts}}': data['number_ts'],
        '{{driver_info}}': data['driver_info'],
        '{{cargo_name}}': data['cargo_name'],
        '{{cargo_weight}}': data['cargo_weight'],
        '{{load_datetime}}': data['load_datetime'],
        '{{load_address}}': data['load_address'],
        '{{load_contact}}': data['load_contact'],
        '{{unload_datetime}}': data['unload_datetime'],
        '{{unload_address}}': data['unload_address'],
        '{{unload_contact}}': data['unload_contact'],
        '{{danger_class}}': data['danger_class'],
        '{{temp_mode}}': data['temp_mode'],
        '{{special_conditions}}': data['special_conditions'],
        '{{cost}}': data['cost'],
        '{{penalties}}': data['penalties'],
        '{{phone_fax}}': data['phone_fax'],
        '{{email}}': data['email'],
        '{{name_ip}}': data['name_ip'],
        '{{name_director}}': data['name_director'],
    }

    try:
        fill_contract(TEMPLATE_PATH, OUTPUT_PATH, replacements)
        file = FSInputFile(OUTPUT_PATH)
        await message.answer_document(file, caption="✅ Ваш договор сформирован.")
    except Exception as e:
        await message.answer(f"❌ Ошибка при создании документа: {e}")

    await state.clear()



