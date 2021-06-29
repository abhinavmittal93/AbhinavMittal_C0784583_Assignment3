Problem:  
In this problem, you will help the railroad provide its customers with information about the routes.  In particular, you will compute the distance along a certain route, the number of different routes between two towns, and the shortest route between two towns.

Input:  A directed graph where a node represents a town, and an edge represents a route between two towns.  The weighting of the edge represents the distance between the two towns.  A given route will never appear more than once, and for a given route, the starting and ending town will not be the same town.

Output: For test input 1 through 5, if no such route exists, output 'NO SUCH ROUTE'.  Otherwise, follow the route as given; do not make any extra stops!  For example, the first problem means to start at city A, then travel directly to city B (a distance of 5), then directly to city C (a distance of 4). 

A1) Calculate the distance of the route A-B-C.
A2) The distance of the route A-D.
A3) The distance of the route A-D-C.
A4) The distance of the route A-E-B-C-D.
A5) The distance of the route A-E-D



B1) The number of trips starting at C and ending at C with a maximum of 3 stops.  In the sample data below, there are two such trips: C-D-C (2 stops). and C-E-B-C (3 stops).


<b>Graph for the routes: AB5, BC4, CD8, DC8, DE6, AD5, CE2, EB3, AE7</b>
