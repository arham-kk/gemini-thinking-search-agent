# Gemini Thinking Search Agent

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Overview

This project implements an agent that uses the Gemini 2.0 Flash Thinking model to answer user requests. It first assesses if the request needs external context using a standard Gemini 2.0 Flash Experimental model. If needed, it then retrieves the relevant information using the Google Search tool. The gathered context is then combined with the user request and passed to the Thinking model, which uses the combined context to formulate its response. This approach shows how you can create an agent that enhances its reasoning and analysis based on real world information.

## Key Features

*   **Contextual Reasoning**: The agent intelligently combines information pulled from search results with the original user request to generate insightful and accurate responses.
*   **Thinking Model**: Employs the Gemini 2.0 Flash Thinking Model to enhance reasoning and demonstrate the model's thought process.
*   **Dynamic Search Integration**: Uses Google Search as a tool to retrieve the most current and relevant information from the web.
*   **Asynchronous Operations**: Leverages `asyncio` for efficient and non-blocking API calls.
*   **Clear Output:** Displays the Thinking Model's thought process and its final response.
  
## Getting Started

### Prerequisites

*   Python 3.8 or higher
*   A Google AI Gemini API key (get one from [Google AI Studio](https://aistudio.google.com/app/apikey))

### Installation

1.  Clone this repository:

    ```bash
    git clone https://github.com/arham-kk/gemini-thinking-search-agent.git
    cd gemini-thinking-search-agent
    ```
2.  Install the required Python packages:

     ```bash
    pip install -r requirements.txt
    ```
     
3. **Set up your API key:**

   *    Add your Gemini API key to the `.env` file in the following format:

        ```
        GEMINI_API_KEY=your_api_key_here
        ```

### Running the Code

Execute the main Python file:

```bash
python agent.py
```

## License

This project is licensed under the MIT License

## Contributing

Contributions are welcome! Please feel free to submit issues or pull requests.
