import csv
from functools import reduce

with open('911_Calls.csv') as file:
    reader = csv.reader(file)
    data = [{x: y for x,y in row.items()}
    for row in csv.DictReader(file)]

filter(lambda x: x != 0, "zip_code")
filter(lambda x: x is None == False , "neighborhood")


total_response_time = [float(i['totalresponsetime']) for i in data if i['totalresponsetime']]
sum_total_response_time = reduce(lambda time1, time2: time1 + time2, total_response_time)
print(sum_total_response_time/len(data))

total_dispatch_time = [float(i["dispatchtime"]) for i in data if i['dispatchtime']]
sum_total_dispatch_time = reduce(lambda time1, time2: time1 + time2, total_dispatch_time)
print(sum_total_dispatch_time/len(data))

total_total_time = [float(i["totaltime"]) for i in data if i['totaltime']]
sum_total_total_time = reduce(lambda time1, time2: time1 + time2, total_total_time)
print(sum_total_total_time/len(data))

unique_neighborhoods = []
for i in data:
    if i["neighborhood"] not in unique_neighborhoods:
        unique_neighborhoods.append(i["neighborhood"])


def unique_neighborhood_list(clean_list, unique):
    n_list = []
    for i in clean_list:
        if i["neighborhood"] == unique:
            n_list.append(i)
    return n_list

neighborhood_list = list(map(lambda i: unique_neighborhood_list(data, i), unique_neighborhoods))

def standard_deviation(time_list):
    if len(time_list) > 1:
        sum_of_times = reduce(lambda time1, time2: time1 + time2, time_list)
        return sum_of_times/len(time_list)
    elif len(time_list) == 1:
        return time_list[0]

for i in neighborhood_list:
   (float(j['totalresponsetime']) for j in i if j['totalresponsetime'])
resopnse_times_list = []
for i in neighborhood_list:
    resopnse_times_list.append([float(j['totalresponsetime']) for j in i if j['totalresponsetime']])

avg_response_times = list(map(lambda x: standard_deviation(x), resopnse_times_list))


for i in neighborhood_list:
    (float(j['dispatchtime']) for j in i if j['dispatchtime'])
dispatch_times_list = []
for i in neighborhood_list:
    dispatch_times_list.append([float(j['dispatchtime']) for j in i if j['dispatchtime']])

avg_dspatch_times = list(map(lambda x: standard_deviation(x), dispatch_times_list))

total_times_list = []
for i in neighborhood_list:
    total_times_list.append([float(j['totaltime']) for j in i if j['totaltime']])

avg_total_times = list(map(lambda x: standard_deviation(x), total_times_list))

avg_times = []
for i in range(0, len(unique_neighborhoods)):
    avg_times.append({"neighborhood": f"{unique_neighborhoods[i]}", "avg_response_time": f"{avg_response_times[i]}", 
                      "avg_dispatch_time": f"{avg_dspatch_times[i]}", "avg_total_time": f"{avg_total_times[i]}"})
#print(*avg_times, sep = "\n")


import json
with open("911_Calls_data.json", "wt+") as file:
    json.dump(data,file)
with open("911_Calls_nieghborhoods.json", "wt+") as file:
    json.dump(neighborhood_list, file)
with open("911_Calls_avg_times.json", "wt+") as file:
    json.dump(avg_times, file)