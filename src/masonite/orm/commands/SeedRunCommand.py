from cleo import Command
from ..seeds import Seeder


class SeedRunCommand(Command):
    """
    Run seeds.

    seed:run
        {--c|connection=default : The connection you want to run migrations on}
    """

    def handle(self):
        Seeder().run_database_seed()
