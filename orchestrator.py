import dotenv

dotenv.load_dotenv()

from google.adk.agents import Agent
from google.adk.agents.remote_a2a_agent import RemoteA2aAgent
from google.genai import types
from google.adk.runners import InMemoryRunner
from google.adk.utils._debug_output import print_event

# 1. Register the remote agent via its A2A agent card endpoint
remote_prime_agent = RemoteA2aAgent(
    name="remote_prime_checker",
    description="Delegates prime checking requests to an external math service.",
    agent_card="http://localhost:8001/.well-known/agent-card.json",
)

# 2. Use the standard config pattern or register via the tools/agents array
# If top-level keys throw extra_forbidden errors, pass it using the explicit config pattern:
root_agent = Agent(
    model="gemini-2.5-flash",
    name="orchestrator_agent",
    # If using direct constructor arguments:
    instruction="You are an orchestrator. If a user asks to analyze numbers for primality, delegate that task entirely to the remote_prime_checker agent.",
    sub_agents=[
        remote_prime_agent
    ],  # Remote agents can be treated directly as sub_agents
)

# 3. Execute a turn
if __name__ == "__main__":
    runner = InMemoryRunner(agent=root_agent)
    runner.auto_create_session = True

    events = runner.run(
        user_id="user_1",
        session_id="session_1",
        new_message=types.Content(
            role="user",
            parts=[
                types.Part(text="Can you tell me if 17, 24, and 97 are prime numbers?")
            ],
        ),
    )

    for event in events:
        print_event(event, verbose=True)
