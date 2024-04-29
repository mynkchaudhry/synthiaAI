## SYNTHIA AI

Demo:https://synthiaai.streamlit.app/

```markdown
# SYNTHIA Chatbot

SYNTHIA is a simple chatbot application built using Streamlit, Groq API, and other libraries. It allows users to interact with different language models and customize conversational memory length.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/mynkchaudhry/synthiaAI.git
   ```

2. Navigate to the project directory:
   ```bash
   cd synthiaAI
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Set up environment variables:
   - Create a `.env` file in the root directory.
   - Add your Groq API key to the `.env` file:
     ```
     GROQ_API_KEY=your_api_key_here
     ```

2. Run the Streamlit app:
   ```bash
   streamlit run synthiaAI.py
   ```

3. Interact with the chatbot:
   - Choose a language model and conversational memory length from the sidebar.
   - Enter your question in the text area and click "Generate Response" to receive a response from the chatbot.
   - Use "New Chat" to start a new conversation and "Show Chat History" to view past interactions.

## Customization Options

- **Language Model:** Select from available models like `mixtral-8x7b-32768`, `gemma-7b-it`, `llama3-70b-8192`, or `llama3-8b-8192`.
- **Conversational Memory Length:** Adjust the length of the chatbot's memory from 1 to 1000.


## Preview

![SYNTHIA Chatbot Screenshot](https://github.com/mynkchaudhry/synthiaAI/blob/main/Demo.png)

## Credits

- Icons: [Iconscout](https://iconscout.com/)
- Background Image: [Pixabay](https://pixabay.com/)
- Streamlit: [Streamlit](https://www.streamlit.io/)
- Groq API: [Groq](https://www.groq.ai/)
