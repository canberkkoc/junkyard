def droppedRequests(requestTime: list) -> int:
    # Write your code here
    total_dropped = 0
    for req_count, req_value in enumerate(requestTime):

        if req_count > 2 and requestTime[req_count] == requestTime[req_count - 3]:
            total_dropped += 1
            # For visual purpose
            print(f'1 second 3 request violation on {req_value} come {requestTime.count(req_value)} th time ')

        elif req_count > 19 and requestTime[req_count] - requestTime[req_count - 20] < 10:
            total_dropped += 1
            # For visual purpose
            print(f'10 second 20 request violation on {req_value} come {req_count + 1} th time ')

        elif req_count > 59 and requestTime[req_count] - requestTime[req_count - 60] < 60:
            # For visual purpose
            print(f'60 second 60 request violation on {req_value} come {req_count + 1} th time ')
            total_dropped += 1

    return total_dropped


requestTime = [1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 7, 11, 11, 11, 11]

print(droppedRequests(requestTime))
