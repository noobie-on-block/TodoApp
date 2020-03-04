from unittest import TestCase
from app import create_app, db
from sqlalchemy import inspect
from app.models import Todo, List


class DatabaseTestCase(TestCase):
    def setUp(self) -> None:
        app = create_app('testing')
        self.app_ctx = app.app_context()
        self.app_ctx.push()
        db.create_all()
        self.inspector = inspect(db.engine)

    def tearDown(self) -> None:
        db.session.remove()
        db.drop_all()
        self.app_ctx.pop()

    def test_models_exist(self):
        tables = self.inspector.get_table_names()
        self.assertIn('lists', tables)
        self.assertIn('todos', tables)

    def test_insertion(self):
        task_list = List(title="tasks")
        task_list.todos = [Todo(title="exercise"), Todo(title="office"),
                          Todo(title="breakfast")]
        db.session.add(task_list)
        db.session.commit()

        self.assertEqual(len(List.query.all()), 1)
        self.assertEqual(len(Todo.query.all()), 3)

    def test_deletion_of_orphans(self):
        task_list = List(title="tasks")
        work_list = List(title="work")
        task_list.todos = [Todo(title="exercise"), Todo(title="office"),
                           Todo(title="breakfast")]
        work_list.todos = [Todo(title="health insurance"), Todo(title="support")]
        db.session.add_all([task_list, work_list])
        db.session.commit()

        db.session.delete(task_list)
        db.session.commit()

        self.assertEqual(len(Todo.query.all()), len(work_list.todos))
