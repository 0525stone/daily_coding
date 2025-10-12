import pandas as pd

# txt 파일에서 데이터를 읽고 엑셀 파일로 저장하는 함수
def txt_to_excel(input_file, output_file, delimiter):
    # txt 파일 읽기
    df = pd.read_csv(input_file, delimiter=delimiter, engine='python')
    
    # 엑셀 파일로 저장
    df.to_excel(output_file, index=False)
    print(f"'{input_file}' 파일이 '{output_file}'로 변환되었습니다.")

# 사용 예시
input_txt_file = 'gg/sample.txt'  # 입력 txt 파일명
output_excel_file = 'gg/output.xlsx'  # 출력 엑셀 파일명
delimiter = '\t'  # 구분자 (예: '\t'는 탭 구분자, ','는 콤마 구분자)

# 함수 호출
txt_to_excel(input_txt_file, output_excel_file, delimiter)