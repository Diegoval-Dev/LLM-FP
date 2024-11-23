# AI Agent Interface with Streamlit

This project provides an AI-powered interface using Streamlit that integrates various AI agents to execute Python code and analyze CSV files. The AI agents can answer questions, generate code, and process data from CSV files.

## Features

- **Python Code Execution**: The interface includes an AI agent capable of executing Python code using a REPL environment.
- **Data Analysis with CSV Agents**: Multiple CSV agents are implemented to analyze data from different datasets, such as Bitcoin price data, Fortnite statistics, gym datasets, and S&P 500 prices.
- **Interactive UI**: Users can interact with the agents through an easy-to-use interface built with Streamlit, allowing them to make requests and see the results in real-time.
- **Customizable Options**: The interface provides pre-defined tasks for the agent to perform, as well as a text input field for custom requests.

## Setup Instructions

### Clone the Repository

Clone this repository to your local machine:

```bash
git clone <https://github.com/Diegoval-Dev/LLM-FP>
cd <LLM-FP>
```

### Install Dependencies

Make sure to have Python installed, then install the required packages:

```bash
pip install -r requirements.txt
```

### Set Up Environment Variables

Create a `.env` file in the root directory and add your OpenAI API key:

```plaintext
OPENAI_API_KEY=your_openai_api_key_here
```

### Run the Application

Launch the Streamlit application:

```bash
streamlit run main.py
```

## How to Use

### Select a Task for the Python Agent

Choose a predefined task from the dropdown menu:

- Generate and save 3 QR codes that point to google.com.
- Execute a Fizz Buzz program from 1 to 100.
- Convert a JSON to a Python dictionary.

### Execute the Selected Task

Click the "Ejecutar solicitud de trabajo" button to execute the selected task. The result will be displayed below the button.

### Ask a Custom Question

Enter a custom question or request in the text field and click "Ejecutar pregunta". The AI agent will process the input and return a response.

## CSV Agents

The interface includes agents that can analyze the following CSV datasets:

- **BTC/USD Data (btcusd_1-min_data.csv)**: Provides analysis on Bitcoin price data.
- **Fortnite Statistics (Fortnite Statistics.csv)**: Analyzes data related to Fortnite player statistics.
- **Gym Dataset (megaGymDataset.csv)**: Provides insights into gym attendance and membership information.
- **S&P 500 Prices (prices.csv)**: Analyzes historical data of S&P 500 prices.

### Example Questions for CSV Agents

Here are some example questions you can ask about the CSV files:

- **BTC CSV Agent**: "¿Cuál fue el precio máximo del BTC/USD registrado en el CSV?"
- **Fortnite CSV Agent**: "¿Cuántos jugadores tuvieron más de 10 victorias en el dataset de Fortnite?"
- **Gym CSV Agent**: "¿Cuál es la edad promedio de los miembros del gimnasio en el dataset?"
- **SP500 Prices CSV Agent**: "¿Cuál fue el valor más alto del S&P 500 en el último mes según los datos del CSV?"

## Technologies Used

- **Streamlit**: Used for building the user interface.
- **Langchain**: Provides the framework for integrating various agents and tools.
- **OpenAI GPT-4**: Used as the core language model to understand and execute tasks.
- **Python**: The primary programming language used for creating and managing the agents.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

## Acknowledgments

- OpenAI for providing the GPT-4 model used in this project.
- Streamlit for making it easy to build interactive UIs.

## video

