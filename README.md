# Ice Breaker

Ice Breaker is an AI-powered web application that generates personalized conversation starters and professional summaries for any LinkedIn user, given their name. It leverages modern agentic AI techniques using LangChain, LLMs, and third-party APIs to automate LinkedIn profile lookup and summarization.

---

## Features
- **LinkedIn Profile Lookup:**
  - Automatically finds a person's LinkedIn profile URL based on their name using a custom agent and search tools.
- **Profile Scraping:**
  - Retrieves public profile data (mocked or via API) for further processing.
- **AI Summarization:**
  - Uses LLMs (Ollama, OpenAI, etc.) to generate a concise professional summary and two interesting facts about the person.
- **Web Interface:**
  - Simple Flask web app for user input and result display.

---

## Project Structure
```
├── app.py                  # Flask web server
├── ice_breaker.py          # Main logic: orchestrates lookup, scraping, and summarization
├── agents/
│   └── linkedin_lookup_agent.py  # Agent for finding LinkedIn URLs
├── third_parties/
│   └── linkedin.py         # LinkedIn profile scraping logic
├── tools/
│   └── tools.py            # Utility tools for agents
├── output_parsers.py       # Output parsing and formatting
├── templates/
│   └── index.html          # Web UI template
├── .env                    # Environment variables (not committed)
├── README.md               # Project documentation
├── LICENSE                 # License info
```

---

## Setup & Usage

1. **Clone the repository:**
   ```sh
   git clone https://github.com/YoussefMIS/ice_breaker_project.git
   cd ice_breaker_project
   ```

2. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```
   *(Create a `requirements.txt` if not present, listing Flask, langchain, dotenv, requests, etc.)*

3. **Set up environment variables:**
   - Create a `.env` file in the project root with your API keys:
     ```env
     SCRAPIN_API_KEY=your_scrapin_api_key
     OPENAI_API_KEY=your_openai_api_key
     ```

4. **Run the app:**
   ```sh
   python app.py
   ```
   - Visit `http://localhost:5000` in your browser.

---

## Example
- Enter a name (e.g., "Youssef Shehata MegaSoft LinkedIn") in the web UI.
- The app will:
  1. Find the LinkedIn profile URL.
  2. Scrape (or mock) the profile data.
  3. Generate a summary and two interesting facts using an LLM.
  4. Display the results and profile picture.

---

## Technologies Used
- **Python 3**
- **Flask**
- **LangChain** (agents, tools, prompts)
- **Ollama / OpenAI LLMs**
- **dotenv**
- **requests**

---

## License
This project is licensed under the Apache 2.0 License. See [LICENSE](LICENSE) for details.

---

## Credits
This project was created as part of the Udemy course: **LangChain- Develop LLM powered applications with LangChain**.

---

## Disclaimer
- This project is for educational purposes. Do not use it for scraping or automating actions on LinkedIn in violation of their terms of service.

---

## Contact
For inquiries or feedback, please reach out to [youssefmis2002@hotmail.com](mailto:youssefmis2002@hotmail.com).
