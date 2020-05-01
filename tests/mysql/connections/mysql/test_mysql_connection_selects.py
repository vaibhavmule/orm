from src.masonite.orm.builder import QueryBuilder
from src.masonite.orm.grammar import GrammarFactory
from src.masonite.orm.models import Model
import unittest
import os


class MockUser(Model):

    __table__ = "users"


if os.getenv("RUN_MYSQL_DATABASE", False) == "True":

    class TestMySQLSelectConnection(unittest.TestCase):
        def setUp(self):
            self.builder = QueryBuilder(GrammarFactory.make("mysql"), table="users")

        def test_can_compile_select(self):
            to_sql = MockUser.where("id", 1).to_sql()

            sql = "SELECT * FROM `users` WHERE `users`.`id` = '1'"
            self.assertEqual(to_sql, sql)

        def test_can_get_first_record(self):
            user = MockUser.where("id", 1).first()
            self.assertEqual(user.id, 1)

        def test_can_find_first_record(self):
            user = MockUser.find(1)
            self.assertEqual(user.id, 1)

        def test_can_get_all_records(self):
            users = MockUser.all()
            self.assertGreater(len(users), 1)

        def test_can_get_5_records(self):
            users = MockUser.limit(5).get()
            self.assertEqual(len(users), 5)

        def test_can_get_1_record_with_get(self):
            users = MockUser.where("id", 1).limit(5).get()
            self.assertEqual(len(users), 1)

            users = MockUser.limit(5).where("id", 1).get()
            self.assertEqual(len(users), 1)
