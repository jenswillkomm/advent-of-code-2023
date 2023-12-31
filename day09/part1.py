input = '''0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45
'''

# with open('input') as file:
#     input = file.read()


def predict_next_value(history):
    if len([v for v in history if v != 0]) < 1:
        return 0
    nextVal = predict_next_value([history[i + 1] - history[i] for i in range(len(history) - 1)])
    return history[-1] + nextVal


history = list(map(lambda x: list(list(map(int, x.split(' ')))), input.splitlines()))
predValues = map(predict_next_value, history)

# print(list(predValues))


print(sum(predValues))
