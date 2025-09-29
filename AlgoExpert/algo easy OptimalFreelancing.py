def optimalFreelancing(jobs):
    jobs.sort(key=sortDeadline)
    longest_dl = jobs[-1]["deadline"]

    jobs.sort(key=sortPayment)
    highest_val = 0
    

    return jobs

def sortPayment(e):
    return e["payment"]

def sortDeadline(e):
    return e['deadline']



print(optimalFreelancing([{"deadline": 1, "payment": 1}, {"deadline": 1, "payment": 3}, {"deadline": 2, "payment": 4}, {"deadline": 1, "payment": 2}]))