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
    def Control_SrInput(self):
        temp = "점심 메뉴 추천해줘"
        # temp = input("입력 : ")
        if temp.endswith("설명해줘"):
            call_GPT = Control.Call_Generate_Sentences(self, temp)
            return call_GPT
        elif temp.endswith("추천해줘"):
            # allergy_Info = input("알레르기 정보를 입력해주세요! : ")
            allergy_Info = "계란"
            call_GPT = Control.recom_Function(self, allergy_Info)
            return call_GPT
        else:
            print("테스트2")

    # 추천 기능 호출 함수
    def recom_Function(self, allergy):
        allergy_Info = ""
        if allergy.endswith("알레르기"):
            allergy_Info = allergy
        else:
            temp = [allergy, "알레르기"]
            allergy_Info = " ".join(temp)

        call_GPT = GPT_API.USE_GPT()
        return_value = call_GPT.Recomm_Menu(allergy_Info)
        return return_value

    # 답변 생성 기능 호출 함수
    def Call_Generate_Sentences(self, prompt):
        call_GPT = GPT_API.USE_GPT()
        result_value = call_GPT.generate_Sentences(prompt)
        return result_value
