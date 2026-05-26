## Google ADK Multi-Agent System (A2A)

This project implements a decentralized multi-agent system using the Google Agent Development Kit (ADK) and the Agent-to-Agent (A2A) protocol. It demonstrates how to expose a specialized tool as an independent microservice and consume it remotely using a central orchestrator agent.


## Architecture 
FlowThe system routes incoming user requests through an orchestration tier down to a network-isolated capability layer.
flowchart TD

    A[User Request<br/>e.g., "Are 17, 24, 97 prime?"] --> B[Orchestrator Agent]

    B -->|Detects prime-checking intent| C[RemoteA2aAgent Wrapper]

    C -->|Calls via HTTP| D[Remote Prime Checker A2A Service]

    D -->|Runs check_prime tool| E[Prime Results<br/>{17: true, 24: false, 97: true}]

    E --> F[Orchestrator Agent Formats Response]

    F --> G[Final Answer to User]

## Agent Server 
Start the remote prime-checking agent:
uv run uvicorn agent_api:a2a_app --host localhost --port 8001

This exposes:
http://localhost:8001/.well-known/agent-card.json


 ## Agent Consumer
Run the orchestrator agent

python agent_consume.py