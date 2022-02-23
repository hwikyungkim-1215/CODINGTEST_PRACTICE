'''
이진 탐색: 이미 정렬이 되어있는 배열에서 원하는 원소를 효율적으로 찾을 수 있는 알고리즘
1. 이미 정렬된 상태이므로 반을 짤라 찾는 원소가 왼쪽인지 오른쪽인지 확인해 아닌 부분은 버린다.
2. 시작 부분(start), 끝 부분(end) = len(arr) - 1
3. data 중에서 target 을 검색하여 index 값을 return 한다.
4. 없으면 None을 return한다.
'''

def binary_search(target, data):
    data.sort() #정렬 먼저
    start = 0
    end = len(data) - 1

    while start <= end:
        # 중간 값 저장
        mid = (start + end) // 2

        # 함수를 끝내버린다
        if data[mid] == target:
            return mid
        # target이 더 크면 start를 오른쪽으로, 작으면 왼쪽으로 옮긴다
        elif data[mid] < target:
            start = mid + 1
        else:
            end = mid -1

    return None

# 테스트용 코드
if __name__ == "__main__":
  li = [i for i in range(11)]
  print(li)
  target = 9
  idx = binary_search(target, li)

  if idx:
      print(li[idx])
  else:
      print("찾으시는 타겟 {}가 없습니다".format(target))