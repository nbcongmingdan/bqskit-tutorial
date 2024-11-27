from bqskit import Circuit
from bqskit import compile 
from bqskit.passes import *
from bqskit.compiler import Compiler
from bqskit.compiler.compile import get_instantiate_options 
from bqskit.compiler.basepass import BasePass
from bqskit.compiler import BasePass, Compiler, Workflow
from bqskit.compiler.passdata import PassData


from bqskit.passes.partitioning import QuickPartitioner
from bqskit.passes.synthesis.qsearch import QSearchSynthesisPass
from bqskit.passes.processing import ScanningGateRemovalPass 
from bqskit.passes.control.foreach import ForEachBlockPass


# from bqskit.passes import PassGroup

import random
from bqskit.ir import Circuit
from bqskit.ir.gates import U3Gate, CXGate

# 创建一个包含 5 个比特的电路
num_qubits = 5
circuit = Circuit(num_qubits)

# 随机添加门到电路中
for _ in range(10):  # 添加 10 个门
    if random.choice([True, False]):
        # 添加单比特门（U3Gate）
        qubit = random.randint(0, num_qubits - 1)
        params = [random.uniform(0, 2 * 3.1415) for _ in range(3)]
        circuit.append_gate(U3Gate(), [qubit], params)
    else:
        # 添加双比特门（CXGate）
        control = random.randint(0, num_qubits - 1)
        target = random.randint(0, num_qubits - 1)
        while target == control:
            target = random.randint(0, num_qubits - 1)
        circuit.append_gate(CXGate(), [control, target])





dummy_compiler = Compiler()
from pytest import MyFirstPass


dummy_workflow = Workflow([
    QuickPartitioner(3), 

    UnfoldPass(),
    MyFirstPass()
])