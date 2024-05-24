# Main_Control.py
# Module에 있는 코드를 사용하기 위한 호출 담당

import sys
import os

# env_dir = os.environ.get("AI_CODE_DIR")
# sys.path.append(env_dir)  # Control 폴더가 있는 경로를 직접 추가


sys.path.append('../')  # 상위 디렉터리 추가

from API_CODE.Module import GPT_API


class Control:



    # 음성 인식처리 & 추천 기능 함수 호출
    def Control_SrInput(self, text, products):

        keyword = "예산"
        temp = text


        if temp.endswith("설명해줘."):
            call_GPT = Control.Call_Generate_Sentences(self, temp)
            return call_GPT
        elif temp.endswith("추천해줘."):
            allergy_Info = "계란"
            call_GPT = Control.recom_Function(self, allergy_Info, products)
            return call_GPT
        elif temp.endwith("장바구니에 담아줘.") : 

            ### 만약 문장 종결문이 "장바구니에 담아줘." 라는 내용이 있으면 ###

            # 사용자가 담고 싶어 하는 아이템이 DB Product 테이블에 존재 하는지 확인
            # 있으면 해당 아이템을 products에서 추출 후 return , 클라이언트는 해당 아이템 장바구니에 담는 코드 생성
            # 없으면 return 잘못된요청

            #클라이언트 측에서 데이터를 어떤 방식으로 ?
            
            if temp in products :
                return "테스트2"

            return "테스트"
        elif keyword in temp:
            call_GPT = Control.recom_Function_Budget(self, temp, products)
            return call_GPT

        else:
            return "테스트"

    # 추천 기능 호출 함수
    def recom_Function(self, allergy, products):
        allergy_Info = ""
        if allergy.endswith("알레르기"):
            allergy_Info = allergy
        else:
            temp = [allergy, "알레르기"]
            allergy_Info = " ".join(temp)

        call_GPT = GPT_API.USE_GPT()
        return_value = call_GPT.Recomm_Menu(allergy_Info, products)
        return return_value
    
    def recom_Function_Budget(self, temp, products):
        call_GPT = GPT_API.USE_GPT()
        return_value = call_GPT.Recomm_Menu(temp, products)
        return return_value

    # 답변 생성 기능 호출 함수
    def Call_Generate_Sentences(self, prompt):
        call_GPT = GPT_API.USE_GPT()
        result_value = call_GPT.generate_Sentences(prompt)
        return result_value
    
