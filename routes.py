import timeit

from logconfig import LogConfig

log_config = LogConfig()
logger = log_config.logger_config()


class Routes:

    def __init__(self, graph):
        self.graph = graph

    # This will calculate the distance between the provided route
    def calc_distance_btwn_routes(self, route):
        start_time = timeit.default_timer()
        start_time_message = f'calc_distance_btwn_routes({route}): The start time is : {start_time}'
        print(start_time_message)
        logger.info(start_time_message)

        try:
            distance = 0

            if len(route) == 0:
                raise Exception('Route should not be blank.')

            for i in range(len(route)):
                origin_city = route[i]
                if i + 1 < len(route):
                    next_city = route[i + 1]
                    if next_city in self.graph[origin_city]:
                        distance += self.graph[origin_city][next_city]
                    else:
                        logger.warning(f'NO SUCH ROUTE - {route}')
                        return f'NO SUCH ROUTE - {route}'
        except Exception as exception:
            logger.exception(f'Exception occured in calc_distance_btwn_routes({route}): {exception}')

        end_time = timeit.default_timer()
        end_time_message = f'calc_distance_btwn_routes({route}): The end time is : {end_time}'
        print(end_time_message)
        logger.info(end_time_message)

        time_difference = float(end_time) - float(start_time)
        time_diff_message = f'calc_distance_btwn_routes({route}): The time taken is : {time_difference}'
        print(time_diff_message)
        logger.info(time_diff_message)
        return f'The distance between route: {route} is {distance}'

    # It calculates the number of routes with the number of stops less than the provided in max_stops between the origin and destination (i.e., origin)
    def calc_stops_btwn_routes(self, origin, max_stops):
        method_name = f'calc_stops_btwn_routes({origin}, {max_stops})'

        start_time = timeit.default_timer()
        start_time_message = f'{method_name}: The start time is : {start_time}'
        print(start_time_message)
        logger.info(start_time_message)

        if origin in self.graph:
            response = self.get_number_stops_btwn_route(max_stops, origin)
            response_message = f'Number of routes between {origin} and {origin} having maximum ' \
                               f'number of {max_stops} stops is "{response}". '
        else:
            logger.warning(f'NO SUCH ROUTE FOUND FOR ORIGIN:{origin} and DESTINATION:{origin}')
            response_message = 'NO SUCH ROUTE'

        end_time = timeit.default_timer()
        end_time_message = f'{method_name}: The end time is : {end_time}'
        print(end_time_message)
        logger.info(end_time_message)

        time_difference = end_time - start_time
        time_diff_message = f'{method_name}: The time taken is : {time_difference}'
        print(time_diff_message)
        logger.info(time_diff_message)

        return response_message

    # It returns the number of routes from origin to origin, with stops not more than max_stops
    def get_number_stops_btwn_route(self, max_stops, origin):
        response = 0
        routes = self.get_diff_routes_from_origin(origin, [], [], [])
        for route in routes:
            if len(route) - 1 <= max_stops:
                response += 1
        return response

    # It finds the different routes starting from an origin to back to origin
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
