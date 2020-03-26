# Introduction to Operating Systems Part 1
## Computer Systems Overview
### Stand-alone desktop computer
  * PC, Workstation: Computer system dedicated to mainly a single user
    * I/O devices
    * Can adopts OS technology developed for larger computer systems
  * May run several different types of OSs
***
### Client-Server Computing
  * Servers respond to requests by clients
    * Remote procedure call - also across machine boundaries via network
  * Client/Server are mainly software roles, but machines can be dedicated to one or few such roles
    * Compute server: Compute an action requested by the client
    * File server: interface to file system (read, create, update, delete)
***
### Parallel Systems
  * Multiprocessor systems with more than one CPU in close communication.
    * Today the default, even for desktop machines
  * Tightly coupled system (aka. shared-memory system, multiprocessor)
    * Processors share memory and a clock
    * Communication usually takes place through the shared memory
  * Advantages of parallel systems
    * Increased throughput
    * Economical
      * scalability performance
      * multiprocessor system vs multiple single-processor system
    * Increased reliability
      * graceful degradation
      * fail-soft systems
  * Symmetric multiprocessing (SMP)
    * One OS controls all processors and the shared memory
    * Many processes can run at once without performance deterioration
    * Most modern operating systems support SMP
  * Asymmetric multiprocessing
    * Each processor is assigned a specific task; a master processor schedules and allocates work to slave processors
    * More common in special-purpose systems (e.g. embedded MP-SoC, very common in smartphpnes)
***
### Hardware Multithreading, Multi-Core
  * Example: Intel Xeon Dualcore
    * 2 hardware threads per core
    * 2 cores per CPU chip
    * Appears to the OS like 4 standard processors
***
### Parallel Systems cont.
  * Multicomputer ("distributed memory parallel computer")
    * Several stand-alone servers, each one a SMP, loosely coupled by an interconnection network for internal data exchange
    * More scalable than shared-memory SMPs
    * But more cumbersome to program (message passing)
    * NSC Tetralith, LiU, 2018
  * Speed-up of a single application by parallel processing?
    * Requires parallelisation/restructuring the program using special parallel programming languages/systems
      * SMP: Multithreading -> TDDB68, TDDC78
      * HPC clusters: MPI (Message-Passing Interface) -> TDDC78
      * Data centres: Mapreduce/Hadoop -> 732A54/TDDE31
    * First used in High-Performance Computing for numerically intensive applications
    * ILLIAC 2, K-computer, Connection Machine, IBM Blue Gene, Tianhe-1
***
### Distributed Systems
  * Loosely coupled system
    * Networked stand-alone computers
      * each node has its own local memory
    * Nodes communicate with one another by message passing through various communications lines
    * Clustered systems are a special case, with stronger network
  * Distribute the computation among several physical computers
  * Advantages of distributed systems:
    * Resource sharing
    * Computation speed up
    * Adaptivity: load sharing (migration of jobs)
    * Fault tolerance
  * May be either client-server or peer-to-peer systems
***
  * Network Operating Systems
    * provides file sharing, e.g NFS - Network File System
    * provides communication scheme
    * runs independently from other computers on the network
  * Distributed Operating Systems
    * less autonomy between computers
    * gives the impression that there is a single operating system controlling the network
***
### Real-Time Systems
  * Often used as a control device in a dedicated application/environment, such as controlling scientific experiments, medical devices, avionics/automotive control, etc.
  * Well-defined tasks with fixed time constraints
  * Hard real-time systems
    * deadlines must be met under all circumstances
    * Conflicts with time-sharing systems, not supported bt general-purpose OSs
  * Soft real-time systems
    * Missed deadline -> degraded quality of service
    * Limited utility in industrial control or robotics
    * Useful in applications (multimedia, virtual reality) requiring advanced OS features
    * Certain general-purpose OSs can implement soft real-time systems with the use of priorities
***
### Handheld Systems
  * Personal Digital Assistants (PDAs), tablets etc
  * Cellular telephones, smartphones
  * Issues:
    * Small display screens
    * Limited battery lifetime
***
## Before talking about OS
  * early operating systems were implemented in assembly language (and some low-level parts of modern OS still are)
    * Necessary for direct access to hardware devices
  * Since the 1970s the dominating language for system programming is C
***
## Java vs. C
### Java
  * For application programming only
  * Design goals:
    * Programmer productivity
    * Safety
    * Hardware completely hidden
  * Comfortable
    * E.g. automatic memory management
  * Protection (to some degree)
    * E.g. array bound checking
  * Slow
  * Time-unpredictable
***
### C
  * For system programming mainly
  * Design goals:
    * Direct control of hardware
    * High performance / real-time
    * Minimalistic design
  * Less comfortable
  * Little protection
  * "low-level"
  * "language for the adult programmer"
***
### A short history of C
  * C was developed in the early 1970's by Dennis Ritchie at Bell Labs
    * Objective: Structured but flexible programming language e.g. for writing device drivers or operating systems
    * Used for implementing the Unix OS
    * Book 1978 by Brian Kernighan and Dennis Ritchie ("K&R-C")
  * "ANSI-C" 1989 standard by ANSI
    * The C standard for many programmers and compilers
    * Became the basis for the standard C++
    * Java borrowed much of its syntax
    * The GNU C compiler (gcc) implemented a superset ("GNU-C")
***
## How to build and execute programs on a real computer
  * Diagram of compilation workflow on slides pages 29-35
***
## OS Basics
### Computer System Structure
#### "Like a layer in an onion", can be divided into 4 components
  * Hardware provides basic computing resources
    * CPU, memory, I/O devices
  * Operating system controls and coordinates use of hardware among various applications and users
  * Application programs define the ways in which the system resources are used to solve the computing problems of users
  * Users, people, machines, other computers
***
### Operating System Definition
  * OS is a resource allocator
    * Manages all resources of a computer system
    * Decides between conflicting requests for efficient and fair resource use
  * OS is a control program
    * Controls execution of programs to prevent errors and improper use of the computer
  * No universally accepted definition
  * "The one running at all times on the computer" is called the kernel.
    * Everything else is either a system program (ships with the operating system) or an application program
***
### Where are OSs found?
  * All over the place.
