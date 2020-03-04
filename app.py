from app import create_app, db
from flask_migrate import Migrate
from app.models import List, Todo

app = create_app('testing')
migrate = Migrate(app, db)


@app.shell_context_processor
def make_shell_context():
    return dict(db=db, List=List, Todo=Todo)
