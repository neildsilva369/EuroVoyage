# ✦ EuroVoyage

A premium, interactive Europe travel finder built with Python and Streamlit.

EuroVoyage lets users compare:

- ✈️ Flights
- 🚆 Trains
- 🚌 Buses
- 💶 Indicative fares
- ⏱️ Journey durations
- 🔎 Origin/destination searches
- ↕️ Price and duration sorting
- 📅 Travel dates
- 👥 Passenger count

## Project structure

```text
EuroVoyage/
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
├── data/
│   └── trips.csv
└── assets/
    └── .gitkeep
```

## Run locally

Python 3.10+ is recommended.

```bash
pip install -r requirements.txt
streamlit run app.py
```

The app will open in your browser.

## Deploy with GitHub + Streamlit Community Cloud

1. Create a GitHub repository called `eurovoyage`.
2. Upload this entire project.
3. Open Streamlit Community Cloud.
4. Choose **New app**.
5. Select your GitHub repository.
6. Select the `main` branch.
7. Set the main file to `app.py`.
8. Click **Deploy**.

## Important pricing note

The included CSV contains sample/indicative fares for demonstration.

For a real travel product, connect the app to licensed/live travel data providers
and update the results based on the selected date, passenger count, availability,
baggage rules and currency.

Do not put API keys directly in GitHub. Use Streamlit secrets/environment variables
for private credentials.

## Future upgrades

- Live flight/train/bus APIs
- Hotel search
- Europe map
- Currency conversion
- Saved trips
- User accounts
- Trip itinerary builder
- Booking links
- Multi-city journeys
- Price alerts
- Destination discovery
