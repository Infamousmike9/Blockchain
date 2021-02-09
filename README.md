# Blockchain
Creating, Mining and Transacting on a Custom PoA Blockchain:

In this repository I will show you what is required in order to create a blockchain, make it mine and send a transaction using the Proof of Authority blockchain consensus.
Before we being we have install the following:
- [GoEthereum Tools](https://geth.ethereum.org/) version 1.9.7 (Also known as Geth Tools)

This installation package contains several files but we will only focus on geth and puppeth to create our blockchain and network. Go Ethereum is a command line interface for running Ethereum node implemented in Go Language. Using Geth you can join the Ethereum network, transfer ETH and mine. 

<ins>**Getting Started:**

Once the tools are downloaded we extracted them into a file name Blockchain_Tools for ease of access to "cd" via terminal. The first thing we do is create our nodes. When create a blockchain that you will mine you must create two or more nodes. In this case we are creating two local nodes. We will name then respectively Node1 and Node2. Nodes are computers in a network in this case these are local nodes since these nodes are running off the same computer for purposes of a test network for mining. In blockchain nodes are used for verifying transactions and mining blocks of a blockchain. 

The following picture shows the required code for creating each Node:
- ./geth --datadir node1 account new

<img src = Screenshots/Created_Node1_and_Node2.PNG>

As you can see from the picture, each node contains a public address and a secret key file also known as a UTC keystore file (We will discuss this later) and they are protected by a password of your choice. You can use the same password for all your nodes. The public address will be the address to use to send and receive cryptocurrency. For best practices I saved the password for the nodes in a text file named password.txt.

As you can see when running this code we are in our Blockchain_Tools directory in terminal. we run ./geth to call the geth executable file within the folder to create a new directory named Node1 that is a new account. Within this Node1 folder that is created there will be a keystore file for the UTC data and a geth folder that will hold transaction logs, chain data and other nodekey information. This will be the same for Node2.

<ins>**Puppeth:**

Puppeth is another executable file held in the Blockchain-Tools folder and like geth we call it by typing ./puppeth in terminal within the Blockchain_tools folder directory. In this case we are using puppeth to create our custom Ethereum test network with a Genesis block. For the case of this project i decided to name the network HWNET2021. 

A genesis block is the first block in the blockchain. This block unlike future generated blocks have no previous history and traditionally may contain some type of hidden data. For example Bitcoin's Genesis block contains a hidden message that states "The Times 03/Jan/2009 Chancellor on brink of second bailout for banks." In our case there is no hidden message. 

When creating our network HWNET2021 I used the Clique - Proof of authority consensus engine. This engine, although unreliable for security reasons is the best for running a test network due to its speed. There are many types of consensus engines to use when creating a blockchain network, however, there are three very popular ones. Proof of Work, which is extremely expensive due to the amount of power required to calculate complex equations when verifying and mining blocks with the advantage of security as it requires the good and bad actors to have similar system power. Proof of Authority which gives a small amount of nodes the power to validate transactions and update the distributed ledger with the advantage of speed. Proof of stake, which states that the node with the largest amount of coins can mine and validate transactions with a disadvantage of possible centralization of control over the blockchain.

After selecting the consensus algorithm I decided that each block should take one second. Both nodes were allowed to seal or create blocks and mine. I also decided not to prefund any of my nodes. Finally selected a network/chain ID of 2018. The network ID is a random number that I chose, I will use it later to connect our node to a crypto currency wallet. 

<ins>**Finalizing Genesis**:



