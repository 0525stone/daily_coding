from eliminate_josa_eomi_approximately import eliminate_josa_eomi_approximately_regex_ifor, read_josa_eomi


def test():

    # test : read_josa_eomi()  => 직접 일일이 셀 수 없으니까, txt 파일의 line 수로 확인
    eomis, eomis_if = read_josa_eomi('./data/JosaEomi/EOMI.TXT')
    assert len(eomis)==744
    josas, josas_if = read_josa_eomi('./data/JosaEomi/JOSA.TXT')
    assert len(josas)==429
    print('read_josa_eomi test done')

    texts = ['알코올 의존증을 치료할 생각이 있을쏘냐?', '자전거 여행을 가고 싶다.',  '거짓말로 들통 났다.', '현수는 술주정뱅이다.', '주의가 부족했다.']
    answers_josa = ['알코올 의존증 치료할 생각 있을쏘냐', '자전거 여행 가 싶', '거짓말 들통 났', '현수 술주정뱅' , '주의 부족했']  # 술주정뱅이=>술주정뱅
    answers_josa_eomi = ['알코올 의존증 치료할 생각 있', '자전거 여행 가 싶', '거짓말 들통 났', '현수 술주정뱅' , '주의 부족했']  # 술주정뱅이=>술주정뱅

    for text, answer in zip(texts, answers_josa):
        assert eliminate_josa_eomi_approximately_regex_ifor(text, josas_if)==answer
    print('only josa elimination test is done')

    for text, answer in zip(texts, answers_josa_eomi):
        assert eliminate_josa_eomi_approximately_regex_ifor(text, eomis_if, josas_if)==answer
    print('both josa and eomi test is done')
    
    
    
    print('current test cases all done')




if __name__=="__main__":
    test()