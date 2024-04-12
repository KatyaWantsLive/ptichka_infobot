from app.db.models import async_session
from app.db.models import User, Event, Address
from sqlalchemy import select


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