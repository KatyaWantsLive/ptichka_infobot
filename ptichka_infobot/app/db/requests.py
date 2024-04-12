from app.db.models import async_session
from app.db.models import User, Event, Address
from sqlalchemy import select, delete


async def set_addres(data):
    async with async_session() as session:
        addres = await session.scalar(select(Address).where(Address.street == data['name']))

        if not addres:
            session.add(Address(street = data['name'], address_description = data['description']))
            await session.commit()

async def set_user(tg_id):
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id == tg_id))

        if not user:
            session.add(User(tg_id =  tg_id))
            await session.commit()


async def get_addres():
    async with async_session() as session:
        query = select(Address)
        result = await session.execute(query)
        return result.scalars().all()
    
async def get_address_description(address_id):
    async with async_session() as session:
        query = select(Address.address_description).where(Address.id == address_id)
        result = await session.execute(query)
        return result.scalars().one()
    
async def get_user_status(tg_id):
    async with async_session() as session:
        query = select(User).where(User.tg_id == tg_id)
        result = await session.execute(query)
        user = result.scalar()
        if user is not None:
            return user.is_admin
        else: return False

async def delete_work_site(addres_id):
    async with async_session() as session:
        query = delete(Address).where(Address.id == addres_id)
        await session. execute(query)
        await session.commit()