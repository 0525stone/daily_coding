#-*- coding: utf-8 -*-
"""
1. interface 규정 - eliminate_josa_eomi_approximately(context) = eliminated_context

"""
def eliminate_josa_eomi_approximately_mecab():
    """
    나중에 해야할 것
    - 전체 프로세스에서 1번으로 이것을 거치고 unknown 으로 출력이 나오면 2번으로 넘어감
    """
    pass


def eliminate_josa_eomi_approximately_regex(text):
    result = ''

    # read josa, eomi files
    result = '현수 술주정뱅이'

    return result


# TODO : 이름이 이게 맞는지.. 이 프로그램 안에서는 조사,어미만 읽어오는 것이니까 이렇게 하는게 맞을까?
def read_josa_eomi():
    # JosaEomi/ EOMI.TXT  JOSA.TXT
    with open('./data/JosaEomi/EOMI.TXT','r', encoding='euc-kr') as f:
        dumps = f.read()
        dump = dumps.split('\n')
        
        # if에 사용할 eomi 조건문
        eomi_if = ' | '.join(dump)
        print(f'" {eomi_if} "')
        

def test_josa_eomi():
    read_josa_eomi()


    # test final result
    text = '현수는 술주정뱅이이다.'
    assert eliminate_josa_eomi_approximately_regex(text)=='현수 술주정뱅이'
    text = '알코올 의존증을 치료하려면 무엇이 필요할까?'
    assert eliminate_josa_eomi_approximately_regex(text)=='알코올 의존증 치료 필요'
    text = '자전거 여행을 가고 싶다.'
    assert eliminate_josa_eomi_approximately_regex(text)=='자전거 여행 가 싶'
    text = '거짓말로 들통 났다.'
    assert eliminate_josa_eomi_approximately_regex(text)=='거짓말 들통 났'

if __name__=="__main__":
    test_josa_eomi()