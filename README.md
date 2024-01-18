# MiniNAM fork with Python3 and ipmininet support

### What is MiniNAM?

MiniNAM is a network animator for visualizing real-time packet flows in Mininet. It is a GUI 
based tool written in Python Tkinter. It provides real-time animation of any network created 
by the Mininet emulator. It includes all the components required to initiate, visualize and modify 
Mininet network flows in real-time.

MiniNAM allows dynamic modification of preferences and packet filters: a user can view
selective flows with options to color code packets based on the source/destination node
and/or packet type. This establishes MiniNAM as a very powerful tool for debugging network
protocols or teaching, learning and understanding network concepts.

For more details, please refer to [MiniNAM project](https://github.com/uccmisl/MiniNAM) and [paper](http://ieeexplore.ieee.org/document/7899417/).

### Why this fork is created?

The last update of MiniNAM has been done in 2020. It does not support Python3, which is 
the mostly used Python version. Besides, it does not support [ipmininet](https://github.com/cnp3/ipmininet),
which is a Mininet extention to support emulation of complex IP networks (including IPv6, router configuration, etc.).
This fork aims at filling these two gaps.

### How does it work?

When MiniNAM is launched, it starts or loads the Mininet network instance. It then starts
a separate thread for the Tkinter GUI, and multiple threads to sniff packets on all the network 
interfaces in all network namespaces (one thread per network namespace) created by Mininet. 
For network namespace management, it relies on [pyroute2](https://github.com/crane-denny/python-pyroute2) library
that runs natively on Linux. Other platforms are not supported. 

The GUI displays network nodes and links. If an outcoming packet is sniffed at any interface, it is displayed over 
the relevant link in GUI after applying user-specific preferences and filters. The speed of packet flow can be decreased, 
if needed, for better visibility. As there can be more than one flow in the network at a particular time, MiniNAM tries 
to identify packets that belong to the same flow and adds those packets to a separate FIFO queue for each flow. However,
due to concurrency of multiple sniffing threads, it is important to add delays to all links in the network in order to 
preserve the packet order.

### How to start MiniNAM?

MiniNAM can be started using either using a topology defined in Mininet, or using a custom file.

* Start MiniNAM from CLI with a single command. E.g.

  `sudo python MiniNAM.py --topo tree,depth=2,fanout=2 --controller remote`

  To make MiniNAM easier for Mininet users, arguments of MiniNAM have been kept the same 
  as Mininet. This means that all the arguments that can be passed to `mn` utility can be
  passed to MiniNAM too. A list of these arguments can be seen in help:

  `sudo python MiniNAM.py --help`

* Start MiniNAM from CLI and pass custom files. E.g.

  `sudo python MiniNAM.py --custom <custom_file_name>`
  `sudo python MiniNAM.py --custom <custom_file_name> --topo <topo_name>`

  For example, to start a ipmininet topology with two hosts and a single router, the following command can be run:
  `sudo python MiniNAM.py --ipmininet --custom custom-ipmininet.py --topo mytopo`
