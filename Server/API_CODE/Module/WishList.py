#WishList.py

from typing import List, Dict

# 메모리에 장바구니 데이터를 저장할 딕셔너리
cart_data: Dict[int, List[str]] = {}


class WishList():

    def checkWishlist(self, user_id, items):

        if user_id not in cart_data:
            cart_data[user_id] = []

        # 장바구니에 아이템 추가
        cart_data[user_id].extend(items)

        # 장바구니에 아이템 추가
        cart_data[user_id].extend(items)
        # 장바구니에 아이템 추가
        cart_data[user_id].extend(items)
        return {
            "message": f"{', '.join(items)} 이(가) 장바구니에 추가되었습니다.",
            "items": items,
        }
    
