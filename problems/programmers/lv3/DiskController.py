# Programmers 42627 디스크 컨트롤러
# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/42627
# 난이도: LV3
# 시간 복잡도: O(N log N)
# 공간 복잡도: O(N)

# 문제
# 하드디스크는 한 번에 하나의 작업만 수행
# 우선순위 디스크 컨트롤러라는 가상의 장치를 이용한다고 가정
# 동작
# 1. 어떤 작업 요청이 들어왔을 때 [작업의 번호, 작업의 요청 시각, 작업의 소요 시간]을 저장해 두는 대기 큐
# 처음에 큐는 비어있다.

# 2. 디스크 컨트롤러는 하드 디스크가 작업을 하고 있지 않고 대기 큐가 비어있지 않다면
# 가장 우선순위가 높은 작업을 대기 큐에 꺼내서 하드디스크에 그 작업을 시킴.
# 이때, [작업의 소요시간이 짧은 것, 작업의 요청 시각이 빠른 것, 작업의 번호가 작은 것]순으로
# 우선순위가 높음.

# 3. 하드디스크는 작업을 한 번 시작하면 작업을 마칠 때까지 그 작업만 수행

# 4. 하드디스크가 어떤 작업을 마치는 시점과 다른 작업 요청이 들어오는 시점이 겹친다면
# 하드디스크가 작업을 마치자마자 디스크 컨트롤러는 요청이 들어온 작업을 대기큐에 저장한 뒤
# 우선순위가 높은 작업을 대기 큐에서 꺼내서 하드디스크에 그 작업을 시킴.
# 또, 하드디스크가 어떤 작업을 마치는 시점에 다른 작업이 들어오지 않더라도 그 작업을 마치자마자
# 또 다른 작업을 시작할 수 있음. 이 과정에서 걸리는 시간은 없다고 가정한다.

import heapq


def solution(jobs):
    # 전체 작업 수: 모든 작업을 끝냈는지 확인하고 평균을 계산할 때 사용한다.
    job_count = len(jobs)

    # 현재 시각까지 요청된 작업을 저장하는 최소 힙이다.
    # 힙에는 (소요시간, 요청시간, 작업번호) 순서로 넣는다.
    # heapq는 튜플의 앞쪽 값부터 비교하므로 문제의 우선순위가 그대로 적용된다.
    waiting_jobs = []

    # jobs[i]의 i가 작업 번호이다.
    # 요청이 들어오는 순서대로 확인할 수 있도록 요청시간 기준으로 정렬한다.
    sorted_jobs = sorted(
        (request_time, duration, job_number)
        for job_number, (request_time, duration) in enumerate(jobs)
    )

    # current_time: 디스크가 다음 작업을 시작할 수 있는 현재 시각
    # total_turnaround_time: 각 작업의 반환 시간을 모두 더한 값
    # next_job: sorted_jobs에서 다음으로 확인할 작업의 위치
    # completed_jobs: 처리를 끝낸 작업의 수
    current_time = 0
    total_turnaround_time = 0
    next_job = 0
    completed_jobs = 0

    while completed_jobs < job_count:
        # 요청시간이 현재 시각 이하라면 이미 요청이 들어온 작업이다.
        # 그런 작업을 모두 대기 큐에 넣은 뒤 우선순위를 비교한다.
        while (next_job < job_count and sorted_jobs[next_job][0] <= current_time):
            request_time, duration, job_number = sorted_jobs[next_job]
            heapq.heappush(waiting_jobs,(duration, request_time, job_number),)
            next_job += 1

        if waiting_jobs:
            # 가장 먼저 나온 작업이 현재 대기 중인 작업 중 우선순위가 가장 높다.
            duration, request_time, job_number = heapq.heappop(waiting_jobs)

            # 작업을 시작하면 중간에 멈출 수 없으므로 소요시간만큼 시간이 흐른다.
            current_time += duration

            # 반환 시간 = 작업이 끝난 시각 - 작업을 요청한 시각
            total_turnaround_time += current_time - request_time
            completed_jobs += 1
        else:
            # 대기 중인 작업이 없으면 시간을 1씩 증가시킬 필요가 없다.
            # 다음 작업이 요청되는 시각으로 바로 이동한다.
            current_time = sorted_jobs[next_job][0]

    # 문제에서 평균의 소수점 이하는 버리라고 했으므로 정수 나눗셈을 사용한다.
    return total_turnaround_time // job_count
