def droppedRequests(requestTime: list) -> int:
    # Write your code here
    total_dropped = 0
    for req_count, req_value in enumerate(requestTime):

        if req_count > 2 and requestTime[req_count] == requestTime[req_count - 3]:
            total_dropped += 1

        elif req_count > 19 and requestTime[req_count] - requestTime[req_count - 20] < 10:
            total_dropped += 1

        elif req_count > 59 and requestTime[req_count] - requestTime[req_count - 60] < 60:
            total_dropped += 1

    return total_dropped


requestTime = [1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 7, 11, 11, 11, 11]

print(droppedRequests(requestTime))
