**Data Visualization with Streamlit: Two Approaches**

This repository demonstrates two methods for creating data visualizations from CSV files using Streamlit,integrated with advanced AI tools. 
Below are the approaches used, along with their respective advantages and disadvantages:

________________________________________

**1. PandasAI with Ollama Models**

**•	Overview:**

Utilizes PandasAI, a library designed to integrate natural language queries with Pandas DataFrames. This approach leverages Ollama models for visualization generation.

**•	Advantages:**

o	Free usage of Ollama models (no subscription required).

o	Flexible and user-friendly integration with Pandas, which is a very new technology.

o	Offers advanced natural language capabilities for understanding prompts.


**•	Disadvantages:**

o	Requires very precise prompts to generate accurate visualizations, as this new technology is still being researched.

o	Ollama models are less fine-tuned compared to other state-of-the-art LLMs.

o	Some Streamlit integration issues on certain systems.

o	UI could be enhanced with additional tools like React.

________________________________________

**2. Gemini API**

**•	Overview:**

Employs the Gemini API, which utilizes highly advanced and well-trained models to facilitate data visualization.

**•	Advantages:**

o	Free API with access to cutting-edge AI models.

o	Easier implementation for creating visualizations.

o	More robust language processing compared to Ollama.


**•	Disadvantages:**

o	Requires explicit specification of the visualization type in code.

o	Lacks the dynamic adaptability seen in PandasAI for inferring visualization needs, along with API integration problems.

o	Performance could be further improved with additional training or optimizations.

________________________________________

**Suggestions for Future Improvements**

**1.	Custom LLM Development:**

o	Train a proprietary LLM tailored specifically for analyzing and visualizing data from CSV files.

**2.	OpenAI API Integration:**

o	For users without cost concerns, integrating OpenAI's GPT models can provide unparalleled natural language understanding and visualization capabilities. Although its capabilities are yet to be experimented.

**3.	Optimization:**
   
o	Develop faster and more efficient algorithms to process prompts and render visualizations seamlessly.

**4.	UI/UX Enhancements:**
	
o	Explore frontend frameworks like React or Angular to create a more polished user interface.

________________________________________

**Video Demonstrations**

To better understand the workflow, videos showcasing both approaches have been included in this repository are posted in youtube in the given link below.

**GeminiAI Approach :- **

**PandasAI Approach:- **

