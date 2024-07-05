class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source_stop: int, target_stop: int) -> int:
        if source_stop == target_stop:
            return 0
        stop_to_routes_map = collections.defaultdict(list)
        for route_index, route in enumerate(routes):
            for stop in route:
                stop_to_routes_map[stop].append(route_index)
            routes[route_index] = set(route)
        visited_routes = set()
        routes_queue = stop_to_routes_map[source_stop][:]
        bus_count = 1

        while routes_queue:
            next_level_routes = []
            for current_route in routes_queue:
                if target_stop in routes[current_route]:
                    return bus_count

                if current_route in visited_routes:
                    continue

                visited_routes.add(current_route)
                for stop in routes[current_route]:
                    for next_route in stop_to_routes_map[stop]:
                        if next_route not in visited_routes:
                            next_level_routes.append(next_route)
            bus_count += 1
            routes_queue = next_level_routes

        return -1
