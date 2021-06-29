import unittest

from routes import Routes


class TestRoutesMethods(unittest.TestCase):

    # This function will be called before each method in your test class.
    @classmethod
    def setUpClass(cls):
        # Graph: AB5, BC4, CD8, DC8, DE6, AD5, CE2, EB3, AE7
        cls.graph = {
            'A': {'B': 5, 'D': 5, 'E': 7},
            'B': {'C': 4},
            'C': {'D': 8, 'E': 2},
            'D': {'C': 8, 'E': 6},
            'E': {'B': 3}
        }

    # AssertEquals Example
    def test_calc_distance_btwn_routes(self):
        routes = Routes(self.graph)
        self.assertEqual(routes.calc_distance_btwn_routes(['A', 'D']),
                         'The distance between route: [\'A\', \'D\'] is 5')

    # AssertTrue Example
    def test_get_number_stops_btwn_route(self):
        routes = Routes(self.graph)
        self.assertTrue(routes.get_number_stops_btwn_route(3, 'C') == 2)

    # AssertRaises Example
    def test_calc_distance_btwn_routes_assert_raises(self):
        routes = Routes(self.graph)
        self.assertRaises(Exception, routes.calc_distance_btwn_routes([]))

    # AssertGreater Example
    def test_get_number_stops_btwn_route_assert_greater(self):
        routes = Routes(self.graph)
        self.assertGreater(routes.get_number_stops_btwn_route(3, 'C'), 0)


if __name__ == '__main__':
    unittest.main()
