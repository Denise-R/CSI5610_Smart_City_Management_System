class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        #implementing scan algorithm

        #initiate results list
        results = [0]*n
        #initiate empty list for flight and seats
        flights = []

        for (i, j, k) in bookings:
            #append the start(i)/end(j) (inclusive), and corresponding seats (k)
            flights.append((i - 1, k))
            flights.append((j, -k))
        #print(flights)
        #sort the flights list
        flights.sort()
        #print(flights)
        for flight in flights:
            #if flights surpasses the length of n
            if flight[0] >= n:
                continue
            #else
            results[flight[0]] += flight[1]

        #prefix sum
        for i in range(1, n):
            results[i] += results[i-1]
        return results
