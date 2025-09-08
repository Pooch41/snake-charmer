from sqlalchemy import create_engine, text

QUERY_FLIGHT_BY_ID = ("SELECT flights.*, airlines.airline, "
                      "flights.ID as FLIGHT_ID, flights.DEPARTURE_DELAY as DELAY FROM flights "
                      "JOIN airlines ON flights.airline = airlines.ID WHERE flights.ID = :ID")

QUERY_FLIGHT_BY_DATE = ("SELECT flights.*, airlines.airline, "
                        "flights.ID as FLIGHT_ID, flights.DEPARTURE_DELAY as DELAY FROM flights "
                        "JOIN airlines ON flights.airline = airlines.ID "
                        "WHERE flights.DAY = :DAY "
                        "AND flights.MONTH = :MONTH "
                        "AND flights.YEAR = :YEAR")

QUERY_DELAYED_FLIGHT_BY_ORIGIN_AIRPORT = ("SELECT flights.*, airlines.airline, "
                                          "flights.ID as FLIGHT_ID, flights.DEPARTURE_DELAY as DELAY FROM flights "
                                          "JOIN airlines ON flights.airline = airlines.ID "
                                          "WHERE flights.ORIGIN_AIRPORT = :ORIGIN_AIRPORT "
                                          "AND flights.DEPARTURE_DELAY > 20")

QUERY_DELAYED_FLIGHT_BY_AIRLINE = ("SELECT flights.*, airlines.airline, "
                                   "flights.ID as FLIGHT_ID, flights.DEPARTURE_DELAY as DELAY FROM flights "
                                   "JOIN airlines ON flights.airline = airlines.ID "
                                   "WHERE airlines.AIRLINE = :AIRLINE "
                                   "AND flights.DEPARTURE_DELAY > 20")
# Define the database URL
DATABASE_URL = "sqlite:///data/flights.sqlite3"

# Create the engine
engine = create_engine(DATABASE_URL)


def execute_query(query, params):
    """
    Execute an SQL query with the params provided in a dictionary,
    and returns a list of records (dictionary-like objects).
    If an exception was raised, print the error, and return an empty list.
    """
    try:
        with engine.connect() as conn:
            result = conn.execute(text(query), params)
            return result.fetchall()
    except Exception as e:
        print("Query error:", e)
        return []


def get_flight_by_id(flight_id):
    """
    Searches for flight details using flight ID.
    If the flight was found, returns a list with a single record.
    """
    params = {'ID': flight_id}
    return execute_query(QUERY_FLIGHT_BY_ID, params)


def get_flights_by_date(day, month, year):
    """
    Searches for flight details using exact date.
    If flights were found, returns as many flights as found.
    """
    params = {'DAY': day,
              'MONTH': month,
              'YEAR': year}
    return execute_query(QUERY_FLIGHT_BY_DATE, params)


def get_delayed_flights_by_airline(airline: str):
    """
    Searches for flight details using airline name.
    If flights were found, returns as many flights as found. Delay means 20+ minutes.
    """
    params = {'AIRLINE': airline}
    return execute_query(QUERY_DELAYED_FLIGHT_BY_AIRLINE, params)


def get_delayed_flights_by_airport(airport: str):
    """
    Searches for flight details using origin airport code.
    If flights were found, returns as many flights as found. Delay means 20+ minutes.
    """
    params = {'ORIGIN_AIRPORT': airport}
    return execute_query(QUERY_DELAYED_FLIGHT_BY_ORIGIN_AIRPORT, params)
