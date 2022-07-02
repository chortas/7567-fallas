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
        beer = Beer(nombre="Pale Ale", color="Rubia", maltas=["pale", "caramel", "munich"], lupulo=["cascade", "centennial"], levadura=["ale"], maceracion="Verter 15 litros de agua en el macerador. Macerar la malta pale durante 1 hora a 65 ºC para obtener el mosto.",
                    ebullicion="Añadir agua al mosto hasta tener 27 litros. Aumentar a temperatura de ebullición y añadir los lúpulos cuando se indica. La ebullición durará una 1 hora y 10 minutos.", fermentacion="Fermentar a unos 18 ºC con levadura US-05 de fermentación alta para ales americanas.", acondicionamiento="Madurar a 12 ºC durante 10 días. Cebar la cerveza con azúcar y guardarla durante seis semanas a 18 ºC.", foto="https://cocinista-vsf.netdna-ssl.com/download/bancorecursos/recetas/receta-cerveza-pale-ale-muntons.jpg")
        self.declare(beer)

    @Rule(BeerInfo(initial_gravity="Regular",
                   final_gravity="Poco",
                   color=MATCH.srm & P(lambda srm: 6 <= srm <= 12),
                   alcohol_graduation=MATCH.ag & P(
                       lambda ag: 6.3 <= ag <= 7.5),
                   bitterness=MATCH.ibu & P(lambda ibu: 50 <= ibu <= 70)))
    def ipa(self):
        beer = Beer(nombre="IPA", color="Roja", maltas=["american two-row"], lupulo=["centennial", "simcoe", "amarillo"], levadura=["ale"], maceracion="Macerar las maltas durante 60 minutos a 65 ºC. Usar 14 litros de agua.",
                    ebullicion="Lavar y recircular hasta obtener el mosto. Añadir agua hasta alcanzar los 27 litros. Hervir durante 60 minutos, añadiendo los lúpulos tal y como se explica anteriormente.", fermentacion="Añadir la levadura y fermentar a 22 ºC. Añadir el lúpulo del dry hopping al 4 día de feremtnación y dejarlo durante 6 días.", acondicionamiento="Madurar durante 3 semanas a 12 ºC.", foto="https://www.sietespirits.com/product_images/e/729/IPA__34221_zoom.jpg?id=1")
        self.declare(beer)

    @Rule(BeerInfo(initial_gravity="Poco",
                   final_gravity="Mucho",
                   color=MATCH.srm & P(lambda srm: 39 <= srm <= 40),
                   alcohol_graduation=MATCH.ag & P(
                       lambda ag: 7 <= ag <= 12),
                   bitterness=MATCH.ibu & P(lambda ibu: 35 <= ibu <= 50)))
    def imperial_porter(self):
        beer = Beer(nombre="Imperial Porter", color="Negra", maltas=["varies"], lupulo=["varies"], levadura=["ale"], maceracion="Se maceran las seis maltas en 19,2 litros de agua durante 1 hora a 67 ºC para obtener el mosto.", ebullicion="Añadir agua al mosto hasta obtener 27 litros y hervir durante 1 hora y 10 minutos. Llevar a ebullición y añadir el lúpulo en los momentos indicados anteriormente.",
                    fermentacion="Se fermenta el mosto con levadura de fermentación baja a unos 12 ºC.", acondicionamiento="Se debe guardar la cerveza fermentada durante 11 semanas a 12 ºC para que madure y se equilibre el carbónico.", foto="https://m.media-amazon.com/images/I/41hIo56JZyL.jpg")
        self.declare(beer)

    @ Rule(BeerInfo(initial_gravity="Muy poco",
                    final_gravity="Muy poco",
                    color=MATCH.srm & P(lambda srm: 40 <= srm <= 45),
                    alcohol_graduation=MATCH.ag & P(
                        lambda ag: 5.7 <= ag <= 8.7),
                    bitterness=MATCH.ibu & P(lambda ibu: 35 <= ibu <= 60)))
    def stout(self):
        beer = Beer(nombre="Stout", color="Negra", maltas=["pale", "black roasted barley", "special B", "caramunich", "chocolate", "pale chocolate"], lupulo=["horizon", "Kent Goldings"], levadura=["ale"], maceracion="Bañar el grano en 20 litros de agua para macerar y extraer el mosto. Tiempo requerido 1 hora a 65 ºC. Recircular y lavar bien para extraer todos los azúcares.",
                    ebullicion="Añadir agua al mosto hasta obtener 27 litros y comenzar e hervir. Añadir los lúpulos tal y como se indica anteriormente. Duración total de l hervido 1 hora y 15 minutos.", fermentacion="Fermentar con levaduras para cerveza ale, de fermentación alta, a unos 20 ºC.", acondicionamiento="Madurar la Imperial Stout a 12 ºC durante 15 semanas para obtener los sabores complejos de esta cerveza.", foto="https://www.nirobeer.com/wp-content/uploads/2019/07/KITS-NEGRA-600x600.png")
        self.declare(beer)

    @ Rule(BeerInfo(initial_gravity="Poco",
                    final_gravity="Muy poco",
                    color=MATCH.srm & P(lambda srm: 11 <= srm <= 18),
                    alcohol_graduation=MATCH.ag & P(
                        lambda ag: 4.4 <= ag <= 6.1),
                    bitterness=MATCH.ibu & P(lambda ibu: 25 <= ibu <= 45)))
    def amber_ale(self):
        beer = Beer(nombre="Amber Ale", color="Roja", maltas=["english Pale Ale", "american two-row", "crystal", "victory"], lupulo=["horizon", "cascade", "centennial"], levadura=["ale"], maceracion="Macerar las maltas durante 60 minutos a 65 ºC. Usar 20 litros de agua.",
                    ebullicion="Lavar y recircular hasta obtener el mosto. Añadir agua hasta alcanzar los 27 litros. Hervir durante 60 minutos, añadiendo los lúpulos tal y como se explica anteriormente.", fermentacion="Añadir levadura de Ale americana y fermentar a 18 – 20 ºC.", acondicionamiento="Madurar durante 5 semanas a 12 ºC.", foto="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT1v8GhELDJ3ftHNvJGwirmi5OzemMGYNyq4tK1eW-wdWvOlmo_sckj6fiAlRBbgnvQwII&usqp=CAU")
        self.declare(beer)

    @ Rule(BeerInfo(initial_gravity="Todo",
                    final_gravity="Todo",
                    color=MATCH.srm & P(lambda srm: 11 <= srm <= 18),
                    alcohol_graduation=MATCH.ag & P(
                        lambda ag: 8.5 <= ag <= 12.2),
                    bitterness=MATCH.ibu & P(lambda ibu: 60 <= ibu <= 100)))
    def american_barley_wine(self):
        beer = Beer(nombre="American Barley Wine", color="Roja", maltas=["pale", "crystal", "pale chocolate", "special B"], lupulo=["magnum", "chinook", "centennial", "amarillo"], levadura=["ale"], maceracion="Bañar a 67 ºC las maltas en 26 litros de agua, durante 1 hora, para obtener el mosto. Lavar y recircular el mosto con cuidado para obtener todos los azúcares fermentables.",
                    ebullicion="Añadir agua al mosto hasta obtener 27 litros y llevar a ebullición. Tiempo de hervido total 70 minutos. Añadir los lúpulos tal y como se explica anteriormente.", fermentacion="Se fermentará los 4 primeros días a 18ºC y el resto de lo que dure la fermentación a 22ºC.", acondicionamiento="Acondicionar a 12 ºC durante 13 semanas.", foto="https://cdn.justwineapp.com/assets/beer/bottle/imperial-centurion-american-barleywine-golden-city-brewery_1612478739.png")
        self.declare(beer)

    @ Rule(BeerInfo(initial_gravity="Muy poco",
                    final_gravity="Muy poco",
                    color=MATCH.srm & P(lambda srm: 3 <= srm <= 7),
                    alcohol_graduation=MATCH.ag & P(
                        lambda ag: 4.1 <= ag <= 5.1),
                    bitterness=MATCH.ibu & P(lambda ibu: 15 <= ibu <= 25)))
    def blonde_ale(self):
        beer = Beer(nombre="Blonde Ale", color="Rubia", maltas=["american two-row", "crystal"], lupulo=["williamette"], levadura=["lagger", "ale"], maceracion="Macerar las maltas durante 60 minutos a 65 ºC. Usar 16,25 litros de agua.",
                    ebullicion=" Lavar y recircular hasta obtener el mosto. Añadir agua hasta alcanzar los 27 litros. Hervir durante 70 minutos, añadiendo los lúpulos tal y como se explica anteriormente.", fermentacion="Añadir levadura de abadía y fermentar a unos 22 ºC.", acondicionamiento="Madurar durante 6 semanas a 12 ºC.", foto="https://cerveceriacoral.com/wp-content/uploads/2017/06/62-estilos-ale-734x1024.jpg")
        self.declare(beer)

    @ Rule(Beer(nombre=MATCH.beer_nombre, color=MATCH.beer_color, maltas=MATCH.beer_maltas, lupulo=MATCH.beer_lupulo, levadura=MATCH.beer_levadura, maceracion=MATCH.beer_maceracion, ebullicion=MATCH.beer_ebullicion, fermentacion=MATCH.beer_fermentacion, acondicionamiento=MATCH.beer_acondicionamiento, foto=MATCH.beer_foto))
    def chosen_beer(self, beer_nombre, beer_color, beer_maltas, beer_lupulo, beer_levadura, beer_maceracion, beer_ebullicion, beer_fermentacion, beer_acondicionamiento, beer_foto):
        self.beers.append(Beer(nombre=beer_nombre, color=beer_color,
                          maltas=beer_maltas, lupulo=beer_lupulo, levadura=beer_levadura, maceracion=beer_maceracion, ebullicion=beer_ebullicion, fermentacion=beer_fermentacion, acondicionamiento=beer_acondicionamiento, foto=beer_foto))
        print(f"Chosen beer: {beer_nombre}")
