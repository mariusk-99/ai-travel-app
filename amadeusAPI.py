from amadeus import Client, ResponseError

amadeus = Client(
    client_id='ulVH5r4YFKMxhaBOx6YVq5UxR1Qxsely',
    client_secret='O1unGcw4cnDh6GDZ'
)

try:
    response = amadeus.shopping.flight_offers_search.get(
        originLocationCode='MAD',
        destinationLocationCode='ATH',
        departureDate='2023-11-01',
        adults=1)
    print(response.data)
except ResponseError as error:
    print(error)
