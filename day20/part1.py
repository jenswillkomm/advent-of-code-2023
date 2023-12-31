from enum import Enum
from abc import abstractmethod


input = '''broadcaster -> a, b, c
%a -> b
%b -> c
%c -> inv
&inv -> a
'''

input = '''broadcaster -> a
%a -> inv, con
&inv -> b
%b -> con
&con -> output
'''

# with open('input') as file:
#     input = file.read()


class Pulse(Enum):
    LOW = 0
    HIGH = 1


class Module:
    @abstractmethod
    def send(self, source, signal):
        # ignore
        return


class FlipFlop(Module):
    def __init__(self):
        # States:
        # * off := False
        # * on := True
        self.state = False

    def send(self, source, signal):
        if signal == Pulse.HIGH:
            return None

        self.state = not self.state
        if self.state:  # Is flip-flop on?
            return Pulse.HIGH
        else:
            return Pulse.LOW


class Conjunction(Module):
    def __init__(self):
        self.remember = {}

    def send(self, source, signal):
        self.remember[source] = signal
        if set(self.remember.values()) == {Pulse.HIGH}:
            return Pulse.LOW
        return Pulse.HIGH

    def addInput(self, name):
        self.remember[name] = Pulse.LOW


class Broadcaster(Module):
    def send(self, source, signal):
        return signal


def push_button(state):
    nbLowPulses = 0
    nbHighPulses = 0

    signalQueue = []
    # print('button -low-> broadcaster')
    signalQueue.append(('button', Pulse.LOW, 'broadcaster'))
    nbLowPulses += 1
    while signalQueue:
        source, signal, module = signalQueue.pop(0)
        if module not in state.keys():
            continue
        obj, destinations = state[module]
        nextSignal = obj.send(source, signal)
        if not nextSignal:
            continue
        for dest in destinations:
            # print(str(module) + ' -' + str(nextSignal) + '-> ' + str(dest))
            signalQueue.append((module, nextSignal, dest))
            if nextSignal == Pulse.HIGH:
                nbHighPulses += 1
            else:
                nbLowPulses += 1
    return state, nbLowPulses, nbHighPulses


destinationModules = {}
conjunctions = []
for line in input.splitlines():
    source, destinations = line.split(' -> ')
    obj = None
    name = source[1:]
    if source == 'broadcaster':
        obj = Broadcaster()
        name = source
    elif source[0] == '%':
        obj = FlipFlop()
    elif source[0] == '&':
        obj = Conjunction()
        conjunctions.append(name)
    destinationModules[name] = (obj, destinations.split(', '))
for m in destinationModules.keys():
    for c in conjunctions:
        if c in destinationModules[m][1]:
            destinationModules[c][0].addInput(m)

nbLowPulses = 0
nbHighPulses = 0
i = 0
for i in range(1000):
    destinationModules, lowPulses, highPulses = push_button(destinationModules)
    i += 1
    if i <= 1000:
        nbLowPulses += lowPulses
        nbHighPulses += highPulses


print(nbLowPulses * nbHighPulses)
