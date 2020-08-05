# 2020 카카오 인턴십1 키패드 누르기
# https://programmers.co.kr/learn/courses/30/lessons/67256?language=python3
def solution(numbers, hand):
    left_hand = "*"
    right_hand = "#"
    left = ['1', '4', '7', '*']
    right = ['3', '6', '9', '#']
    mid = ['2', '5', '8', '0']
    answer = ''

    for number in numbers:
        if str(number) in left:
            answer += "L"
            left_hand = str(number)
        elif str(number) in right:
            answer += "R"
            right_hand = str(number)
        else:
            left_distance = 0
            right_distance = 0
            isLeftHandInMid = False
            isRightHandInMid = False

            if left_hand in left:
                left_distance += 1
            else:
                isLeftHandInMid = True
            if right_hand in right:
                right_distance += 1
            else:
                isRightHandInMid = True

            if isLeftHandInMid:
                left_distance += abs(mid.index(str(number))-mid.index(left_hand))
            else:
                left_distance += abs(mid.index(str(number))-left.index(left_hand))

            if isRightHandInMid:
                right_distance += abs(mid.index(str(number))-mid.index(right_hand))
            else:
                right_distance += abs(mid.index(str(number))-right.index(right_hand))

            if left_distance< right_distance:
                answer +="L"
                left_hand = str(number)
            elif left_distance> right_distance:
                answer +="R"
                right_hand = str(number)
            else:
                if hand=="right":
                    answer += "R"
                    right_hand = str(number)
                else:
                    answer += "L"
                    left_hand = str(number)

    return answer


if __name__ == "__main__":
    print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))  # "LRLLLRLLRRL"
    print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left"))  # "LRLLRRLLLRR"
    print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right"))  # "LLRLLRLLRL"
