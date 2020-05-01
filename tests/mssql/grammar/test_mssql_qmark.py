from src.masonite.orm.builder import QueryBuilder
from src.masonite.orm.grammar import GrammarFactory
import unittest


class TestMSSQLQmark(unittest.TestCase):
    def setUp(self):
        self.builder = QueryBuilder(GrammarFactory.make("mssql"), table="users")

    def test_can_compile_select(self):
        mark = self.builder.select("username").where("name", "Joe")

        sql = "SELECT [users].[username] FROM [users] WHERE [users].[name] = '?'"
        self.assertEqual(mark.to_qmark(), sql)
        self.assertEqual(mark._bindings, ("Joe",))

    def test_can_compile_update(self):
        mark = self.builder.update({"name": "Bob"}, dry=True).where("name", "Joe")

        sql = "UPDATE [users] SET [users].[name] = '?' WHERE [users].[name] = '?'"
        self.assertEqual(mark.to_qmark(), sql)
        self.assertEqual(mark._bindings, ("Bob", "Joe",))
