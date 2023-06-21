"""CreateDatesTable Migration."""

from masoniteorm.migrations import Migration


class CreateDatesTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("dates") as table:
            table.increments("id")
            table.date("date")
            table.string("timetaken")
            table.string("medname")
            table.integer("medamount")
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("dates")
