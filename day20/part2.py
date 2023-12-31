from enum import Enum
from abc import abstractmethod
import math


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
    lastConjunction_highPulse = []  # log who sends high pulses to the last conjunction

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
            if dest == lastConjunction and nextSignal == Pulse.HIGH:
                lastConjunction_highPulse.append(module)
    return state, nbLowPulses, nbHighPulses, lastConjunction_highPulse


destinationModules = {}
conjunctions = []
lastConjunction = ''
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
        if 'output' in destinations or 'rx' in destinations:
            assert lastConjunction == ''
            lastConjunction = name
    destinationModules[name] = (obj, destinations.split(', '))
for m in destinationModules.keys():
    for c in conjunctions:
        if c in destinationModules[m][1]:
            destinationModules[c][0].addInput(m)

nbLowPulses = 0
nbHighPulses = 0
cyclesLog = {}
i = 0
while cyclesLog.keys() != destinationModules[lastConjunction][0].remember.keys():  # found the cycles for all modules that input to the last conjunction
    destinationModules, lowPulses, highPulses, lastConjunction_highPulse = push_button(destinationModules)
    i += 1
    if i <= 1000:
        nbLowPulses += lowPulses
        nbHighPulses += highPulses

    for m in lastConjunction_highPulse:
        cyclesLog[m] = i


print(math.lcm(*cyclesLog.values()))
