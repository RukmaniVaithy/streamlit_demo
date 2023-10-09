# Stock Data Explorer with Streamlit

This is a simple Streamlit application for exploring dummy stock data. The app generates dummy stock data, allows users to filter data by stock, and provides interactive visualizations.

## Getting Started

Follow these instructions to run the Streamlit app on your local machine.

### Prerequisites

Before running the app, make sure you have Python and Streamlit installed. You can install Streamlit using pip:

```bash
pip install streamlit
```

## Running the App:

### 1. Clone this repository to your local machine

```bash
git clone https://github.com/yourusername/stock-data-explorer.git
```

### 2. Navigate to the project repository

```bash
cd streamlit_demo
```

### 3. Running the Streamlit app from diffent interface

### 3.1 Run the streamlit app as standalone application

```bash
streamlit run streamlit_app.py
```

Open your web browser and navigate to http://localhost:8501. You will see the Stock Data Explorer app running.

### 3.2 Run the streamlit app from Jupyter notebook

### Prerequisites

Before running the app, make sure you have Python and Streamlit installed. You can install Streamlit using pip. And make sure there is an active Jupyter notebook environment.

```bash
jupyter nbconvert --to script Streamlit_Jupyter.ipynb # convert jupyter notebook to script
awk '!/ipython/' Streamlit_Jupyter.py > temp.py && mv temp.py app.py && rm Streamlit_Jupyter.py #remove ipython widgets and create app.py
streamlit run app.py
```

## 3.3 Host the streamlit application in Jupyter Hub instead of running as stand-alone application

Goal: 

- To share the interactive dashboard to small group of colleagues having access to org's Jupyter Hub environment.

JupyterHub Plugin to Use:

- [ContainDS Dashboards](https://cdsdashboards.readthedocs.io/en/stable/)

Advantage:

- Deploy dashboards developed in JHub securely to JHub environment automatically

- Framework agnostic and supports deploying dashboards written using open source framework - Plotly Dash, Voila, Streamlit, ...

- Shareable Dahsboards to selected JupyterHub users by linking to SSO


## Usage:

- Select a stock from the dropdown menu to filter the data.
- Choose the type of visualization (Line Chart or Bar Chart) to view stock prices.
- Explore the data and visualize stock prices interactively.

## Built With

- [Streamlit](https://streamlit.io/) - The web app framework used for creating interactive data applications.

## Author:

- https://github.com/RukmaniVaithy

## Acknowledgements

- Inspiration: [Streamlit Documentation](https://chat.openai.com/c/f6dd3f86-d37f-4cd9-b4a9-7d88cf2eb14a#:~:text=Streamlit%20Documentation)
- [ContainDS Dashboard](https://cdsdashboards.readthedocs.io/en/stable/)
- [Running Streamlit inside Jupyter Notebook](https://github.com/SurendraRedd/StreamlitProjects/blob/master/Streamlit.ipynb)
- [Improving Streamlit Performance](https://blog.streamlit.io/six-tips-for-improving-your-streamlit-app-performance/)



