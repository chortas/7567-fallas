from experta import *
from facts import *


class BeerDecider(KnowledgeEngine):
    def __init__(self):
        super().__init__()
        self.beers = []

    def get_beers(self):
        return self.beers

    """
    Maceración: Verter 15 litros de agua en el macerador. Macerar la malta pale durante 1 hora a 65 ºC para obtener el mosto.
    Ebullición: Añadir agua al mosto hasta tener 27 litros. Aumentar a temperatura de ebullición y añadir los lúpulos cuando se indica. La ebullición durará una 1 hora y 10 minutos.
    Fermentación: Fermentar a unos 18 ºC con levadura US-05 de fermentación alta para ales americanas.
    Acondicionamiento: Madurar a 12 ºC durante 10 días. Cebar la cerveza con azúcar y guardarla durante seis semanas a 18 ºC.
    """

    @Rule(BeerInfo(initial_gravity="Poco",
                   final_gravity="Poco",
                   color=MATCH.srm & P(lambda srm: 3 <= srm <= 7),
                   alcohol_graduation=MATCH.ag & P(
                       lambda ag: 4.1 <= ag <= 5.1),
                   bitterness=MATCH.ibu & P(lambda ibu: 15 <= ibu <= 25)))
    def pale_ale(self):
        beer = Beer(nombre="Pale Ale", color="Rubia", maltas=["pale", "caramel", "munich"], lupulo=["cascade", "centennial"], levadura=["ale"])
        self.declare(beer)

    @Rule(BeerInfo(initial_gravity="Regular",
                   final_gravity="Poco",
                   color=MATCH.srm & P(lambda srm: 6 <= srm <= 12),
                   alcohol_graduation=MATCH.ag & P(
                       lambda ag: 6.3 <= ag <= 7.5),
                   bitterness=MATCH.ibu & P(lambda ibu: 50 <= ibu <= 70)))
    def ipa(self):
        beer = Beer(nombre="IPA", color="Roja", maltas=["american two-row"], lupulo=["centennial", "simcoe", "amarillo"], levadura=["ale"])
        self.declare(beer)

    @Rule(BeerInfo(initial_gravity="Poco",
                   final_gravity="Mucho",
                   color=MATCH.srm & P(lambda srm: 39 <= srm <= 40),
                   alcohol_graduation=MATCH.ag & P(
                       lambda ag: 7 <= ag <= 12),
                   bitterness=MATCH.ibu & P(lambda ibu: 35 <= ibu <= 50)))
    def imperial_porter(self):
        beer = Beer(nombre="Imperial Porter", color="Negra", maltas=["varies"], lupulo=["varies"], levadura=["ale"])
        self.declare(beer)

    @ Rule(BeerInfo(initial_gravity="Muy poco",
                    final_gravity="Muy poco",
                    color=MATCH.srm & P(lambda srm: 40 <= srm <= 45),
                    alcohol_graduation=MATCH.ag & P(
                        lambda ag: 5.7 <= ag <= 8.7),
                    bitterness=MATCH.ibu & P(lambda ibu: 35 <= ibu <= 60)))
    def stout(self):
        beer = Beer(nombre="Stout", color="Negra", maltas=["pale", "black roasted barley", "special B", "caramunich", "chocolate", "pale chocolate"], lupulo=["horizon", "Kent Goldings"], levadura=["ale"])
        self.declare(beer)

    @ Rule(BeerInfo(initial_gravity="Poco",
                    final_gravity="Muy poco",
                    color=MATCH.srm & P(lambda srm: 11 <= srm <= 18),
                    alcohol_graduation=MATCH.ag & P(
                        lambda ag: 4.4 <= ag <= 6.1),
                    bitterness=MATCH.ibu & P(lambda ibu: 25 <= ibu <= 45)))
    def amber_ale(self):
        beer = Beer(nombre="Amber Ale", color="Roja", maltas=["english Pale Ale", "american two-row", "crystal", "victory"], lupulo=["horizon", "cascade", "centennial"], levadura=["ale"])
        self.declare(beer)

    @ Rule(BeerInfo(initial_gravity="Todo",
                    final_gravity="Todo",
                    color=MATCH.srm & P(lambda srm: 11 <= srm <= 18),
                    alcohol_graduation=MATCH.ag & P(
                        lambda ag: 8.5 <= ag <= 12.2),
                    bitterness=MATCH.ibu & P(lambda ibu: 60 <= ibu <= 100)))
    def american_barley_wine(self):
        beer = Beer(nombre="American Barley Wine", color="Roja", maltas=["pale", "crystal", "pale chocolate", "special B"], lupulo=["magnum", "chinook", "centennial", "amarillo"], levadura=["ale"])
        self.declare(beer)

    @ Rule(BeerInfo(initial_gravity="Muy poco",
                    final_gravity="Muy poco",
                    color=MATCH.srm & P(lambda srm: 3 <= srm <= 7),
                    alcohol_graduation=MATCH.ag & P(
                        lambda ag: 4.1 <= ag <= 5.1),
                    bitterness=MATCH.ibu & P(lambda ibu: 15 <= ibu <= 25)))
    def blonde_ale(self):
        beer = Beer(nombre="Blonde Ale", color="Rubia", maltas=["american two-row", "crystal"], lupulo=["williamette"], levadura=["lagger", "ale"])
        self.declare(beer)

    @ Rule(Beer(nombre=MATCH.beer_nombre, color=MATCH.beer_color, maltas=MATCH.beer_maltas, lupulo=MATCH.beer_lupulo, levadura=MATCH.beer_levadura))
    def chosen_beer(self, beer_nombre, beer_color, beer_maltas, beer_lupulo, beer_levadura):
        self.beers.append(Beer(nombre=beer_nombre, color=beer_color, maltas=beer_maltas, lupulo=beer_lupulo, levadura=beer_levadura))
        print(f"Chosen beer: {beer_nombre}")
