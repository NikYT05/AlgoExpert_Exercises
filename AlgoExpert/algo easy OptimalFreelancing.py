def optimalFreelancing(jobs):
    jobs.sort(key=sortPayment)
    jobs.sort(key=sortDeadline)
    days = 7
    while i != 
    return jobs

def sortPayment(jobs):
    return jobs['payment']

def sortDeadline(jobs):
    return jobs['deadline']


jobs = [
        {"deadline": 1, "payment": 1},
        {"deadline": 2, "payment": 1},
        {"deadline": 2, "payment": 2}
        ]

print(optimalFreelancing(jobs))