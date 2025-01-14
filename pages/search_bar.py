import streamlit as st

# text를 입력하는 검색창을 하나 만듭니다.
# ani_list에 있는 글자가 일부라도 들어가면
# img_list에 있는 해당 그림이 출력되는 검색창을 하나 만들어주세요


ani_list = ['짱구는못말려', '몬스터','릭앤모티']
img_list = ['https://i.imgur.com/t2ewhfH.png', 
            'https://i.imgur.com/ECROFMC.png', 
            'https://i.imgur.com/MDKQoDc.jpg']


# 검색창 UI
st.title("")
search = st.text_input(input("찾을 애니메이션 이름을 입력하세요."))

print(search)


# 검색 로직
for ani in ani_list:
    if search in ani[0] :
        img_idx = ani_list.index(ani)

if search == '': # 초기 상태를 이미지없이 실행
    st.image(img_list(img_idx))