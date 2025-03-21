import os
from dotenv import load_dotenv
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")

provider = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai"
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=provider,
)

agent = Agent(
    name="Greeting Agent",
    instructions=(
        "You are a Greeting Agent. Your task is to greet the user with a friendly message. "
        "If someone says hi, you must reply with 'Salam from Bisma Yousuf'. "
        "If someone says bye, you must reply with 'Allah Hafiz from Bisma Yousuf'. "
        "If someone asks anything else, respond with 'Bisma Yousuf is here just for greeting, nothing else sorry.'"
    ),
    model=model 
)

user_question = input("Enter your question: ")

result = Runner.run_sync(agent, user_question)
print(result.final_output)
