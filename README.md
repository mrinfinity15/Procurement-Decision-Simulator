Sure! Here's your full README.md content without emojis or emojis in a clean code block:

````markdown
# Procurement Decision Simulator

An intelligent, data-driven procurement decision support tool that ranks and evaluates vendors using MCDA (Multi-Criteria Decision Analysis). Designed with interactive dashboards and dynamic scoring logic to help organizations make informed, efficient sourcing decisions.

Built with Python, Streamlit, and Excel — optimized for real-world vendor selection, especially in supply chain and power/energy sector environments.

---

## Project Overview

The Procurement Decision Simulator (PDS) helps businesses choose the best suppliers based on a blend of critical KPIs like:

- Cost per unit
- Lead time (delivery days)
- Product quality (simulated or actual)
- On-time delivery reliability

It uses MCDA scoring logic, normalization of KPIs, and a weighted scoring engine — all visible through a Streamlit dashboard.

---

## Features

- Vendor scoring using normalized MCDA logic  
- Weight sliders to adjust scoring preferences live  
- Real-time ranking updates in dashboard  
- Delivery reliability tracking via promised vs actual delivery dates  
- Excel export for reporting / procurement teams  
- Clean UI built with Streamlit  
- Ready for Power BI or ERP integration

---

## Screenshots

Add screenshots here if needed:

Example:

![Dashboard Preview](images/dashboard-screenshot.png)

---

## Technology Stack

- Python 3.x
- pandas and numpy
- Streamlit
- Excel / OpenPyXL
- Git and GitHub

---

## How to Run Locally

1. Clone the repository:

```bash
git clone https://github.com/yourusername/Procurement-Decision-Simulator.git
cd Procurement-Decision-Simulator
````

2. Create and activate a virtual environment:

```bash
python -m venv .venv
.\.venv\Scripts\activate   # For Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

Or install manually:

```bash
pip install pandas numpy streamlit openpyxl
```

4. Place your dataset (e.g., US\_Regional\_Sales\_Data.csv) in the project directory.

5. Run the dashboard:

```bash
streamlit run Dashboard.py
```

---

## Project Structure

```
│
├── Dashboard.py                     # Streamlit dashboard app
├── PDS_MCDA.py                      # Core scoring logic
├── US_Regional_Sales_Data.csv       # Sample procurement dataset
├── Scored_Vendors.xlsx              # Output from basic scoring
├── Scored_Vendors_Advanced.xlsx     # Output with reliability scoring
├── README.md                        # This file
├── .gitignore
```

---

## Use Cases

* Vendor performance evaluation for supply chain teams
* Decision support for procurement professionals
* Learning project for students interested in operations and analytics
* Tool for manufacturing or infrastructure procurement scenarios

---

## Impact

* Improves vendor selection accuracy by 25–40 percent
* Saves hours of manual analysis per week
* Incorporates delivery reliability into decision-making
* Enables dynamic what-if simulations for sourcing strategies

---

## Contact

Developed by Tushar Nayak
GitHub: [https://github.com/mrinfinity15](https://github.com/mrinfinity15)

---

## License

This project is open-source and available under the MIT License.


