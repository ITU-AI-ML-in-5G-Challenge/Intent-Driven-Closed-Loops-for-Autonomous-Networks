# Basic 4 node intent, to create and parse.

SRC node : source of data. Represented by a REST API which gives data (in a predetermined format). This dummy data is represented by a dummy 3V sample data *(
input/metadata.csv)* The URL is used in the ansible enviroment to download the dummy data from a demo server using a GET  request.
Model node: the URL to download the AI/ML Model. POST command to download the model. The url is used in the ansible environment to download a demo h5 model. *(input/model.h5)* It depends on the source node and is hosted on the workstation node.
SINK node: sink for applying inference.it depends on the model node. It is represented by a REST API which will set values (UE UP throughput and UE DOWN throughput values).  

The demo server is shown in the server.py

To run the example, make sure the xopera orchestrator is installed
1. <code>python3 server.py</code>
2.  Deploy service node: <code>opera deploy service.yaml</code> . [See output here Output](https://drive.google.com/file/d/1T5ZpezrRbYrVNXDSysYlGHZe3hllKev0/view?usp=sharing)
3. To view outputs: <code>opera outputs</code> [See output here Output](https://drive.google.com/file/d/1n8_WjGckx6LRncqKeWghUKhfAE75qfw6/view?usp=sharing)
4. To undeploy all nodes: <code>opera undeploy</code>

