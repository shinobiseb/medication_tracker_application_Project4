""" A PostController Module """

from masonite.controllers import Controller
from masonite.request import Request
from app.Date import Date

class PostController(Controller):
    """Class Docstring Description
    """
    def __init__(self, request:Request):
        self.request = request

    def show(self):
        id = self.request.param("id")
        return Date.where("id", id).get()

    def index(self):
        return Date.all()

    def create(self):
        # REMEMBER THE REQUEST.INPUT
        date = self.request.input("date") 
        timetaken = self.request.input("timetaken")
        medname = self.request.input("medname")
        medamount = self.request.input("medamount")
        date = Date.create({"date": date, "timetaken": timetaken, "medname": medname, "medamount": medamount})
        return date

    def update(self):
        id = self.request.param("id")
        date = self.request.input("date")
        timetaken = self.request.input("timetaken")
        medname = self.request.input("medname")
        medamount = self.request.input("medamount")
        Date.where("id", id).update({"date": date, "timetaken": timetaken, "medname": medname, "medamount": medamount})
        return Date.where("id", id).get()

    def destroy(self):
        id = self.request.param("id")
        date = Date.where("id", id).get()
        Date.where("id", id).delete()
        return date