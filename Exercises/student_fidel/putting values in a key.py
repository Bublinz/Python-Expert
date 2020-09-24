keys = ['ten','twenty','thirty']
values = [10,20,30]
sample = dict(zip(keys, values))
print(sample)

me = {'ten': 10, 'twenty': 20}
be = {'thirty': 30, 'fourty': 40}
let = {**me,**be}
print(let)

simple = {
    "class":{
        "student":{
            "name": "john",
            "marks":{
                "physics": 80,
                "history": 90
                }
            }
        }
    }
print(simple["class"]["student"]["marks"]["history"])
