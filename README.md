# RAG-finetuning

# RAG (Recurrent Autoregressive Generator) Project

## Overview
The RAG project is a software tool developed to generate didactic mini-scenarios for educational games. It employs recurrent autoregressive models to create context-specific scenarios based on provided didactic mechanics. This tool aims to assist educators and game developers in designing engaging and educational gameplay experiences.


*  [RAG with fin tuning](https://github.com/Yema7D/RAG-finetuning.git).
*  ![chat](https://github.com/Yema7D/RAG-finetuning/blob/main/img/1game.png)
*  *  ![chat](https://github.com/Yema7D/RAG-finetuning/blob/main/img/2game.png)

## Features
- **Mini-scenario Generation:** Utilizes recurrent autoregressive models to generate context-specific mini-scenarios.
- **Contextual Relevance:** Ensures that generated mini-scenarios are directly related to the provided didactic mechanics and context.
- **Customization:** Allows users to specify the number of mini-scenarios to generate and the language of the output.
- **Example-Based Learning:** Provides examples of well-formulated mini-scenarios to guide users in creating contextually relevant scenarios.

## Usage
To generate didactic mini-scenarios, follow these steps:
1. Clone this repository to your local machine.
2. Install the required dependencies specified in the `requirements.txt` file.
3. deployment app on docker
## Getting started
```
git clone https://github.com/Yema7D/RAG-finetuning.git
cd RAG-finetuning
```
* Create a virtual environment for this project and install dependencies
```
python3 -m venv .env
```

* Activate the virtual environment
```
source .env/bin/activate
```

* Install the dependencies
```
pip install -r requirements.txt
```
* Run the application

```bash
uvicorn main:app
```

* install images and run containers on docker 
```
docker-compose up
```


