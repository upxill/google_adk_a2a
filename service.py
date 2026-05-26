import dotenv
dotenv.load_dotenv()

from google.adk.agents import Agent
from google.adk.a2a.utils.agent_to_a2a import to_a2a


# 1. Define your standard ADK tools/skills
def check_prime(nums: list[int]) -> dict:
    """Check if numbers in a list are prime using mathematical computation."""

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    return {str(num): is_prime(num) for num in nums}


# 2. Create your core ADK Agent
prime_agent = Agent(
    model="gemini-2.5-flash",
    name="check_prime_agent",
    description="An agent specialized in checking whether numbers are prime.",
    tools=[check_prime],
)

# 3. Convert it to an A2A-compatible application wrapper
a2a_app = to_a2a(prime_agent, port=8001)
