from app.handlers.about_us.about_us import router as about_router
from app.handlers.admin_panel.admin_panel import router as admin_router
from app.handlers.contact.Contact import router as contact_router
from app.handlers.command.main import router as command_router
from app.handlers.rules.rules import router as rules_router
from loader import dp

def include_routers():
    routers = [
        admin_router,
        about_router,
        contact_router,
        command_router,
        rules_router
    ]
    for router in routers:
        dp.include_router(router)

