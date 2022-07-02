from experta import *
from facts import *


class BeerDecider(KnowledgeEngine):
    def __init__(self):
        super().__init__()
        self.beers = []

    def get_beers(self):
        return self.beers

    @Rule(BeerInfo(initial_gravity="Poco",
                   final_gravity="Poco",
                   color=MATCH.srm & P(lambda srm: 3 <= srm <= 7),
                   alcohol_graduation=MATCH.ag & P(
                       lambda ag: 4.1 <= ag <= 5.1),
                   bitterness=MATCH.ibu & P(lambda ibu: 15 <= ibu <= 25)))
    def pale_ale(self):
        beer = Beer(name="Pale Ale", color="Rubia", malts=["pale", "caramel", "munich"], hops=["cascade", "centennial"], yeast=["ale"])
        self.declare(beer)

    @Rule(BeerInfo(initial_gravity="Regular",
                   final_gravity="Poco",
                   color=MATCH.srm & P(lambda srm: 6 <= srm <= 12),
                   alcohol_graduation=MATCH.ag & P(
                       lambda ag: 6.3 <= ag <= 7.5),
                   bitterness=MATCH.ibu & P(lambda ibu: 50 <= ibu <= 70)))
    def ipa(self):
        beer = Beer(name="IPA", color="Roja", malts=["american two-row"], hops=["centennial", "simcoe", "amarillo"], yeast=["ale"])
        self.declare(beer)

    @Rule(BeerInfo(initial_gravity="Poco",
                   final_gravity="Mucho",
                   color=MATCH.srm & P(lambda srm: 39 <= srm <= 40),
                   alcohol_graduation=MATCH.ag & P(
                       lambda ag: 7 <= ag <= 12),
                   bitterness=MATCH.ibu & P(lambda ibu: 35 <= ibu <= 50)))
    def imperial_porter(self):
        beer = Beer(name="Imperial Porter", color="Negra", malts=["varies"], hops=["varies"], yeast=["ale"])
        self.declare(beer)

    @ Rule(BeerInfo(initial_gravity="Muy poco",
                    final_gravity="Muy poco",
                    color=MATCH.srm & P(lambda srm: 40 <= srm <= 45),
                    alcohol_graduation=MATCH.ag & P(
                        lambda ag: 5.7 <= ag <= 8.7),
                    bitterness=MATCH.ibu & P(lambda ibu: 35 <= ibu <= 60)))
    def stout(self):
        beer = Beer(name="Stout", color="Negra", malts=["pale", "black roasted barley", "special B", "caramunich", "chocolate", "pale chocolate"], hops=["horizon", "Kent Goldings"], yeast=["ale"])
        self.declare(beer)

    @ Rule(BeerInfo(initial_gravity="Poco",
                    final_gravity="Muy poco",
                    color=MATCH.srm & P(lambda srm: 11 <= srm <= 18),
                    alcohol_graduation=MATCH.ag & P(
                        lambda ag: 4.4 <= ag <= 6.1),
                    bitterness=MATCH.ibu & P(lambda ibu: 25 <= ibu <= 45)))
    def amber_ale(self):
        beer = Beer(name="Amber Ale", color="Roja", malts=["english Pale Ale", "american two-row", "crystal", "victory"], hops=["horizon", "cascade", "centennial"], yeast=["ale"])
        self.declare(beer)

    @ Rule(BeerInfo(initial_gravity="Todo",
                    final_gravity="Todo",
                    color=MATCH.srm & P(lambda srm: 11 <= srm <= 18),
                    alcohol_graduation=MATCH.ag & P(
                        lambda ag: 8.5 <= ag <= 12.2),
                    bitterness=MATCH.ibu & P(lambda ibu: 60 <= ibu <= 100)))
    def american_barley_wine(self):
        beer = Beer(name="American Barley Wine", color="Roja", malts=["pale", "crystal", "pale chocolate", "special B"], hops=["magnum", "chinook", "centennial", "amarillo"], yeast=["ale"])
        self.declare(beer)

    @ Rule(BeerInfo(initial_gravity="Muy poco",
                    final_gravity="Muy poco",
                    color=MATCH.srm & P(lambda srm: 3 <= srm <= 7),
                    alcohol_graduation=MATCH.ag & P(
                        lambda ag: 4.1 <= ag <= 5.1),
                    bitterness=MATCH.ibu & P(lambda ibu: 15 <= ibu <= 25)))
    def blonde_ale(self):
        beer = Beer(name="Blonde Ale", color="Rubia", malts=["american two-row", "crystal"], hops=["williamette"], yeast=["lagger", "ale"])
        self.declare(beer)

    @ Rule(Beer(name=MATCH.beer_name, color=MATCH.beer_color, malts=MATCH.beer_malts, hops=MATCH.beer_hops, yeast=MATCH.beer_yeast))
    def chosen_beer(self, beer_name, beer_color, beer_malts, beer_hops, beer_yeast):
        self.beers.append(Beer(name=beer_name, color=beer_color, malts=beer_malts, hops=beer_hops, yeast=beer_yeast))
        print(f"Chosen beer: {beer_name}")
