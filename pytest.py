import sys
print(sys.executable)

import pbd

from bqskit import Circuit
from bqskit.ir.gates import U3Gate, CXGate
from bqskit import compile 
from bqskit.passes import *
from bqskit.compiler.basepass import BasePass
from bqskit.compiler import BasePass
from bqskit.compiler.passdata import PassData


class MyFirstPass(BasePass):
    def __init__(self):
        super().__init__()

    def run(self, circuit: Circuit, data: PassData) -> None:
        pbd.set_trace()
        #手动断点, hope it work
        count = circuit.count(CXGate)
        print(f"Number of CXGates: {count}")



import random

num_qubits = 5
circuit = Circuit(num_qubits)

for _ in range(10):
    if random.choice([True, False]):
        # 添加单比特门
        qubit = random.randint(0, num_qubits - 1)
        params = [random.uniform(0, 2 * 3.1415) for _ in range(3)]
        circuit.append_gate(U3Gate(), (qubit,), params)  # 单比特门的location用(0,)这种形式
    else:
        # 添加二比特门
        control = random.randint(0, num_qubits - 1)
        target = random.randint(0, num_qubits - 1)
        while target == control:
            target = random.randint(0, num_qubits - 1)
        circuit.append_gate(CXGate(), (control, target))  # 二比特门的location用(control,target)
