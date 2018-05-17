from vayse import BayesFilter

vy = BayesFilter()
vy.fit("파격 세일 오늘까지만 30%세일","광고")
vy.fit("쿠폰 선물 & 무료 배송","광고")
vy.fit("현대 백화점 세일","광고")
vy.fit("봄과 함께 찾아온 따뜻한 신제품 소식","광고")
vy.fit("인기 제품 기간 한정 세일","광고")

vy.fit("오늘 일정 확인","중요")
vy.fit("프로젝트 진행 상황 보고","중요")
vy.fit("계약 잘 부탁 드립니다","중요")
vy.fit("회의 일정이 등록되었습니다.","중요")
vy.fit("오늘 일정이 없습니다.","중요")

result = vy.predict("현재 프로젝트 진행 정보를 메일로 보내주세요")
print(result)
