# Basic 3 node intent, to create and parse.

SRC node : source of data. Represented by a REST API which gives data (in a predetermined format). This dummy data is represented by a dummy 3Vs sample data *(
input/metadata.csv)* The URL is used in the ansible enviroment to download the dummy data from a demo server using a GET  request.
Model node: the URL to download the AI/ML Model. POST command to download the model. The url is used in the ansible environment to download a demo h5 model. *(input/model.h5)* It depends on the source node and is hosted on the workstation node.
SINK node: sink for applying inference.it depends on the model node. It is represented by a REST API which will set values (UE UP throughput and UE DOWN throughput values).  


To run the example, make sure the xopera orchestrator is installed
1. 	Clone the repo https://github.com/gblessed/Intent-Driven-Closed-Loops-.git
2.	Install xopera [here](https://github.com/xlab-si/xopera-opera), docker for ubuntu [here](https://docs.docker.com/engine/install/ubuntu/) and docker module in python3 [pip install docker]
3. Change all directory paths in the playbooks folder to create.yaml, create-model-node.yaml and create-sink-node.yaml files to the correct paths in your storage location. ![image](https://user-images.githubusercontent.com/53085242/139949917-33738cab-e6b4-46ca-ab77-6fdb17d088a3.png)
4. Login as root user [sudo -s]
5.  Activate the virtual enviroment where the xopera is installed
6.  Deploy service template: <code>opera deploy service.yaml -c </code>. ![image](https://user-images.githubusercontent.com/53085242/139952222-5f69b66d-eaee-4d0e-a943-ca51081f27af.png)
8. To view outputs: <code>opera outputs</code> [See output here Output](https://drive.google.com/file/d/1n8_WjGckx6LRncqKeWghUKhfAE75qfw6/view?usp=sharing) After deploying, three json files (source_api.json, model_api.json and sink_api.json)  containing the REST APIs. Also, three docker containers are created from each node, which uses the API provided by each node.
9. To undeploy all nodes: <code>opera undeploy</code>

Note:
  A video guide is available in the Team_winest_demo_ITU.rar [here](https://github.com/gblessed/Intent-Driven-Closed-Loops-/blob/main/basic_three_node/Team_winest_demo_ITU.rar)
  Ensure that all the directory paths in the create, create_model_node and create_sink_node are set correctly. 
  Ensure that docker is installed [link](https://docs.docker.com/engine/install/ubuntu/)
  
  
  

