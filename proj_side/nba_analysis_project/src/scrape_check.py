"""
241119
- nba_api 를 사용하여 정보들 열람하는 것이 좋을 듯
- 구조는 기존에 가져온것 그대로 가져가되, 요소들에 대한 디버깅 필요

nba_analysis_project/
├── data/               # 크롤링 및 API 데이터를 저장
├── notebooks/          # 데이터 전처리 및 분석
├── reports/            # 리포트 결과물
├── src/                # 주요 파이썬 코드
│   ├── scraper.py      # 크롤링 코드
│   ├── data_analysis.py # 데이터 분석
│   ├── visualizer.py   # 시각화 코드
│   └── main.py         # 실행 코드
├── tests/              # 테스트 코드
├── requirements.txt    # 필요한 라이브러리
└── README.md           # 프로젝트 설명
"""

from nba_api.stats.static import teams
from nba_api.stats.endpoints import leaguedashplayerstats
import pandas as pd

def fetch_nba_data(season='2023-24'):
    # NBA 팀 데이터 가져오기
    nba_teams = teams.get_teams()
    print(f"Found {len(nba_teams)} teams.")

    # 선수 통계 데이터 가져오기
    player_stats = leaguedashplayerstats.LeagueDashPlayerStats(season=season).get_data_frames()[0]

    # 주요 컬럼 선택
    columns = ['PLAYER_NAME', 'TEAM_ABBREVIATION', 'PTS', 'REB', 'AST', 'STL', 'BLK']
    player_stats = player_stats[columns]

    return player_stats

def main():
    print("Fetching NBA data...")
    nba_data = fetch_nba_data()
    print(nba_data.head())  # 상위 5개 데이터 출력

    # 데이터 저장
    nba_data.to_csv('nba_player_stats.csv', index=False)
    print("Data saved to 'nba_player_stats.csv'.")

if __name__ == "__main__":
    main()