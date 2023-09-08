"""my_var = 10
print(my_var)

my_list = [1, 2, 3]
print(*my_list)
print(my_list)"""
# 쉬프트 알트 A 로 전체 주석 단축기

# 정수 
my_int = 10
# 부동 소수점
my_float = 3.14
# 복소수
my_complex = 3 + 4j
""" print(my_int)
print(my_float)
print(my_complex) """

""" my_character = 'A'
my_char = "@"
print(my_character)
print(my_char)
my_string = 'Hello, World!'
str_name = "python"
print(my_string)
print(str_name) """

# 블리언 데이터 타입은 True or False 값을 가진다
""" my_bool = True
bFlag = False
print(my_bool, bFlag) """

# 리스트는 인덱스 순번이 들어간다
my_list = [10, 3, 8, 9, 42, "hello"]

""" print(*my_list)
print(my_list) """

""" print(my_list)
print(my_list.__len__()) #__len__()으로 리스트 크기확인 """

# [] 인덱스를 사용해 리스트 중 선택
""" print(my_list)
print(my_list[3])
my_list[3] = 't'
print(my_list) """

# 다른 문자열 계산 X
""" print(my_list[3] - my_list[5]) """

# 슬라이싱 자르는 거
""" slice_ls = my_list[2:5]
print(slice_ls) """

# 이중 리스트 리스트 안에 리스트 슬라이싱도 할 수 있음
my_list = [0, 3, 8, 9, 42, "hello", [5, 4, 2, "world"]]
""" print(my_list)
print(my_list[6][1]) """

# .찍으면 메소드들이 나옴 무슨 확장프로그램인지는 몰겟당

# .insert(순서, 값) index에 설정 값을 넣는다
my_list = [0, 3, 8, 9, 42, "hello"]
""" print(my_list)
my_list.insert(2,4)
print(*my_list) """

# .index() 해당 순서 출력 = [] 대괄호 사용

# .append(n) = 마지막 n 더해짐
""" print(my_list)
my_list.append(22)
print(*my_list)  """

# .count는 값의 동일한 요소 갯수 출력, 리스트에 없는 숫자를 넣으면 0 출력
my_list = [0, 3, 8, 9, 42, 8, "hello"]
""" print(my_list.count(5)) """

# .pop는 마지막 요소 출력후 삭제
""" print(my_list)
print(my_list.pop())
print(*my_list) """

# .sort()는 오름 차순, .reverse()는 역순, 숫자는 숫자 영어는 영어끼리
my_list = [0, 3, 8, 9, 42, 8]
""" print(my_list)
my_list.sort()
print(*my_list)
my_list.reverse()
print(*my_list) """

# 리스트.extend(리스트) 두 리스트를 결합, .clear은 ㅏㄱ제
""" my_list = [10, 3, 8, 9, 42, 8, "hello"]
list_tmp = [5, 7, "world"]
print(my_list, list_tmp)
my_list.extend(list_tmp)
print(*my_list)

list_tmp.clear()
print(list_tmp) """

# remove, dellist[] 사용해보기

""" my_tuple = (1, 2, 'three', True)
tpItem = (3.14, "b", 'two', False)
print(my_tuple)
print(tpItem) """

my_tup = (4, 2, 6, 1, "py", "w")
""" print(my_tup.__len__()) """

# 튜플은 데이터 변화이 안된다, 연산은 가능 my_tup[2] = 9

# 슬라이싱 [~부터:여까지짤라]
""" print(*my_tup[3:])
print(*my_tup[2:5]) """

# 이중튜플 가능
my_tup = (4, 2, 6, 1, "py", "w", ("h", 8, 7, 3))
""" print(my_tup)
print(my_tup[6][0])
 """
# 튜플 인덱스 (스타트와 엔드 설정해줘야함) 끝을 알기에 해주줘야함
""" my_tup = (4, 2, 6, 1, "py", "w")
print(my_tup.index(2, 0, 3))
print(my_tup.index("py", 3, 5)) """
# print(my_tup.index(1, 0, 3)) 없는 값 계산

#count 같은 값 몇개인지 나옴

#dictionary 딕셔너리 {}사용 키 값 설정

my_dict = {'key1' : 'value1', 'key2' : 'value2'}
my_item = my_dict.items()
print(my_item)

idx =("key1", "key2", "key3")
dicts = dict.fromkeys(idx, "0")
print(dicts)

my_dict = {'key1' : 'value1', 'key2' : 'value2'}
dicdata = {"name" : "python", "number" : 23564897}

print(my_dict['key1'])

my_dict = {'key1' : 'value1', 'key2' : 'value2'}
my_str = my_dict.get("key2")
print(my_str)

my_dict = {'key1' : 'value1', 'key2' : 'value2'}
print(my_dict.pop("key1"))
print(my_dict)

my_dict = {'key1' : 'value1', 'key2' : 'value2'}
dicts = my_dict.copy()
print(dicts)
print(my_dict)

my_dict = {'key1' : 'value1', 'key2' : 'value2'}
dicdata = {"name" : "python", "number" : 23564897}

my_dict["key3"] = "value3"
print(my_dict)

my_dict = {'key1' : 'value1', 'key2' : 'value2'}
my_dict.setdefault("key3")
print(my_dict)

my_dict = {'key1' : 'value1', 'key2' : 'value2'}
my_dict.update({"key1" : "v4"})
print(my_dict)

my_dict = {'key1' : 'value1', 'key2' : 'value2'}
del my_dict["key2"]
print(my_dict)

my_dict = {'key1' : 'value1', 'key2' : 'value2'}
print("key2" in my_dict)
print("key3" in my_dict)

my_dict = {'key1' : 'value1', 'key2' : 'value2'}
my_list = list(my_dict.keys())
print(my_list)

my_dict = {'key1' : 'value1', 'key2' : 'value2'}
my_set = set(my_dict.keys())
print(my_set)

my_dict = {'key1' : 'value1', 'key2' : 'value2'}
my_dict.clear()
print(my_dict)






