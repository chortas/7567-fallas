from experta import *

class BeerDecider(KnowledgeEngine):
    def __init__(self):
        super().__init__()
        self.beers = []

    def get_beers(self):
      return self.beers

    @Rule(Fact(initial_gravity="Poco",
               final_gravity="Poco",
               color="Muy poco",
               alcohol_graduation="Muy poco",
               bitterness="Muy poco"))
    def pale_ale(self):
        beer = Fact(name="Pale Ale")
        self.declare(beer)

    @Rule(Fact(initial_gravity="Regular",
               final_gravity="Poco",
               color="Poco",
               alcohol_graduation="Poco",
               bitterness="Mucho"))
    def ipa(self):
        beer = Fact(name="IPA")
        self.declare(beer)

    @Rule(Fact(initial_gravity="Poco",
               final_gravity="Mucho",
               color="Todo",
               alcohol_graduation="Mucho",
               bitterness="Regular"))
    def imperial_porter(self):
        beer = Fact(name="Imperial Porter")
        self.declare(beer)

    @Rule(Fact(initial_gravity="Muy poco",
               final_gravity="Muy poco",
               color="Todo",
               alcohol_graduation="Regular",
               bitterness="Regular"))
    def stout(self):
        beer = Fact(name="Stout")
        self.declare(beer)

    @Rule(Fact(initial_gravity="Poco",
               final_gravity="Muy poco",
               color="Regular",
               alcohol_graduation="Muy poco",
               bitterness="Poco"))
    def amber_ale(self):
        beer = Fact(name="Amber Ale")
        self.declare(beer)

    @Rule(Fact(initial_gravity="Todo",
               final_gravity="Todo",
               color="Regular",
               alcohol_graduation="Todo",
               bitterness="Todo"))
    def american_barley_wine(self):
        beer = Fact(name="American Barley Wine")
        self.declare(beer)

    @Rule(Fact(initial_gravity="Muy poco",
               final_gravity="Muy poco",
               color="Muy poco",
               alcohol_graduation="Muy poco",
               bitterness="Muy poco"))
    def blonde_ale(self):
        beer = Fact(name="Blonde Ale")
        self.declare(beer)

    @Rule(Fact(name=MATCH.beer_name))
    def chosen_beer(self, beer_name):
        self.beers.append(Fact(name=beer_name))
        print(f"Chosen beer: {beer_name}")
