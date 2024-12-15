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
import asyncio

from bqskit.ir import Circuit
from bqskit.ir.gates import U3Gate, CXGate

from pytest import MyFirstPass

async def main():
# 创建一个包含 5 个比特的电路
# 创建一个简单的2比特电路
    circuit = Circuit(2)
    # 添加一个U3单比特门在qubit 0 上
    circuit.append_gate(U3Gate(), (0,), [0.1, 0.2, 0.3])
    # 添加一个CX二比特门在qubit 0和1上
    # 注意这里使用tuple (0,1) 而非 [0,1]
    circuit.append_gate(CXGate(), (0, 1))



    dummy_compiler = Compiler()
    from pytest import MyFirstPass


    dummy_workflow = Workflow([
        QuickPartitioner(3), 

        UnfoldPass(),
        MyFirstPass()
    ])


if __name__=="__main__":
    asyncio.run(main())