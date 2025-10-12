from scraper import scrape_nba_data
from data_analysis import filter_data_by_team, calculate_top_scorers
from visualizer import plot_top_scorers

def main():
    print("Scraping NBA data...")
    nba_data = scrape_nba_data()

    print("Filtering data for team: Lakers")
    lakers_data = filter_data_by_team(nba_data, 'LAL')

    print("Calculating top 10 scorers...")
    top_scorers = calculate_top_scorers(nba_data)

    print("Visualizing top scorers...")
    plot_top_scorers(top_scorers)

if __name__ == "__main__":
    main()
