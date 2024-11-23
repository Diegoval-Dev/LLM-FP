import streamlit as st
from typing import Any
from dotenv import load_dotenv
from langchain import hub
from langchain_core.tools import Tool
from langchain_openai import ChatOpenAI
from langchain.agents import create_react_agent, AgentExecutor
from langchain_experimental.tools import PythonREPLTool
from langchain_experimental.agents import create_csv_agent


load_dotenv()

def main():
    
    st.set_page_config(page_title="AI Super Agent", layout="centered")
    st.title("AI Super Agent")

    
    instructions = """You are an agent designed to write and execute Python code to answer questions.
    You have access to a python REPL, which you can use to execute python code.
    You have qrcode package installed
    If you get an error, debug your code and try again.
    Only use the output of your code to answer the question.
    You might know the answer without running any code, but you should still run the code to get the answer.
    If it does not seem like you can write code to answer the question, just return "I don't know" as the answer.
    """
    
    base_prompt = hub.pull("langchain-ai/react-agent-template")
    prompt = base_prompt.partial(instructions=instructions)

    
    tools = [PythonREPLTool()]
    python_agent = create_react_agent(
        prompt=prompt,
        llm=ChatOpenAI(temperature=0, model="gpt-4-turbo"),
        tools=tools,
    )
    python_agent_executor = AgentExecutor(agent=python_agent, tools=tools, verbose=True)

    
    btc_csv_agent_executor: AgentExecutor = create_csv_agent(
        llm=ChatOpenAI(temperature=0, model="gpt-4"),
        path="btcusd_1-min_data.csv",
        verbose=True,
        allow_dangerous_code=True,
    )

    fortnite_csv_agent_executor: AgentExecutor = create_csv_agent(
        llm=ChatOpenAI(temperature=0, model="gpt-4"),
        path="Fortnite Statistics.csv",
        verbose=True,
        allow_dangerous_code=True,
    )

    gym_csv_agent_executor: AgentExecutor = create_csv_agent(
        llm=ChatOpenAI(temperature=0, model="gpt-4"),
        path="megaGymDataset.csv",
        verbose=True,
        allow_dangerous_code=True,
    )

    pricesSP500_csv_agent_executor: AgentExecutor = create_csv_agent(
        llm=ChatOpenAI(temperature=0, model="gpt-4"),
        path="SP500_test.csv",
        verbose=True,
        allow_dangerous_code=True,
    )

    
    def python_agent_executor_wrapper(original_prompt: str) -> dict[str, Any]:
        return python_agent_executor.invoke({"input": original_prompt})

    
    tools = [
        Tool(
            name="Python REPL",
            func=python_agent_executor_wrapper,
            description="Executes Python code to answer questions."
        ),
        Tool(
            name="BTC CSV Agent",
            func=btc_csv_agent_executor.invoke,
            description="Analyzes BTC/USD data from a CSV file."
        ),
        Tool(
            name="Fortnite CSV Agent",
            func=fortnite_csv_agent_executor.invoke,
            description="Analyzes Fortnite statistics from a CSV file."
        ),
        Tool(
            name="Gym CSV Agent",
            func=gym_csv_agent_executor.invoke,
            description="Analyzes gym dataset from a CSV file."
        ),
        Tool(
            name="SP500 Prices CSV Agent",
            func=pricesSP500_csv_agent_executor.invoke,
            description="Analyzes S&P 500 prices from a CSV file."
        )
    ]

    
    prompt = base_prompt.partial(instructions="")
    group_agent = create_react_agent(
        prompt=prompt,
        llm=ChatOpenAI(temperature=0, model="gpt-4-turbo"),
        tools=tools,
    )
    grand_agent_executor = AgentExecutor(agent=group_agent, tools=tools, verbose=True)

    
    st.subheader("Selecciona una solicitud de trabajo para el agente Python:")
    options = [
        "Generar y guardar 3 códigos QR que apunten a google.com",
        "Haz un Fizz Buzz del 1 al 100",
        "Imprimir el siguiente JSON explicando cada campo en Python: {'name': 'John', 'age': 30, 'city': 'New York'}"
    ]
    selected_option = st.selectbox("Opciones de trabajo", options)

    
    if st.button("Ejecutar solicitud de trabajo"):
        if selected_option == options[0]:
            st.write("Ejecutando: Generar y guardar 3 códigos QR que apunten a google.com...")
            result = grand_agent_executor.invoke(
                input={
                    "input": "Generate and save in current working directory 3 qrcode that point to google.com?"
                }
            )
            st.write(result)
        elif selected_option == options[1]:
            st.write("Ejecutando: Haz un Fizz Buzz del 1 al 100...")
            result = grand_agent_executor.invoke(
                input={
                    "input": "Write a Python program that prints Fizz Buzz from 1 to 100."
                }
            )
            st.write(result)
        elif selected_option == options[2]:
            st.write("Ejecutando: Imprimir JSON...")
            result = grand_agent_executor.invoke(
                input={
                    "input": "Make a function for print each camp of the JSON: {'name': 'John', 'age': 30, 'city': 'New York'}"
                }
            )
            st.write(result)

    
    st.subheader("Realiza una pregunta o solicitud para el agente:")
    user_input = st.text_input("Escribe tu pregunta o solicitud aquí")

    
    if st.button("Ejecutar pregunta"):
        if user_input:
            st.write("Procesando la solicitud...")
            result = grand_agent_executor.invoke(input={"input": user_input})
            st.write(result)
        else:
            st.write("Por favor, escribe una pregunta o solicitud antes de presionar el botón.")

if __name__ == "__main__":
    main()
    
    
# BTC CSV Agent:

# "¿Cuál fue el precio máximo del BTC/USD registrado en el CSV?"
# "¿Cuál es la variación media del precio de BTC/USD durante un periodo de 24 horas?"
# Fortnite CSV Agent:

# "¿Cual es la distancia promedio recorrida en el dataset de Fortnite?"
# "¿Cuál es el promedio de muertes (kills) por partida en las estadísticas de Fortnite?"
# Gym CSV Agent:

# "Hazme una rutina de tricep"
# "¿Cuál es el mejor ejercicio para pecho?"
# SP500 Prices CSV Agent:

# "¿Cuál fue el valor más alto del S&P 500 en el último mes según los datos del CSV?"
# "¿Cuál es la tendencia de los precios del S&P 500 durante los últimos 7 días?"
