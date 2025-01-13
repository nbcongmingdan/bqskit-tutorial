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

class MyFirstPass(BasePass):
    def __init__(self):
        super().__init__()

    def run(self, circuit: Circuit, data: PassData) -> None:

        #手动断点, hope it work
        count = circuit.count(CXGate)
        print(f"Number of CXGates: {count}")




async def main():
# 创建一个包含 5 个比特的电路
# 创建一个简单的2比特电路
    circuit = Circuit(2)
    # 添加一个U3单比特门在qubit 0 上
    circuit.append_gate(U3Gate(), (0,), [0.1, 0.2, 0.3])
    # 添加一个CX二比特门在qubit 0和1上
    circuit.append_gate(CXGate(), (0, 1))

    # 打印电路状态
    print(f"Initial circuit: {circuit}")


    # 示例异步操作
    await asyncio.sleep(1)
    print("Asynchronous operation completed.")

    dummy_compiler = Compiler()

    dummy_workflow = Workflow([
        QuickPartitioner(3), 

        UnfoldPass(),
        MyFirstPass()
    ])


if __name__=="__main__":
     # 确认 main 是协程函数
    print(f"main is a coroutine function: {asyncio.iscoroutinefunction(main)}")  # 应输出 True
    asyncio.run(main())