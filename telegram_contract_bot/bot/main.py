import asyncio
import os
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.memory import MemoryStorage
from dotenv import load_dotenv

# Импорт хендлеров
from telegram_contract_bot.bot.handlers import (
    start_contract,
    get_contract_number,
    get_customer,
    get_director,
    get_date_and_generate,
    get_legal_address,
    get_postal_address,
    get_inn_kpp,
    get_ogrn,
    get_bank,
    get_bik,
    get_cor_account,
    get_checking_account,
    get_type_ts,
    get_number_ts,
    get_driver_info,
    get_cargo_name,
    get_cargo_weight,
    get_load_datetime,
    get_load_address,
    get_load_contact,
    get_unload_datetime,
    get_unload_address,
    get_unload_contact,
    get_danger_class,
    get_temp_mode,
    get_special_conditions,
    get_cost,
    get_penalties,
    get_phone_fax,
    get_email,
    get_name_ip,
    get_name_director,
)
from telegram_contract_bot.bot.states import ContractForm

# Загрузка переменных окружения
load_dotenv()
API_TOKEN = "8089549688:AAEClblB4zK6_vSb4dbKFWKAiwhNXGsDXQQ"

# Если переменная не найдена
if not API_TOKEN:
    raise ValueError("❌ BOT_TOKEN не найден в .env или переменной окружения!")

# Инициализация бота и диспетчера
bot = Bot(token=API_TOKEN)
dp = Dispatcher(storage=MemoryStorage())

# Команда /start
@dp.message(CommandStart())
async def command_start_handler(message: Message, state: FSMContext):
    await start_contract(message, state)

# Обработчики состояний
@dp.message(ContractForm.contract_number)
async def _(message: Message, state: FSMContext): await get_contract_number(message, state)

@dp.message(ContractForm.customer_name)
async def _(message: Message, state: FSMContext): await get_customer(message, state)

@dp.message(ContractForm.director_name)
async def _(message: Message, state: FSMContext): await get_director(message, state)

@dp.message(ContractForm.contract_date)
async def _(message: Message, state: FSMContext): await get_date_and_generate(message, state)

@dp.message(ContractForm.legal_address)
async def _(message: Message, state: FSMContext): await get_legal_address(message, state)

@dp.message(ContractForm.postal_address)
async def _(message: Message, state: FSMContext): await get_postal_address(message, state)

@dp.message(ContractForm.inn_kpp)
async def _(message: Message, state: FSMContext): await get_inn_kpp(message, state)

@dp.message(ContractForm.ogrn)
async def _(message: Message, state: FSMContext): await get_ogrn(message, state)

@dp.message(ContractForm.bank)
async def _(message: Message, state: FSMContext): await get_bank(message, state)

@dp.message(ContractForm.bik)
async def _(message: Message, state: FSMContext): await get_bik(message, state)

@dp.message(ContractForm.cor_account)
async def _(message: Message, state: FSMContext): await get_cor_account(message, state)

@dp.message(ContractForm.checking_account)
async def _(message: Message, state: FSMContext): await get_checking_account(message, state)

@dp.message(ContractForm.type_ts)
async def _(message: Message, state: FSMContext): await get_type_ts(message, state)

@dp.message(ContractForm.number_ts)
async def _(message: Message, state: FSMContext): await get_number_ts(message, state)

@dp.message(ContractForm.driver_info)
async def _(message: Message, state: FSMContext): await get_driver_info(message, state)

@dp.message(ContractForm.cargo_name)
async def _(message: Message, state: FSMContext): await get_cargo_name(message, state)

@dp.message(ContractForm.cargo_weight)
async def _(message: Message, state: FSMContext): await get_cargo_weight(message, state)

@dp.message(ContractForm.load_datetime)
async def _(message: Message, state: FSMContext): await get_load_datetime(message, state)

@dp.message(ContractForm.load_address)
async def _(message: Message, state: FSMContext): await get_load_address(message, state)

@dp.message(ContractForm.load_contact)
async def _(message: Message, state: FSMContext): await get_load_contact(message, state)

@dp.message(ContractForm.unload_datetime)
async def _(message: Message, state: FSMContext): await get_unload_datetime(message, state)

@dp.message(ContractForm.unload_address)
async def _(message: Message, state: FSMContext): await get_unload_address(message, state)

@dp.message(ContractForm.unload_contact)
async def _(message: Message, state: FSMContext): await get_unload_contact(message, state)

@dp.message(ContractForm.danger_class)
async def _(message: Message, state: FSMContext): await get_danger_class(message, state)

@dp.message(ContractForm.temp_mode)
async def _(message: Message, state: FSMContext): await get_temp_mode(message, state)

@dp.message(ContractForm.special_conditions)
async def _(message: Message, state: FSMContext): await get_special_conditions(message, state)

@dp.message(ContractForm.cost)
async def _(message: Message, state: FSMContext): await get_cost(message, state)

@dp.message(ContractForm.penalties)
async def _(message: Message, state: FSMContext): await get_penalties(message, state)

@dp.message(ContractForm.phone_fax)
async def _(message: Message, state: FSMContext): await get_phone_fax(message, state)

@dp.message(ContractForm.email)
async def _(message: Message, state: FSMContext): await get_email(message, state)

@dp.message(ContractForm.name_ip)
async def _(message: Message, state: FSMContext): await get_name_ip(message, state)

@dp.message(ContractForm.name_director)
async def _(message: Message, state: FSMContext): await get_name_director(message, state)

# Запуск бота
async def main():
    print("✅ Бот запущен. Ожидаю сообщения...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

