from src.masonite.orm.grammar.mysql_grammar import MySQLGrammar 
from src.masonite.orm.blueprint.Blueprint import Blueprint
from src.masonite.orm.grammar.GrammarFactory import GrammarFactory 
from src.masonite.orm.schema.Schema import Schema
import unittest

class TestMySQLUpdateGrammar(unittest.TestCase):


    def setUp(self):
        self.schema = Schema.on('mysql')
        print(self.schema)
        # self.blueprint = 


    def test_can_compile_column(self):
        with self.schema.create('users') as blueprint:
            blueprint.string('name')

        sql = "CREATE TABLE `users` (`name` VARCHAR(255) NOT NULL)"
        self.assertEqual(blueprint.to_sql(), sql)

    def test_can_compile_multiple_columns(self):
        with self.schema.create('users') as blueprint:
            blueprint.string('name').nullable()
            blueprint.integer('age')

        print('query', blueprint.to_sql())

        sql = ("CREATE TABLE `users` ("
                "`name` VARCHAR(255), "
                "`age` INT(11) NOT NULL"
            ")"
        )
        self.assertEqual(blueprint.to_sql(), sql)

    def test_can_compile_not_null(self):
        with self.schema.create('users') as blueprint:
            blueprint.string('name')

        sql = ("CREATE TABLE `users` ("
                "`name` VARCHAR(255) NOT NULL"
            ")"
        )

        self.assertEqual(blueprint.to_sql(), sql)

    def test_can_compile_primary_key(self):
        with self.schema.create('users') as blueprint:
            blueprint.increments('id')
            blueprint.string('name')

        sql = ("CREATE TABLE `users` ("
                "`id` INT AUTO_INCREMENT PRIMARY KEY NOT NULL, "
                "`name` VARCHAR(255) NOT NULL"
            ")"
        )

        self.assertEqual(blueprint.to_sql(), sql)

    def test_can_compile_enum(self):
        with self.schema.create('users') as blueprint:
            blueprint.enum('age', [1,2,3]).nullable()

        sql = ("CREATE TABLE `users` ("
                "`age` ENUM('1','2','3')"
            ")"
        )

        self.assertEqual(blueprint.to_sql(), sql)

    def test_can_compile_large_blueprint(self):
        with self.schema.create('users') as blueprint:
            blueprint.string('name')
            blueprint.string('email')
            blueprint.string('password')
            blueprint.integer('age').nullable()
            blueprint.enum('type', ['Open', 'Closed'])
            blueprint.datetime('pick_up')
            blueprint.binary('profile')
            blueprint.boolean('of_age')
            blueprint.char('first_initial', length=4)
            blueprint.date('birthday')
            blueprint.decimal('credit', 17,6)
            blueprint.text('description')
            blueprint.unsigned('bank').nullable()

        sql = ("CREATE TABLE `users` ("
                "`name` VARCHAR(255) NOT NULL, "
                "`email` VARCHAR(255) NOT NULL, "
                "`password` VARCHAR(255) NOT NULL, "
                "`age` INT(11), "
                "`type` ENUM('Open','Closed') NOT NULL, "
                "`pick_up` DATETIME NOT NULL, "
                "`profile` LONGBLOB NOT NULL, "
                "`of_age` BOOLEAN NOT NULL, "
                "`first_initial` CHAR(4) NOT NULL, "
                "`birthday` DATE NOT NULL, "
                "`credit` DECIMAL(17, 6) NOT NULL, "
                "`description` TEXT NOT NULL, "
                "`bank` INT UNSIGNED"
            ")"
        )
        print('query', blueprint.to_sql())
        self.assertEqual(blueprint.to_sql(), sql)
