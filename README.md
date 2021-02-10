# Blockchain
<p align="center">
<ins><b>Creating, Mining and Transacting on a Custom PoA Blockchain:</b><br><ins>
</p>

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

After selecting the consensus algorithm I decided that each block should take one second. Both nodes were allowed to seal or create blocks and mine. I also decided not to pre-fund any of my nodes. Finally, selected a network/chain ID of 2018. The network ID is a random number that I chose, I will use it later to connect our node to a crypto currency wallet. 

Code used to initiate puppeth:
- ./puppeth 

<img src =Screenshots/Created_New_Genesis_puppeth.PNG>

<ins>**Finalizing Genesis**:

As previously stated the genesis block is the first block in the blockchain. This genesis block will have the name of our network and is saved in a JSON file. When a exporting the genesis file during proof of Work four files are created a basic JSON file, an aleth JSON file, a harmony JSON file and a parity JSON file all under the name of the netowrk created. In this case since we are using the proof of authority consensus only two files were created, the basic network name JSON file hwnet2021.json and the harmony file hwnet2021-harmony.json. From what I have been able to research briefly Harmony is a fast and secure blockchain for decentralized applications. However, we will only be focusing on the main basic hwnet2021.json that holds our necessary information. 

<img src = Screenshots/Exported_genesis_to_json.PNG> 

<ins>**Initializing Nodes:**

After the nodes and genesis are created the next step is to initialize the nodes. What I am doing here is using Geth to obtain my genesis json file (hwnet2021.json) located in the hwnet2021 folder directory and using that genesis data to create the first block within that node. Since we have two nodes we have to initialize each node separately specifying the node number. You can see when you are successful initializing your node when you see the chaindata hash with a hash key and the message "Successfully wrote genesis state."

<img src = Screenshots/Initiated_nodes1and2.PNG>

<ins>**Mining your nodes:**

After going through the very tedious process of creating your nodes, creating your genesis and initializing your nodes we are now at the very last but important step in creating your blockchain, Mining. Mining is the process of solving complex mathematical equations to validate transactions to create more blocks that contain validated transactions to a block chain. In this case, both of our nodes will be mining. The code required for mining is somewhat intricate and requires a specific set of what are known as flags that are required to do certain things which will be explained below.

The flags required are the following: 
- ./geth
- --datadir node#
- --unlock
- --rpc
- --mine
- --minerthreads #
- --password
- --allow-insecure-unlock
- --ipcdisable
- --bootnodes

**./geth:**

As previous state geth is one of the executable files contained in the Go Ethereum tools package. Geth is a very powerful blockchain tool built with the Google Go language. It is used to create software that runs on the Ethereum Virtual Machine.

**--datadir node #:**

This flag is used to guide the executable file being used to find a file. Or better said datadir defines the path to a directory. In this case datadir is telling geth to use the node1 directory located in the Blockchain-Tools folder.

**--unlock:**

This flag is used to unlock an account in geth. When using this flag you must specify the account you want to unlock. In this case, we unlocked the node1 address with the first two characters usually starting in 0x. 

**--rpc:**

This flag is known as the Remote Procedure Call. Primarily seen in distributed computing (nodes) in which messages are encoded in JSON format. RPC can be written in several different languages to be used in different aspects of computing and networking. RPC is a concept in computer science that enables one computer to call a procedure of another computer. The origins of RPC date all the way back to the 1970s when researchers such as [Richard Shantz](https://ds.bbn.technology/people/schantz/) and [Bruce Jay Nelson](https://en.wikipedia.org/wiki/Bruce_Jay_Nelson) were trying to understand how distributed applications could effectively communicate on the predecessors to today’s internet. Blockchain architects focus on using RPC for a more direct connection to the blockchain which is simple and well understood means of client/server communication.

**--mine:**

This flag is the command that allows your node to mine the blocks. 

**--minerthreads #:**

This flag is a command that allows your node to mine specifying the amount of threads you would like to use from you CPU. Each CPU has a limited amount of threads depending on the amount of threads available on your CPU you can increase the number of threads to be used for mining. The higher the number the more power you are allocating to your miner and the faster you will mine. (We will not be discussing CPUs here :-)). In my case, out of curiosity, I chose to mine with two threads.

**--password:**

This flag is used to automagically enter the password of your node while mining. After creating my node I created a text file saved as password.txt that holds my node's password. This gives me the ability of not having to enter my password manually. 

**--allow-insecure-unlock:**

This flag allows you to unlock access to a node with geth via HTTP protocol. Without it an error is received "account unlock with HTTP access is forbidden". In order to avoid this error this flag must be used as we are running the network and nodes in an HTTP protocol.

**--ipcdisable:**

This flag was only used on our node2. It is only required if you have a windows based PC. It removes certain security measure present in Windows that does not allow a node to mine. 

**--bootnodes:**

This final flag is the most important. This flag is an application that holds the address to your genesis node and tells your second node to connect with it, although using a different port. In our case we used port 30303 and 30304 respectively. 

The codes required for mining are as follows:
- ./geth --datadir node1 --unlock 0daf09b88cA3CbF31059653D4DA6b998beBb7f63 --rpc --mine --minerthreads 2 --password password.txt --allow-insecure-unlock

- ./geth --datadir node2 --mine --unlock c5E262E8F01965ee7c4D22cf93E398b1C81D62E8 --password password.txt --port 30304 --allow-insecure-unlock --bootnodes 
enode://35fe96bf4ef0c734803917197408aa6c24573615bdd185aed4a73fe86d590e410359522bd4d4d4abfc9b2370e8c556a659ee5335957bcc57c52929a02087ce6a@127.0.0.1:30303 --ipcdisable

Notice when mining node2 we are adding an enode address to bootnodes. As previously stated enode is the address of the first node. In node2 via bootnodes we are directing the node to connect to that specific node one address. 

<img src = Screenshots/Mining_NODE1.PNG>

<ins>**How do you know you are mining?:**

Once your miner has started you will see several items automatically being added to the screen. Mined potential block and commiting new mining work. Both nodes will be working/mining at the same time. The screen will reflect the number of blocks mined as well has the has key for each block created. 

<img src = Screenshots/Mining_NODE1_and_NODE2.PNG>

**Conclusion:**

In the last step of my blockchain project we connect our node1 to a cryptocurrency wallet in order to check our balance and send a transaction. 

We connect our node1 to the wallet Mycrypto using what is called a keystore file. When your node is created the file holding your node contains a keystore file that begins with UTC this file contains a private key of your node address. As you can see from the below picture once I entered my node1 keystore file I was able to see a nice balance in my wallet.

<img src = Screenshots/Node_1_MyCrypto.PNG>

After connecting the node to my wallet I sent a large amoutn of ethereum to my node2 address directly from the wallet. 

<img src = Screenshots/SendingETH_NODE1_to_NODE2.PNG>

The transaction was pending for sometime as you can se below it warned it can take up to 3 hours to be mined and confirmed. Luckily it did not take that long.

<img src = Screenshots/SentETH_waiting_to_mine.PNG>

Finally, the transaction was successful. 

<img src = Screenshots/Successful_Sent.PNG>
<img src = Screenshots/TXStatus_Check.PNG>

We created our blockchain, initialized it, mined and transacted. 


### I got curious:

So I attempted to use python to check my node balance and send ethereum to my node2. The issue here is i did nto have time to hide my private key:







