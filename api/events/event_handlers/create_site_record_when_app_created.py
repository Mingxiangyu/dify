from events.app_event import app_was_created
from extensions.ext_database import db
from models.model import Site


@app_was_created.connect
def handle(sender, **kwargs):
    # 接收端都添加日志
    print("Signal received!")
    """Create site record when an app is created."""
    # 创建应用程序时创建站点记录
    app = sender
    account = kwargs.get("account")
    site = Site(
        app_id=app.id,
        title=app.name,
        icon_type=app.icon_type,
        icon=app.icon,
        icon_background=app.icon_background,
        default_language=account.interface_language,
        customize_token_strategy="not_allow",
        code=Site.generate_code(16),
    )

    db.session.add(site)
    db.session.commit()
