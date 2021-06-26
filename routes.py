import logging
import timeit

#Create and configure logger
logging.basicConfig(filename='app.log',
                    filemode='w',
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    datefmt='%d-%b-%y %H:%M:%S',
                    level=logging.DEBUG)

#Creating an object
logger=logging.getLogger()

class Routes:

    def __init__(self, graph):
        self.graph = graph

    # This will calculate the distance between the provided route
    def calc_distance_btwn_routes(self, route):
        start_time = timeit.default_timer()
        start_time_message = f'calc_distance_btwn_routes({route}): The start time is : {start_time}'
        print(start_time_message)
        logger.info(start_time_message)

        distance = 0
        for i in range(len(route)):
            origin_city = route[i]
            if i + 1 < len(route):
                next_city = route[i + 1]
                if next_city in self.graph[origin_city]:
                    distance += self.graph[origin_city][next_city]
                else:
                    return f'NO SUCH ROUTE - {route}'

        end_time = timeit.default_timer()
        end_time_message = f'calc_distance_btwn_routes({route}): The end time is : {end_time}'
        print(end_time_message)
        logger.info(end_time_message)

        time_difference = float(end_time) - float(start_time)
        time_diff_message = f'calc_distance_btwn_routes({route}): The time taken is : {time_difference}'
        print(time_diff_message)
        logger.info(time_diff_message)
        return f'The distance between route: {route} is {distance}'

    # It calculates the number of routes with the number of stops less than the provided in max_stops
    def calc_stops_btwn_routes(self, origin, destination, max_stops):
        method_name = f'calc_stops_btwn_routes({origin}, {destination}, {max_stops})'

        start_time = timeit.default_timer()
        start_time_message = f'{method_name}: The start time is : {start_time}'
        print(start_time_message)
        logger.info(start_time_message)

        response = 0
        if origin in self.graph and destination in self.graph:

            routes = self.get_diff_routes_from_origin(origin, [], [], [])

            for route in routes:
                if len(route) - 1 <= max_stops:
                    response += 1

            end_time = timeit.default_timer()
            end_time_message = f'{method_name}: The end time is : {end_time}'
            print(end_time_message)
            logger.info(end_time_message)

            time_difference = end_time - start_time
            time_diff_message = f'{method_name}: The time taken is : {time_difference}'
            print(time_diff_message)
            logger.info(time_diff_message)
            return f'Number of routes between {origin} and {destination} is "{response}" having maximum number of {max_stops} stops.'

        else:
            end_time = timeit.default_timer()
            end_time_message = f'{method_name}: The end time is : {end_time}'
            print(end_time_message)
            logger.info(end_time_message)

            time_difference = end_time - start_time
            time_diff_message = f'{method_name}: The time taken is : {time_difference}'
            print(time_diff_message)
            logger.info(time_diff_message)
            logger.warning(f'NO SUCH ROUTE FOUND FOR ORIGIN:{origin} and DESTINATION:{destination}')
            return 'NO SUCH ROUTE'

    # It finds the different routes between an origin to destination
    def get_diff_routes_from_origin(self, origin, routes=[], single_route=[], visited=[]):

        if origin in self.graph:

            if len(single_route) > 2 and single_route[-1] == single_route[0]:
                temp = single_route[0]
                single_route = [temp]

            single_route.append(origin)

            if len(single_route) > 1 and single_route[0] == origin and single_route not in routes:
                routes.append(single_route)

            if len(visited) == 0 or origin not in visited or (len(visited) > 0 and visited[0] == origin):
                visited.append(origin)
                for route in self.graph[origin]:
                    self.get_diff_routes_from_origin(route, routes, single_route)

        return routes
