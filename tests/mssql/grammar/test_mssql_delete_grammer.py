from src.masonite.orm.builder import QueryBuilder
from src.masonite.orm.grammar import GrammarFactory
import unittest


class TestMySQLDeleteGrammar(unittest.TestCase):
    def setUp(self):
        self.builder = QueryBuilder(GrammarFactory.make("mssql"), table="users")

    def test_can_compile_delete(self):
        to_sql = self.builder.delete("id", 1, query=True).to_sql()

        sql = "DELETE FROM [users] WHERE [users].[id] = '1'"
        self.assertEqual(to_sql, sql)

    def test_can_compile_delete_with_where(self):
        to_sql = (
            self.builder.where("age", 20)
            .where("profile", 1)
            .set_action("delete")
            .delete(query=True)
            .to_sql()
        )

        sql = (
            "DELETE FROM [users] WHERE [users].[age] = '20' AND [users].[profile] = '1'"
        )
        self.assertEqual(to_sql, sql)
