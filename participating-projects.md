---
layout: page
title: Projects
---

> #### You can see all of the tagged issues on GitHub [here](https://github.com/topics/unitaryhack)!

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:grey;border-style:none;border-width:1px;
  overflow:hidden;padding:5px 5px;word-break:normal;}
.tg .tg-sj11{!important;;font-size:medium; text-align:left;vertical-align:middle}
</style>
<table class="tg">
<tbody>
  <tr>
    <td class="tg-sj11"><a href="#mitiq">Mitiq</a></td>
    <td class="tg-sj11"><a href="#pennylane">PennyLane</a></td>
    <td class="tg-sj11"><a href="#strawberry-fields">Strawberry Fields</a></td>
    <td class="tg-sj11"><a href="#the-walrus">The Walrus</a></td>
  </tr>
  <tr>
    <td class="tg-sj11"><a href="#toqito">toqito</a></td>
    <td class="tg-sj11"><a href="#scirate">SciRate</a></td>
    <td class="tg-sj11"><a href="#qunetsim">QuNetSim</a></td>
    <td class="tg-sj11"><a href="#interlin-q">Interlin-q</a></td>
  </tr>
  <tr>
    <td class="tg-sj11"><a href="#qrand">QRAND</a></td>
    <td class="tg-sj11"><a href="#qrack">Qrack</a></td>
    <td class="tg-sj11"><a href="#qutip">QuTiP</a></td>
    <td class="tg-sj11"><a href="#pulser">Pulser</a></td>
  </tr>
  <tr>
    <td class="tg-sj11"><a href="#qcor">QCOR</a></td>
    <td class="tg-sj11"><a href="#xacc">XACC</a></td>
    <td class="tg-sj11"><a href="#qosf-monthly-challenges">QOSF Monthly Challenges</a></td>
    <td class="tg-sj11"><a href="#yao">Yao</a></td>
  </tr>
  <tr>
    <td class="tg-sj11"><a href="#quantify">Quantify</a></td>
    <td class="tg-sj11"><a href="#qqcs">QQCS</a></td>
    <td class="tg-sj11"><a href="#q">Q#</a></td>
    <td class="tg-sj11"></td>
  </tr>
</tbody>
</table>

---
## [Mitiq](https://github.com/unitaryfund/mitiq)

Mitiq is a Python toolkit for implementing error mitigation techniques on quantum computers.

Current quantum computers are noisy due to interactions with the environment, imperfect gate applications, state preparation and measurement errors, etc.
Error mitigation seeks to reduce these effects at the software level by compiling quantum programs in clever ways.
You can watch some videos about Mitiq on the [Unitary Fund YouTube channel](https://www.youtube.com/watch?v=5KDQtWzJcfw&list=PL-VMs2BCTI_lklMMfY4iMdETT19rgZe5o).


> General issues we are looking for help with during [unitaryHACK](https://github.com/unitaryfund/mitiq/labels/unitaryhack)

### Bounties

#### $100 each

- [Add tutorial example where mitiq makes a variational problem trainable](https://github.com/unitaryfund/mitiq/issues/529)

#### $75 each

- [Add type check to CI](https://github.com/unitaryfund/mitiq/issues/489)

#### $25 each

- [Add an XACC executor example and item to software list](https://github.com/unitaryfund/mitiq/issues/357)
- [Warn users when their programs are too short](https://github.com/unitaryfund/mitiq/issues/275)
- [Improve braket support](https://github.com/unitaryfund/mitiq/issues/679)

---

## [PennyLane](https://github.com/PennyLaneAI/pennylane)

PennyLane is a cross-platform Python library for differentiable programming of quantum computers.

Train a quantum computer the same way as a neural network.

### Bounties

#### $100 each
- [Create a quantum simulator in PyTorch](https://github.com/PennyLaneAI/pennylane/issues/1225)

---
## [Strawberry Fields](https://github.com/XanaduAI/strawberryfields)

Strawberry Fields is a full-stack Python library for designing, simulating, and optimizing continuous-variable quantum optical circuits.

### Bounties

#### $100 each
- [Add a hybrid Gaussian/non-Gaussian compiler that merges Gaussian gates](https://github.com/XanaduAI/strawberryfields/issues/574)

---
## [The Walrus](https://github.com/XanaduAI/thewalrus)

A library for the fast calculation of hafnians, Hermite polynomials, and Gaussian boson sampling.

### Bounties

#### $50 each
- [Improve the calculation of multidimensional hermite polynomials](https://github.com/XanaduAI/thewalrus/issues/214)

---
## [toqito](https://github.com/vprusso/toqito)

The toqito package is an open source Python library for studying various
objects in quantum information, namely, states, channels, and measurements.

Specifically, toqito focuses on providing numerical tools to study problems
pertaining to entanglement theory, nonlocal games, matrix analysis, and other
aspects of quantum information that are often associated with computer science.

> A complete list of issues can be found
[here](https://github.com/vprusso/toqito/issues)

### Bounties

#### $85 each

- [Implement feature for calculating the NPA hierarchy](https://github.com/vprusso/toqito/issues/5)
- [Implement feature for converting a binary constraint game to a nonlocal game](https://github.com/vprusso/toqito/issues/44)
- [Implement feature for determining whether an operator is block-positive](https://github.com/vprusso/toqito/issues/45)

---
## [SciRate](https://github.com/scirate/scirate)

[SciRate](http://scirate.com/) is an open source rating and commenting system
for arXiv preprints.  Papers are upvoted and discussed by the community, and
we sometimes play host to more in depth peer review.

> Check out some issues we are looking for help with ["help
wanted"](https://github.com/scirate/scirate/issues?q=is%3Aissue+is%3Aopen+label%3A%22help+wanted%22).

### Bounties

#### $125 each
- [Make a twitter/discord bot that posts the top papers each day](https://github.com/scirate/scirate/issues/430)
- [Build and deploy with nix](https://github.com/scirate/scirate/issues/429)

---
## [QuNetSim](https://github.com/tqsd/QuNetSim)

QuNetSim is a quantum network simulation framework. With it, one can develop protocols for quantum networks
such as QKD, quantum teleportation, anonymous transmission, and many more over custom network topologies.
You can watch the Quantum Software Talk on QuNetSim on [YouTube](https://www.youtube.com/watch?v=MmdRLYh1_mI&list=PL-VMs2BCTI_nnSQmBaccJ1CdQfw5cpHSp&index=5).

> The complete list of issues for QuNetSim are [here](https://github.com/tqsd/QuNetSim/issues).

### Bounties

#### $60 each

- [Develop a user interface for QuNetSim](https://github.com/tqsd/QuNetSim/issues/82)
- [Develop QKD protocols](https://github.com/tqsd/QuNetSim/issues/90)
- [Develop a more complex templating script](https://github.com/tqsd/QuNetSim/issues/52)
- [Develop an example of a second generation quantum repeater](https://github.com/tqsd/QuNetSim/issues/91)

---
## [Interlin-q](https://github.com/Interlin-q/Interlin-q)

Interlin-q is a simulation platform for simulating distributed quantum algorithms. The purpose
of Interlin-q is to be able to enter a monolithic quantum circuit and based on the distributed
architecture, automatically map the circuit and then simulate the control process to run the algorithm.

### Bounties
#### $250

- [Integrate pyQuirk with Interlin-q](https://github.com/Interlin-q/Interlin-q/issues/35)

---
## [QRAND](https://github.com/pedrorrivero/qrand)

QRAND is a smart quantum random number generator for arbitrary probability
distributions, which operates by providing a multiplatform NumPy adapter
interface (e.g. qiskit, cirq, qsharp). To boost the randomness production
speed it implements an efficient randomness retrieval strategy based on caching
and multithreading.

On top of that, it also allows the design and use of different platform-agnostic
quantum randomness generation protocols; as well as performing validation on the
results, according to a variety of NIST standards.

- [Unitary Hack sponsored issues](https://github.com/pedrorrivero/qrand/labels/unitaryhack)
- [Complete list of issues](https://github.com/pedrorrivero/qrand/issues)

### Bounties

#### $100 each
- [Cirq support](https://github.com/pedrorrivero/qrand/issues/1)
- [Q# support](https://github.com/pedrorrivero/qrand/issues/2)

#### $50 each
- [Entropy validation suite](https://github.com/pedrorrivero/qrand/issues/3)

---
## [Qrack](https://github.com/vm6502q/qrack)

Qrack is a GPU-accelerated HPC quantum computer simulator framework. The core library is
dependency-free C++11, with optional OpenCL and Boost headers. Hardware supports spans from desktop,
to mobile, to distributed clusters, and OS support includes Linux, Windows, Mac, Android, and iOS.
Qrack aims to optimize the performance of noiseless pure state simulations. To this end, it contains
many "layers" of functionality and novel optimization techniques.
You can watch the Quantum Software Talk on Qrack on [YouTube](https://www.youtube.com/watch?v=yxyqJDC4SUo&list=PL-VMs2BCTI_nnSQmBaccJ1CdQfw5cpHSp&index=2).

- A complete list of issues can be found
[here](https://github.com/vm6502q/qrack/issues)

### Bounties

#### $125

- [Feature: Cirq plugin](https://github.com/vm6502q/qrack/issues/678)

#### $125

- [Feature: Optional CUDA Support](https://github.com/vm6502q/qrack/issues/397)

---

## [QuTiP](https://github.com/qutip/qutip)

QuTiP is an open-source Python library for simulating the dynamics of closed
and open quantum systems, including quantum information processing and
quantum control.
You can watch the Quantum Software Talk on QuTiP on [YouTube](https://www.youtube.com/watch?v=2tF_4ZJAuYY&list=PL-VMs2BCTI_nnSQmBaccJ1CdQfw5cpHSp&index=3).
### Bounties

#### $25
- [Fix error raised by ffmpeg command from User Guide](https://github.com/qutip/qutip/issues/799)
- [Bloch sphere requires matplotlib >= 3.3](https://github.com/qutip/qutip/issues/1502)
- [Address deprecation warnings in Matplotlib 3.4](https://github.com/qutip/qutip/issues/1503)

#### $75
- [Address "malloc: Incorrect checksum" error in qutip.testing qt.run()](https://github.com/qutip/qutip/issues/1160)

TBD

---

## [Pulser](https://github.com/pasqal-io/Pulser)

Pulser is a Python library for programming neutral-atom quantum devices at the pulse level. The low-level nature of Pulser makes it a versatile framework for quantum control both in the digital and analog settings. The library also contains simulation routines for studying and exploring the outcome of pulse sequences for small systems.

> We recommend tackling [these issues](https://github.com/pasqal-io/Pulser/issues?q=is%3Aissue+is%3Aopen+label%3Aunitaryhack). If you want to start with a simple contribution, look also for a ["good first issue"](https://github.com/pasqal-io/Pulser/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22).

### Bounties

#### $100 each
- [Add Support for Simulation in XY Mode](https://github.com/pasqal-io/Pulser/issues/147)
- [Add type hints, and mypy CI tests](https://github.com/pasqal-io/Pulser/issues/16)

#### $50
- [Option to display pulses' areas and phases on a plot](https://github.com/pasqal-io/Pulser/issues/149)

---

## [QCOR](https://github.com/ornl-qci/qcor)

QCOR is a quantum-retargetable compiler platform providing language extensions for both C++
and Python that allows programmers to express quantum code as stand-alone kernel functions.
You can watch the Quantum Software Talk on QCOR and XACC on [YouTube](https://www.youtube.com/watch?v=GzslhEnHUHI&list=PL-VMs2BCTI_nnSQmBaccJ1CdQfw5cpHSp&index=2).
### Bounties

#### $25
- [API for command-line argument parsing](https://github.com/ornl-qci/qcor/issues/123)
- [Improved CMake Target Exporting and Downstream Quantum-Classical add_executable()](https://github.com/ornl-qci/qcor/issues/101)

#### $50
- [Quantum JIT Cache Manager](https://github.com/ornl-qci/qcor/issues/126)

#### $150
- [Python Wheels or Conda Binary](https://github.com/ornl-qci/qcor/issues/129)

---

## [XACC](https://github.com/eclipse/xacc)

XACC is a service-oriented, system-level software infrastructure in C++ promoting an
extensible API for the typical quantum-classical programming, compilation, and execution
workflow.
You can watch the Quantum Software Talk on QCOR and XAAC on [YouTube](https://www.youtube.com/watch?v=GzslhEnHUHI&list=PL-VMs2BCTI_nnSQmBaccJ1CdQfw5cpHSp&index=2).

### Bounties

#### $50
- [xacc::getAccelerator("ibm") automatic backend selection based on jobs in the queue](https://github.com/eclipse/xacc/issues/441)

#### $100
- [Flexible Instruction Simulation](https://github.com/eclipse/xacc/issues/442)
- [Implement 3-qubit decomposition](https://github.com/eclipse/xacc/issues/437)

---

## [Yao](https://github.com/QuantumBFS/Yao.jl)

Yao is an open source framework that aims to empower quantum information research with software tools in the [Julia programming language](http://julialang.org/).

### Bounties

#### $50
- [integration with PastaQ](https://github.com/QuantumBFS/Yao.jl/issues/280)

#### $100
- [integrate YaoBlocks with IBMQClient and OpenQASM](https://github.com/QuantumBFS/Yao.jl/issues/279)
- [webpage (tutorial/documentation/etc.) pipeline improvements](https://github.com/QuantumBFS/Yao.jl/issues/278)

---

## [QOSF Monthly Challenges](https://github.com/qosf/monthly-challenges/)

The Quantum Open Source Foundation (QOSF) Monthly Challenges aim to help participants hone their general quantum computing skills. These are open to everyone and welcome solo or team contributions. Solutions are peer-reviewed.

### Bounties

#### $25
- [Design a challenge!](https://github.com/qosf/monthly-challenges/issues/33)
- [Design a challenge!](https://github.com/qosf/monthly-challenges/issues/34)

---

## [QQCS](https://github.com/dde/qqcs)

QQCS is a simple linear notation for the simulation of quantum circuits.

> A list of issues can be found [here](https://github.com/dde/qqcs/issues)

### Bounties

#### $125 Each
- [Design new syntax to declare circuit lines to be divided into separate registers.](https://github.com/dde/qqcs/issues/15)
- [Add an adjoint operator (') the gate suffix syntax and to the interpreter.](https://github.com/dde/qqcs/issues/16)

#### $25
- [Add a command line switch to display sparse matrices with periods (.) replacing zero elements (0).](https://github.com/dde/qqcs/issues/18)

---

## [Quantify](https://gitlab.com/quantify-os)

Quantify is a python based data acquisition platform focused on Quantum Computing and solid-state physics experiments. It is built on top of [QCoDeS](https://qcodes.github.io/Qcodes/) and is a spiritual successor of [PycQED](https://github.com/DiCarloLab-Delft/PycQED_py3). Quantify currently consists of [quantify-core](https://gitlab.com/quantify-os/quantify-core) and [quantify-scheduler](https://gitlab.com/quantify-os/quantify-scheduler).

A list of other issues can be found here:
- [Quantify-core issues](https://gitlab.com/quantify-os/quantify-core/-/issues?label_name%5B%5D=unitaryhack)
- [Quantify-scheduler issues](https://gitlab.com/quantify-os/quantify-scheduler/-/issues?label_name%5B%5D=unitaryhack)

### Bounties

#### $25
- [Create an interactive data browser](https://gitlab.com/quantify-os/quantify-core/-/issues/204)
- [Save JSON schedule to harddisk](https://gitlab.com/quantify-os/quantify-scheduler/-/issues/2)

#### $50
- [Replace PyQT5 for realtime visualization](https://gitlab.com/quantify-os/quantify-core/-/issues/203)

#### $75
- [Support loops and classical logic in quantify-scheduler](https://gitlab.com/quantify-os/quantify-scheduler/-/issues/33)
- [Parser and generator for Qiskit, Cirq](https://gitlab.com/quantify-os/quantify-scheduler/-/issues/111)


## [Q#](https://github.com/microsoft/qsharp-language/tree/main/Specifications/Language)

We are working on adding support for compiling Q# to [QIR](https://github.com/microsoft/qsharp-compiler/tree/main/src/QsCompiler/QirGeneration) and executing it. QIR is a convention for how to represent quantum programs in [LLVM](https://github.com/llvm/). We aim to ultimately move the Q# compiler to be fully LLVM-based.

While the support and integration is not yet complete, we have set up an example for how to compile a Q# project to QIR and execute it on our full state simulator for early adventurers who are excited to give it a try!

For Unitary Hack, we have defined two tasks in particular to explore QIR:
      
### Bounties

#### $25 each
- Create an imaginative Q# program that is significantly different than any of our [samples](https://github.com/microsoft/Quantum), compile it to QIR, and execute it on our full state simulator. Create a PR adding the program to the [example](https://github.com/microsoft/qsharp-compiler/blob/unitaryhack/examples/QIR/Development/Program.qs) and post or attach the generated QIR to one of these GitHub issues: [example 1](https://github.com/microsoft/qsharp-compiler/issues/1028), [example 2](https://github.com/microsoft/qsharp-compiler/issues/1031), [example 3](https://github.com/microsoft/qsharp-compiler/issues/1032).


#### $50 each
- Find a Q# program that doesn't compile correctly into QIR or unexpectedly fails when executing the QIR on the full state simulator due to an issue with the generated QIR that hasn't been [filed](https://github.com/microsoft/qsharp-compiler/issues?q=is%3Aopen+is%3Aissue+label%3A%22area%3A+QIR%22) yet, and [file the issue](https://github.com/microsoft/qsharp-compiler/issues/new?assignees=&labels=bug%2C+area%3A+QIR&template=unitary_hack.md&title=[UnitaryHack]). The following GitHub issues contain more details: [issue 1](https://github.com/microsoft/qsharp-compiler/issues/1030), [issue 2](https://github.com/microsoft/qsharp-compiler/issues/1033), [issue 3](https://github.com/microsoft/qsharp-compiler/issues/1034)
