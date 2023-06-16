from amadeus import Client, ResponseError

amadeus = Client(
    client_id='xxxxx',
    client_secret='xxxxxx'
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
