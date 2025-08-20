from strands import Agent
import json



agent = Agent()

def call_agent(event, context):
# Ask the agent a question
    resp = agent("Tell me about agentic AI")
    return {
        'statusCode': 200,
        'body': json.dumps(resp.message)
    }